@echo off
:: Moverse al directorio donde está este .bat
cd /d "%~dp0"

echo === Activando entorno virtual (.venv) ===
call ..\.venv\Scripts\activate.bat

echo === Ejecutando ejecucion.py ===
python ejecucion.py

pause