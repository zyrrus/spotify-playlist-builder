@echo off
set SPOTIPY_CLIENT_ID=
set SPOTIPY_CLIENT_SECRET=
set SPOTIPY_REDIRECT_URI=

"%VIRTUAL_ENV%\Scripts\python.exe" "%VIRTUAL_ENV%\src\main.py" %1
