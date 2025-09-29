from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import tempfile
import librosa
import soundfile as sf
import numpy as np
from transformers import pipeline
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('humorMe.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize the humor classification pipeline
try:
    classifier = pipeline("audio-classification", model="rishiA/humor_model_v2")
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    classifier = None

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_audio():
    """Classify uploaded audio as funny or not funny"""
    try:
        if not classifier:
            return jsonify({'error': 'Model not loaded'}), 500
        
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            audio_file.save(tmp_file.name)
            
            try:
                # Load and preprocess audio
                audio_data, sr = librosa.load(tmp_file.name, sr=16000)
                
                # Ensure audio is not too short (at least 0.5 seconds)
                if len(audio_data) < 8000:  # 0.5 seconds at 16kHz
                    return jsonify({'error': 'Audio too short. Please record at least 0.5 seconds.'}), 400
                
                # Ensure audio is not too long (max 30 seconds)
                if len(audio_data) > 480000:  # 30 seconds at 16kHz
                    audio_data = audio_data[:480000]
                
                # Save processed audio
                processed_path = tmp_file.name.replace('.wav', '_processed.wav')
                sf.write(processed_path, audio_data, 16000)
                
                # Classify the audio
                result = classifier(processed_path)
                
                # Parse results
                funny_score = 0
                not_funny_score = 0
                
                for item in result:
                    if item['label'] == 'LABEL_1':
                        funny_score = item['score']
                    else:
                        not_funny_score = item['score']
                
                # Determine prediction
                is_funny = funny_score > not_funny_score
                confidence = max(funny_score, not_funny_score)
                
                return jsonify({
                    'prediction': 'funny' if is_funny else 'not funny',
                    'confidence': round(confidence * 100, 2),
                    'funny_score': round(funny_score * 100, 2),
                    'not_funny_score': round(not_funny_score * 100, 2),
                    'success': True
                })
                
            finally:
                # Clean up temporary files
                try:
                    os.unlink(tmp_file.name)
                    if os.path.exists(processed_path):
                        os.unlink(processed_path)
                except:
                    pass
                    
    except Exception as e:
        logger.error(f"Error processing audio: {e}")
        return jsonify({'error': f'Error processing audio: {str(e)}'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': classifier is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
