@echo off
title NLP Document Translator - Debug Mode
color 0E
echo.
echo ================================================================
echo           NLP Document Translator - DEBUG MODE
echo ================================================================
echo.

REM Run comprehensive test
echo [DEBUG] Running comprehensive tests...
python simple_test.py
echo.

REM Show current directory contents
echo [DEBUG] Current directory contents:
dir /b
echo.

REM Show Python path and version details
echo [DEBUG] Python details:
python -c "import sys; print('Python executable:', sys.executable)"
python -c "import sys; print('Python path:', sys.path[:3])"
echo.

REM Test individual components
echo [DEBUG] Testing individual components...

echo Testing Flask app import...
python -c "import app; print('App module imported successfully')" 2>&1

echo.
echo Testing language detection...
python -c "from langdetect import detect; print('Detected language for Hello World:', detect('Hello World'))" 2>&1

echo.
echo Testing translation...
python -c "from deep_translator import GoogleTranslator; t=GoogleTranslator(source='en', target='es'); print('Translation test:', t.translate('Hello'))" 2>&1

echo.
echo Testing TTS...
python -c "from gtts import gTTS; print('TTS module loaded successfully')" 2>&1

echo.
echo [DEBUG] Starting application in debug mode...
echo Press Ctrl+C to stop
echo.

REM Start with debug output
python -u app.py

echo.
echo [DEBUG] Application stopped
pause