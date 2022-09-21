@echo off
echo %~dp0
pyinstaller UnKnownKnowledge.py --noconsole --icon=icon.ico --onefile
