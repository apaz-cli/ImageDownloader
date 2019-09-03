# ImageDownloader
A simple python script that downloads all the URLs in a text file into a folder.

# Usage Examples:
 
**Linux example:**
```
mkdir ~/Downloads/DownloadedURLs

python ~/Downloads/ImageDownloader-master/DownloadImages.py ~/Downloads/URLs.txt ~/Downloads/DownloadedURLs
```
**Windows example:**
```
mkdir C:\Users\%username%\Downloads\DownloadedURLs

C:\python27\python.exe C:\Users\%username%\Downloads\ImageDownloader-master\DownloadImages.py C:\Users\%username%\Downloads\URLs.txt C:\Users\%username%\Downloads\DownloadedURLs
```



The URLs in the source file should be separated with a newline character.

If you leave the arguments blank, they should default to "URLs.txt" and your default Downloads folder (Should work on at least Windows and most all Linux distros, Mac is untested) respectively. But, if your file is not in fact named URLs.txt, and

If the name of a folder contains a space in it, you may have to escape that space with \\.
