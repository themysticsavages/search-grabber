@echo off

python main.py
echo Opening all the html files in a new tab...
pause

cd Files
for %%a in (*.html) do (
	start chrome file://%CD%\%%a
)
