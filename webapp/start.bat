@echo off
rem Google prep planner: pulls, serves on http://127.0.0.1:8766, pushes after saves.
cd /d "%~dp0.."
python webapp\server.py
pause
