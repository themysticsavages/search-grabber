# Information
SearchScraper is a Python scraper which scrapes the content of Google Searches. It uses a text file which includes several words.

## How to use it
The program requires Python. You won't need any additional modules to run it. The program itself is entirely automated requiring no input at all. However, the program reads off a search file. You can follow the layout of the txt file included. The filename the program reads off by default is called *searches.txt*. You can change it, if you want by replacing the word *searches* with whatever you want (as long as the OS is ok with it):

    try:
        txt = open("searches.txt", "r")
        count = int(len(open("searches.txt").readlines()))
    except FileNotFoundError:
        print('Error: The file "searches.txt" was not found. Please add the text file, follow the instructions provided, and try again.')
        time.sleep(5)
        exit()
        
 After running the program, a 'Files' directory will be created containing the HTML content of every search from the text file. The content may not look entirely correct because the program, as of now, does not download all the assets. So webpages will look incomplete... but, you still get the website, I guess 😬
 
## Demonstation
![](/assets/txt.jpg)
