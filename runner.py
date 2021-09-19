from file_downloader import FileDownloader

filetype = input("Enter file Type | Leave empety to Download All: ")
link = input("Directory LINK to PULL files : ")

f = FileDownloader(link, 'log.txt')
f.download(filetype)
