from datetime import datetime
import requests as req
import os
import json

downloadTime = [0, 5, 0]
filePath = "D:/Miguel/Programas/Automata-Calentador/Code/Downloads/cheapests.json"
cheapestsHoursCuantity = 3
url = f"https://api.preciodelaluz.org/v1/prices/cheapests?zone=PCB&n={str(cheapestsHoursCuantity)}"


def GetTime(onlyHour):
    _hour = str(datetime.now().strftime("%H"))
    _minute = str(datetime.now().strftime("%M"))
    _second = str(datetime.now().strftime("%S"))

    if onlyHour:
        return int(_hour)
    else:
        return [int(_hour), int(_minute), int(_second)]

def DownloadFile(_URL, _filePath):
    if not(os.path.isfile(_filePath)):

        _remoteFile = req.get(_URL, allow_redirects=False)
        
        _encodedFile = json.loads(_remoteFile.content.decode())

        with open(_filePath, "w") as _localFile:
            json.dump(_encodedFile, _localFile, sort_keys=True)
    else:
        os.remove(_filePath)
        DownloadFile(_URL, _filePath)

def DeleteFile(_filePath):
    if os.path.isfile(_filePath):
        os.remove(_filePath)
    else:
        print("File doesn't exist")

def ReadFile(_filePath):
    if os.path.isfile(_filePath):
        with open(_filePath, "r") as _file:
            return json.load(_file)
    else:
        print("File not found")

def GetHours (_filePath):
    if (os.path.isfile(_filePath)):
        hours = []
        
        i = 0
        while (i < cheapestsHoursCuantity):
            hour = ReadFile(_filePath)[i]["hour"]    
            hour = hour[0] + hour[1]

            hours.append(hour)

            i += 1
        
        hours.sort()
        return hours
    else:
        DownloadFile(url, filePath)

def TurnOnRelay():
    print()

DownloadFile(url, filePath)
print(GetHours(filePath))
'''file = ReadFile(filePath)
print(file[0]["hour"])
DeleteFile(filePath)'''

'''while 2 > 1:

    if GetTime(False) == downloadTime:
        DownloadFile(url, filePath)
        
        DeleteFile(filePath)'''
        
