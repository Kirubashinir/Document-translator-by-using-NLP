# Simple test script for NLP Document Translator
import sys

def test_basic_imports():
    print("Testing basic imports...")
    
    try:
        import flask
        print("[OK] Flask")
    except ImportError as e:
        print(f"[ERROR] Flask: {e}")
        return False
    
    try:
        from flask_cors import CORS
        print("[OK] Flask-CORS")
    except ImportError as e:
        print(f"[ERROR] Flask-CORS: {e}")
        return False
    
    try:
        from langdetect import detect
        print("[OK] langdetect")
    except ImportError as e:
        print(f"[ERROR] langdetect: {e}")
        return False
    
    try:
        from deep_translator import GoogleTranslator
        print("[OK] deep-translator")
    except ImportError as e:
        print(f"[ERROR] deep-translator: {e}")
        return False
    
    try:
        from gtts import gTTS
        print("[OK] gTTS")
    except ImportError as e:
        print(f"[ERROR] gTTS: {e}")
        return False
    
    try:
        from docx import Document
        print("[OK] python-docx")
    except ImportError as e:
        print(f"[ERROR] python-docx: {e}")
        return False
    
    try:
        from pdfminer.high_level import extract_text
        print("[OK] pdfminer.six")
    except ImportError as e:
        print(f"[ERROR] pdfminer.six: {e}")
        return False
    
    return True

def test_quick_functionality():
    print("\nTesting quick functionality...")
    
    # Test language detection
    try:
        from langdetect import detect
        detected = detect("This is English text")
        print(f"[OK] Language detection: {detected}")
    except Exception as e:
        print(f"[ERROR] Language detection: {e}")
        return False
    
    # Test translation
    try:
        from deep_translator import GoogleTranslator
        translator = GoogleTranslator(source='en', target='es')
        result = translator.translate('Hello')
        print(f"[OK] Translation: Hello -> {result}")
    except Exception as e:
        print(f"[ERROR] Translation: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("=" * 40)
    print("NLP Document Translator - Quick Test")
    print("=" * 40)
    print(f"Python version: {sys.version}")
    
    if test_basic_imports():
        print("\n[SUCCESS] All imports working!")
        
        if test_quick_functionality():
            print("\n[SUCCESS] Basic functionality working!")
            print("\nYou can now run the application:")
            print("1. python app.py")
            print("2. Or run_app.bat")
        else:
            print("\n[WARNING] Some functionality issues detected")
    else:
        print("\n[ERROR] Import issues detected")
        print("Please install missing packages with: pip install -r requirements.txt")