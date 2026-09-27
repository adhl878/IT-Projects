@echo off
setlocal enabledelayedexpansion

:menu
cls
echo ====================================
echo IT SUPPORT AUTOMATION SCRIPT
echo ====================================
echo.
echo 1. System Information
echo 2. Clear Temp Files
echo 3. Flush DNS Cache
echo 4. Check Network
echo 5. Exit
echo.
set /p choice="Enter choice (1-5): "

if "%choice%"=="1" goto system_info
if "%choice%"=="2" goto clear_temp
if "%choice%"=="3" goto flush_dns
if "%choice%"=="4" goto network_check
if "%choice%"=="5" goto end

:system_info
cls
systeminfo
pause
goto menu

:clear_temp
cls
echo Clearing temp files...
del /q /f /s "%temp%\*.*" 2>nul
echo Done!
pause
goto menu

:flush_dns
cls
ipconfig /flushdns
echo DNS flushed!
pause
goto menu

:network_check
cls
ipconfig /all
pause
goto menu

:end
echo Goodbye!
exit /b
