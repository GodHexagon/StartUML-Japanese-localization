@echo off
REM StarUML Japanese localization installer
REM This script must be run with administrator privileges

echo ============================================
echo StarUML Japanese Localization Installer
echo ============================================
echo.

REM Backup original app.asar
if not exist "C:\Program Files\StarUML\resources\app.asar.backup" (
    echo Backing up original app.asar...
    copy "C:\Program Files\StarUML\resources\app.asar" "C:\Program Files\StarUML\resources\app.asar.backup"
    if errorlevel 1 (
        echo ERROR: Failed to create backup. Please run as administrator.
        pause
        exit /b 1
    )
    echo Backup created: app.asar.backup
) else (
    echo Backup already exists. Skipping...
)

echo.
echo Copying Japanese localized app.asar...
copy /Y "%~dp0app-japanese.asar" "C:\Program Files\StarUML\resources\app.asar"
if errorlevel 1 (
    echo ERROR: Failed to copy file. Please run as administrator.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Installation completed successfully!
echo Please restart StarUML to see Japanese UI.
echo ============================================
echo.
echo To revert to English, run:
echo copy "C:\Program Files\StarUML\resources\app.asar.backup" "C:\Program Files\StarUML\resources\app.asar"
echo.
pause
