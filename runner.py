from file_downloader import FileDownloader

link = input("Directory URL to download files : ")
filetype = input("Enter file Type | Leave empty to Download All: ")
log = input("Enter log file name | Leave empty to skip logging: ")

if not log.endswith(".txt"):
    log += '.txt'

f = FileDownloader(link, log)
f.download(filetype)
