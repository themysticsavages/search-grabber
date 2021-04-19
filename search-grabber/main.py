# READ THIS SECTION
# Please note that this program can scrape 52 searches at a time.
# Not like you need more than that amount anyway.
# (c) 2021 TheRealMysticSavages

import os, os.path, time, requests, sys
clear = lambda: os.system('cls')

local = '\\'.join(__file__.split('\\')[0:-1]) # Removes the need to manually input the location.
# local = input('Path (make sure searches.txt is in the directory): ') # Optional code (uncomment above code)

os.chdir(local)
num = 0

# A letter count to keep track of file names... and stop the program from continuously overwriting the html file.
ch = '`'
i = ord(ch[0])

# A second letter count? Absolutely.
ch1 = '`'
i1 = ord(ch[0])

# For the progress thing later
iprog = 0

clear()

try: # Tries to find searches.txt. 
    txt = open("searches.txt", "r")
    count = int(len(open("searches.txt").readlines()))
except FileNotFoundError: # If not, REEEEEEEEEEE
    print('Error: The file "searches.txt" was not found. Please add the text file, follow the instructions provided, and try again.')
    time.sleep(5)
    exit()

try:  
    os.chdir('Files')

except FileNotFoundError: # Makes the folder instead of stopping the program.   
    print('Notice: The folder "Files" does not exist. Creating folder "Files"...')
    time.sleep(4)
    os.mkdir('Files')
    os.chdir('Files')

# If you're text file has too many words, this changes the progress bar to something less broken.
if count > 52:
    dif = count - 52
    count = count - dif

# The most important part of the program.
for x in txt:  
    req = requests.get('https://google.com/search?q=' + x) # Adds the name of the search to that website thing
    
    i += 1
    char = chr(i)
            
    html_txt = open('index_' + char + '.html', "w+") # Makes a bunch of files
    html_txt.write(req.text) # Writes the html code of each Google Search to each file

    iprog = iprog + 1

    # Refreshes the console without stdout and stuff.
    clear()
    print ("\033[A                             \033[A")
    print(str(iprog) + '/' + str(count) + ' scraped.')

    # The same thing but it writes html files with a 1 at the end of the filename to avoid overwrite issues.
    if char == 'z':
        for x in txt:
            req2 = requests.get('https://google.com/search?q=' + x)

            i1 += 1
            char1 = chr(i1)

            html1_txt = open('index_' + char1 + '1.html', "w+")
            html1_txt.write(req2.text)

            iprog = iprog + 1

            print ("\033[A                             \033[A")
            print(str(iprog) + '/' + str(count) + ' scraped.')

            if char1 == 'z':
                time.sleep(1)
                clear()
                
                print('Scraping has finished.')

                time.sleep(3)
                exit()
