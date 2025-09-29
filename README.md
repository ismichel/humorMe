# HumorMe - An Audio Humor Detection Demo

A full-fledged web application that records audio and classifies whether it's funny or not using a fine-tuned HuggingFace model. The app features real-time audio recording, file upload capabilities, and a modern, responsive UI.

## Features

- **Real-time Audio Recording**: Record audio directly in the browser
- **File Upload Support**: Upload audio files (.wav, .mp3, .m4a, etc.)
- **AI Classification**: Uses fine-tuned wav2vec model for humor detection
- **Modern UI**: Beautiful, responsive design with real-time feedback
- **Confidence Scores**: Shows detailed confidence scores for predictions
- **Audio Validation**: Ensures minimum/maximum audio length requirements

## Model Performance

The app uses a fine-tuned HuggingFace model (`rishiA/humor_model_v4`) that achieves **86% accuracy** on humor detection tasks.

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser with microphone access

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd humorMe
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

### Production Deployment

For production deployment, you can use Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## How to Use

### Recording Audio
1. Click "🎤 Start Recording"
2. Speak something funny or serious
3. Click "⏹️ Stop Recording" when done
4. Wait for the AI analysis

### Uploading Files
1. Click "📁 Choose Audio File"
2. Select an audio file from your device
3. Wait for the AI analysis

### Understanding Results
- **😂 FUNNY**: The AI detected humor in your audio
- **😐 NOT FUNNY**: The AI detected serious/non-humorous content
- **Confidence Score**: How certain the AI is about its prediction
- **Detailed Scores**: Breakdown of funny vs not-funny probabilities

## 🔧 Technical Details

### Backend (Flask)
- **Framework**: Flask with CORS support
- **Audio Processing**: librosa for audio preprocessing
- **Model Integration**: HuggingFace Transformers pipeline
- **File Handling**: Temporary file management for audio processing

### Frontend (HTML/CSS/JavaScript)
- **Audio Recording**: Web Audio API with MediaRecorder
- **File Upload**: Drag-and-drop file input
- **Responsive Design**: Mobile-friendly interface
- **Real-time Feedback**: Status updates and progress indicators

### Audio Processing Pipeline
1. **Input Validation**: Check file format and duration
2. **Preprocessing**: Resample to 16kHz, normalize length
3. **Model Inference**: Pass through fine-tuned wav2vec model
4. **Post-processing**: Extract confidence scores and predictions

## 📊 Model Architecture

The app uses a fine-tuned version of Facebook's wav2vec model:
- **Base Model**: `facebook/hubert-large-ls960-ft`
- **Task**: Binary classification (funny vs not funny)
- **Training**: Custom dataset with class weighting
- **Performance**: 86% accuracy on test set

## 🎨 Customization

### Styling
The UI uses CSS custom properties and can be easily customized by modifying the styles in `templates/index.html`.

### Model Configuration
To use a different model, update the model name in `app.py`:
```python
classifier = pipeline("audio-classification", model="your-model-name")
```

### Audio Constraints
Modify audio length constraints in `app.py`:
```python
# Minimum length (0.5 seconds)
if len(audio_data) < 8000:
    
# Maximum length (30 seconds)
if len(audio_data) > 480000:
```

## Performance Optimization

- **Model Caching**: Model is loaded once at startup
- **Temporary Files**: Automatic cleanup of processed audio files
- **Audio Compression**: Optimized audio preprocessing pipeline
- **Async Processing**: Non-blocking audio classification

## License

This project is open source and available under the MIT License.
---