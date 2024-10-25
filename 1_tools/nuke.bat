@echo off
:: NUKE

:: --- PATH ---
set "MASTERCLASS_ROOT=C:/Users/aheraud/Documents/TDAcademy"
set "SCRIPT_PATH=%MASTERCLASS_ROOT%/softwares/nuke/.nuke"

set "PYTHONPATH=%SCRIPT_PATH%/python;%PYTHONPATH%"

:: --- SETTINGS ---
set "NUKE_PATH=%SCRIPT_PATH%;%NUKE_PATH%"

:: --- INIT & MENU ---
set "NUKE_INIT_PATH=%SCRIPT_PATH%;%NUKE_INIT_PATH%"
set "NUKE_MENU_PATH=%SCRIPT_PATH%;%NUKE_MENU_PATH%"

echo %NUKE_INIT_PATH%
echo %NUKE_MENU_PATH%

:: --- CALL NUKE ---
set "PATH=C:/Program Files/Nuke15.1v3;%PATH%"
start Nuke15.1.exe --nukex


:: --- EXIT ---
exit

:: --- TODOs ---
:: DONE: add custom script path
:: DONE: add overwrite init & menus paths
:: DONE: add exit
:: DONE: turn on echo_off