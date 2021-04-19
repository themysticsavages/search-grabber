@echo off

py main.py
echo Opening all the html files in a new tab...
pause

cd Files
for %%a in (*.html) do (
	start chrome file://%CD%\%%a
)
