# Information
SearchScraper is a Python scraper which scrapes the content of Google Searches. It uses a text file which includes several words. 

## How to use it
It can be laid out like this:
   
    stuff
    milk
    github
    .etc
 
Make sure it is called *searches.txt*, since the program looks for that filename. You can change what it says by replacing the filename.

    try:
        txt = open("searches.txt", "r")
        count = int(len(open("searches.txt").readlines()))
    except FileNotFoundError:
        print('Error: The file "searches.txt" was not found. Please add the text file, follow the instructions provided, and try again.')
        time.sleep(5)
        exit()
