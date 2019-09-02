import os.path, mimetypes, urllib.request, wget, random, shutil, requests, sys, getpass
from urllib.parse import urlparse


# Default arguments
links_path = "URLs.txt"
download_folder_path = os.path.expanduser('~/Downloads')

argnum = len(sys.argv)
if argnum > 3:
    print("Expecting arguments in the form \"DownloadURLs url_file_path downoad_folder_path\".")
    print("If you leave the arguments blank, they should default to \"URLs.txt\" and your default Downloads folder respectively.")
    print("If the name of a folder contains a space in it, you may have to escape that space with \\.")
    exit
if argnum > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("This is a simple script which downloads all the URLs in a file.")
        print("Usage: \"DownloadURLs url_file_path downoad_folder_path\"")
        print("If the name of a folder contains a space in it, you may have to escape that space with \\.")


if argnum > 1:
    links_path = sys.argv[1]
if argnum == 3:    
    download_folder_path = sys.argv[2]

# Load file into list
links = []
try:
    with open(links_path, 'r') as filehandle:
        for line in filehandle:
            links.append(line)    
except:
    pass
if not links:
    print("Please provide a valid file path to a nonempty file.")
    exit

# Download into the path specified with the name specified, without checking for collisions.
def download_file(url, folder_path, file_name): 
    response = requests.get(url, stream=True)
    with open(folder_path + os.sep + file_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

# Download all links, checking for collisions.
for link in links:
    # Deal with potential Windows line terminator issues
    link = link.strip()

    # Ignore blank lines
    if link == "":
        continue

    # Remove any queries 
    query = link.rfind('?')
    if query > 0:
        link = link[0, query]

    filename = os.path.basename(link)
    # resolve collisions
    while os.path.exists(filename):
            filename += random.randint(0, 9)
    
    download_file(link, download_folder_path, filename)
