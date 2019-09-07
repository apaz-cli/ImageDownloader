import os.path, random, shutil, sys, subprocess, pip, errno, getpass


def get_downloads_folder_path():
    if sys.platform.startswith('win'):
        return "C:" +  os.sep + "Users" +  os.sep + getpass.getuser()  +  os.sep + "Downloads"
    else:
        return os.path.expanduser('~/Downloads')

# Default arguments
target_folder_path = get_downloads_folder_path() + os.sep + "ImageDownloader Downloads"
URLs_path = get_downloads_folder_path() + os.sep + 'URLs.txt'

print(target_folder_path)
print(URLs_path)
print(os.sep)

# Overwrite arguments, use defaults, or display help and exit.
argnum = len(sys.argv)
if argnum > 3:
    print("Expecting arguments in the form \"DownloadURLs url_file_path download_folder_path\".")
    print("If you leave the arguments blank, they should default to \"URLs.txt\" in your OS's default Downloads folder and the default Downloads folder respectively.")
    print("If the name of a folder contains a space, you may have to escape that space with \\.")
    sys.exit()
if argnum > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("This is a simple script which downloads all the URLs in a file.")
        print("Usage: \"DownloadURLs url_file_path download_folder_path\"")
        print("If the name of a folder contains a space in it, you may have to escape that space with \\.")
        sys.exit()
    # Use default arguments or command line arguments, if they're not just using the help command.
    else:
        URLs_path = sys.argv[1]
if argnum == 3:    
    target_folder_path = sys.argv[2]

# If they used the default target folder, create if not exists
if target_folder_path == get_downloads_folder_path() + os.sep + "ImageDownloader Downloads":
    # It's convention that you shouldn't look before you leap. Try to make the path, then handle the raised exception resulting if it already exists.
    try:
        os.mkdir(target_folder_path)
    except OSError as e:
        if e == errno.EEXIST:
            # Ignore exception if already exists
            pass
        elif not os.path.exists(get_downloads_folder_path()):
            print("Cannot find your default downloads folder path.")
        


# Fetch/verify dependencies.
print("Verifying requests module installation.")
subprocess.call([sys.executable, "-m", "pip", "install", "--user", "requests"])
import requests



# Load file into list
links = []
try:
    with open(URLs_path, 'r') as filehandle:
        for line in filehandle:
            links.append(line)    
except IOError as e:
    print('error', str(e))
    pass    
if not links:
    print("Please provide a valid file path to a nonempty file.")
    sys.exit()

# Download into the path specified with the name specified, without checking for collisions.
def download_file(url, folder_path, file_name): 
    response = requests.get(url, stream=True)
    with open(folder_path + os.sep + file_name, 'wb+') as out_file:
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

    print("Fetching " + link)

    filename = os.path.basename(link)
    # Resolve collisions
    while os.path.exists(filename):
            filename += random.randint(0, 9)
    
    download_file(link, target_folder_path, filename)
