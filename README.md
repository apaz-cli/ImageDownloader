# ImageDownloader
A simple python script that downloads all the URLs in a text file into a folder.

# Usage Examples:
 
**Linux example:**
```
# Make a folder to put the images into
mkdir ~/Downloads/DownloadedURLs

# Download all the URLs from the text file specified into the folder specified
# If you don't specify a text file, the script will look in your downloads folder for a file named URLs.txt
# If you dont' specify a folder to download into, it will create a new one at ~/Downloads/ImageDownloader Downloads
python ~/Downloads/ImageDownloader-master/DownloadImages.py ~/Downloads/URLs.txt ~/Downloads/DownloadedURLs
```
**Windows example:**
On Windows, the concept is exactly the same, but a bit more complicated. Windows stands out as the only modern operating system which does not actually come with a Python interpreter. Install one, then for the first argument of running the script, use the path to the python executable. The easiest way to do so is through the Windows 10 app store. If you do it that way, you can use just the `python` command, instead of a path to the python executable.
```
REM Make sure that the folder exists.
mkdir C:\Users\%username%\Downloads\DownloadedURLs

REM The path to the python executable that you're using, or python for windows 10 app store version.
REM Additionally, the default Windows .zip extractor creates an additional intermediate folder, whereas most others do not.
C:\python27\python.exe C:\Users\PazderaAaron\Downloads\ImageDownloader-master\ImageDownloader-master\DownloadImages.py C:\Users\%username%\Downloads\URLs.txt C:\Users\%username%\Downloads\DownloadedURLs
```



The URLs in the source file should be separated with a newline character.

If the name of a file or folder contains a space in it, you may have to escape that space with \\.
