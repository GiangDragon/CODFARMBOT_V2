@echo off

cd /d D:\CODFARMBOT_V2
start "" "D:\Call of Dragons\Call of Dragons Game\CALLOFDRAGONS.exe"

timeout /t 10
.venv\Scripts\python auto_farm.py