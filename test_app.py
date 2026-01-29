#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for NLP Document Translator & TTS Application
"""

import sys
import os

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    
    try:
        import flask
        print("[OK] Flask imported successfully")
    except ImportError as e:
        print(f"[ERROR] Flask import failed: {e}")
        return False
    
    try:
        from flask_cors import CORS
        print("[OK] Flask-CORS imported successfully")
    except ImportError as e:
        print(f"[ERROR] Flask-CORS import failed: {e}")
        return False
    
    try:
        from langdetect import detect
        print("[OK] langdetect imported successfully")
    except ImportError as e:
        print(f"[ERROR] langdetect import failed: {e}")
        return False
    
    try:
        from deep_translator import GoogleTranslator
        print("[OK] deep-translator imported successfully")
    except ImportError as e:
        print(f"[ERROR] deep-translator import failed: {e}")
        return False
    
    try:
        from gtts import gTTS
        print("[OK] gTTS imported successfully")
    except ImportError as e:
        print(f"[ERROR] gTTS import failed: {e}")
        return False
    
    try:
        from docx import Document
        print("[OK] python-docx imported successfully")
    except ImportError as e:
        print(f"[ERROR] python-docx import failed: {e}")
        return False
    
    try:
        from pdfminer.high_level import extract_text
        print("[OK] pdfminer.six imported successfully")
    except ImportError as e:
        print(f"[ERROR] pdfminer.six import failed: {e}")
        return False
    
    return True

def test_translation():
    """Test translation functionality"""
    print("\nTesting translation...")
    
    try:
        from deep_translator import GoogleTranslator
        translator = GoogleTranslator(source='en', target='es')
        result = translator.translate('Hello world')
        print(f"[OK] Translation test: 'Hello world' -> '{result}'")
        return True
    except Exception as e:
        print(f"✗ Translation test failed: {e}")
        return False

def test_language_detection():
    """Test language detection"""
    print("\nTesting language detection...")
    
    try:
        from langdetect import detect
        text = "This is a sample English text for testing."
        detected = detect(text)
        print(f"✓ Language detection test: '{text}' -> '{detected}'")
        return True
    except Exception as e:
        print(f"✗ Language detection test failed: {e}")
        return False

def test_tts():
    """Test text-to-speech"""
    print("\nTesting TTS...")
    
    try:
        from gtts import gTTS
        import tempfile
        import os
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        tts = gTTS(text="Hello world", lang='en')
        tts.save(temp_path)
        
        if os.path.exists(temp_path) and os.path.getsize(temp_path) > 0:
            print("✓ TTS test successful")
            os.unlink(temp_path)  # Clean up
            return True
        else:
            print("✗ TTS test failed: No audio file generated")
            return False
            
    except Exception as e:
        print(f"✗ TTS test failed: {e}")
        return False

def check_directories():
    """Check if required directories exist"""
    print("\nChecking directories...")
    
    required_dirs = ['uploads', 'audio', 'static', 'static/css', 'static/js', 'templates']
    
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ Directory '{dir_name}' exists")
        else:
            print(f"✗ Directory '{dir_name}' missing - creating...")
            os.makedirs(dir_name, exist_ok=True)
            print(f"✓ Directory '{dir_name}' created")

def check_files():
    """Check if required files exist"""
    print("\nChecking files...")
    
    required_files = [
        'app.py',
        'templates/index.html',
        'static/css/style.css',
        'static/js/app.js',
        'requirements.txt'
    ]
    
    all_exist = True
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"✓ File '{file_name}' exists")
        else:
            print(f"✗ File '{file_name}' missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("=" * 50)
    print("NLP Document Translator & TTS - System Test")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Run tests
    tests_passed = 0
    total_tests = 6
    
    if test_imports():
        tests_passed += 1
    
    if test_language_detection():
        tests_passed += 1
    
    if test_translation():
        tests_passed += 1
    
    if test_tts():
        tests_passed += 1
    
    check_directories()
    
    if check_files():
        tests_passed += 1
        print("✓ All required files exist")
    else:
        print("✗ Some required files are missing")
    
    # Final summary
    print("\n" + "=" * 50)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("✓ All tests passed! The application should work correctly.")
        print("\nTo start the application:")
        print("1. Run: python app.py")
        print("2. Or double-click: run_app.bat")
        print("3. Open browser to: http://localhost:5000")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return False
    
    return True

if __name__ == "__main__":
    main()