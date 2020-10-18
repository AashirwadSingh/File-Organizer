import os

def createIfnotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

    
if __name__ == "__main__":
    files = os.listdir()
    files.remove("fileOrganiser.py")

    createIfnotExists('Images')
    createIfnotExists('Docs')
    createIfnotExists('Media')
    createIfnotExists('Application')
    createIfnotExists('ZipFiles')

    imgExts = [".png", ".jpg", "jpeg", ".ico"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".docx", ".doc", ".txt", ".pdf", ".xlsx", ".pptx", ".ppt"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4", ".mp3", ".wav", ".mov", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    appExts = [".lnk", ".exe"]
    apps = [file for file in files if os.path.splitext(file)[1].lower in appExts]

    zipExts = [".zip", ".rar", ".7z", ".z"]
    rar = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("ZipFiles", rar)
    move("Application", apps)

