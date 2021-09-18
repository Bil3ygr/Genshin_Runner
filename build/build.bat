@echo off

set PYINSTALLER=C:\Python36\Scripts\pyinstaller.exe

pushd %~dp0\..
%PYINSTALLER% --distpath bin --workpath temp --clean -F -n "Genshin Runner" -c -i "res/Genshin Runner.ico" src/main.py
popd
