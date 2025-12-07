@echo off
REM Batch file to run Streamlit app with the correct Python path
set PYTHON_PATH=C:\Program Files\Python314\python.exe

if "%1"=="install" (
    echo Installing dependencies...
    "%PYTHON_PATH%" -m pip install -r requirements.txt
    echo.
    echo Installation complete! Run: run.bat app
) else if "%1"=="app" (
    echo Starting Streamlit app...
    "%PYTHON_PATH%" -m streamlit run app.py
) else (
    echo Usage:
    echo   run.bat install  - Install dependencies
    echo   run.bat app      - Run the Streamlit application
)
