from file_downloader import FileDownloader

link = input("Directory LINK to PULL files : ")
filetype = input("Enter file Type | Leave empety to Download All: ")
log = input("Enter log file name | Leave empety to skip logging: ")

if not log.endswith(".txt"):
    log += '.txt'

f = FileDownloader(link, log)
f.download(filetype)
