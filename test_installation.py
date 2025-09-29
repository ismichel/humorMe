#!/usr/bin/env python3
"""
Test script for HumorMe application
Verifies that all dependencies are properly installed and the model can be loaded.
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'flask',
        'flask_cors', 
        'transformers',
        'torch',
        'librosa',
        'soundfile',
        'numpy',
        'scipy',
        'requests'
    ]
    
    print("🔍 Testing package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    return failed_imports

def test_model_loading():
    """Test if the HuggingFace model can be loaded"""
    print("\n🤖 Testing model loading...")
    try:
        from transformers import pipeline
        print("✅ Transformers pipeline imported successfully")
        
        # Try to load the model (this will download it if not cached)
        print("📥 Loading humor detection model...")
        classifier = pipeline("audio-classification", model="rishiA/humor_model_v4")
        print("✅ Model loaded successfully!")
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🎭 HumorMe Installation Test")
    print("=" * 40)
    
    # Test Python version
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python {python_version.major}.{python_version.minor}.{python_version.micro} (requires 3.8+)")
        return False
    
    # Test package imports
    failed_imports = test_imports()
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Please install missing packages with: pip install -r requirements.txt")
        return False
    
    # Test model loading
    model_loaded = test_model_loading()
    
    # Summary
    print("\n" + "=" * 40)
    if not failed_imports and model_loaded:
        print("🎉 All tests passed! HumorMe is ready to run.")
        print("Run: python app.py")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
