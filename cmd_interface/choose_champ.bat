@echo off
set /p role="Enter role (-r for random):  " %=%
choose_champ.py %role%
pause