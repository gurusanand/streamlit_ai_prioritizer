@echo off
echo ========================================
echo Agentic AI Prioritization Framework
echo ========================================
echo.

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Python found: 
python --version
echo.

REM Check if requirements are installed
echo Checking dependencies...
python -c "import streamlit" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Installing required packages...
    echo This may take a few minutes...
    pip install -r requirements.txt
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo Starting the application...
echo ========================================
echo.
echo The app will open in your browser automatically.
echo If not, navigate to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start Streamlit
streamlit run app.py

pause

