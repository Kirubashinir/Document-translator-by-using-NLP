@echo off
title NLP Document Translator & TTS Application
color 0A
echo.
echo ================================================================
echo           NLP Document Translator ^& TTS Application
echo ================================================================
echo.

REM Check if Python is installed
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.8+ and add it to your PATH.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Display Python version
python --version
echo [OK] Python is available
echo.

REM Check if pip is available
echo [2/6] Checking pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available!
    pause
    exit /b 1
)
echo [OK] pip is available
echo.

REM Run quick test
echo [3/6] Testing dependencies...
python simple_test.py
if errorlevel 1 (
    echo.
    echo [INFO] Installing missing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies!
        echo Please check your internet connection and try again.
        pause
        exit /b 1
    )
    echo [OK] Dependencies installed successfully!
)
echo.

REM Create necessary directories
echo [4/6] Creating directories...
if not exist "uploads" (
    mkdir uploads
    echo [OK] Created uploads directory
)
if not exist "audio" (
    mkdir audio
    echo [OK] Created audio directory
)
if not exist "static" (
    mkdir static
    echo [OK] Created static directory
)
if not exist "static\css" (
    mkdir static\css
    echo [OK] Created static\css directory
)
if not exist "static\js" (
    mkdir static\js
    echo [OK] Created static\js directory
)
if not exist "templates" (
    mkdir templates
    echo [OK] Created templates directory
)
echo [OK] All directories ready
echo.

REM Check if all files exist
echo [5/6] Checking application files...
if not exist "app.py" (
    echo [ERROR] app.py not found!
    pause
    exit /b 1
)
if not exist "templates\index.html" (
    echo [ERROR] templates\index.html not found!
    pause
    exit /b 1
)
if not exist "static\css\style.css" (
    echo [ERROR] static\css\style.css not found!
    pause
    exit /b 1
)
if not exist "static\js\app.js" (
    echo [ERROR] static\js\app.js not found!
    pause
    exit /b 1
)
echo [OK] All application files present
echo.

REM Start the Flask application
echo [6/6] Starting Flask application...
echo.
echo ================================================================
echo                    APPLICATION STARTING
echo ================================================================
echo.
echo ^> Server will start on: http://localhost:5000
echo ^> Open your web browser and navigate to the above URL
echo ^> Press Ctrl+C to stop the server
echo ^> Close this window to stop the application
echo.
echo ================================================================
echo.

REM Start the Flask application
python app.py

echo.
echo ================================================================
echo                   APPLICATION STOPPED
echo ================================================================
echo.
pause