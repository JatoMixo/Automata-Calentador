from datetime import datetime
import requests as req
import os
import json

downloadTime = [12, 6, 0]
filePath = "D:/Miguel/Programas/Automata-Calentador/Code/Downloads/cheapests.json"

def GetTime():
    _hour = str(datetime.now().strftime("%H"))
    _minute = str(datetime.now().strftime("%M"))
    _second = str(datetime.now().strftime("%S"))

    
    return [int(_hour), int(_minute), int(_second)]

def DownloadFile(_URL, _filePath):
    if not(os.path.isfile(_filePath)):

        _remoteFile = req.get(_URL, allow_redirects=True)
        _localFile = open(_filePath, "w")

        _localFile.write(str(_remoteFile.content))

        _localFile.close()
    else:
        os.remove(_filePath)
        DownloadFile(_URL, _filePath)

def DeleteFile(_filePath):
    if os.path.isfile(_filePath):
        os.remove(_filePath)
    else:
        print("File doesn't exist")

def ReadFile(_filePath):
    hours = []


DownloadFile("https://api.preciodelaluz.org/v1/prices/cheapests?zone=PCB&n=3", filePath)

print(ReadFile(filePath))

DeleteFile(filePath)

while 2 > 1:

    if GetTime() == downloadTime:
        DownloadFile("https://api.preciodelaluz.org/v1/prices/cheapests?zone=PCB&n=3", filePath)

        DeleteFile(filePath)
        
