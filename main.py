from datetime import datetime
import requests as req

horaDescarga = [16, 44, 0]

def ObtenerHora():
    hora = str(datetime.now().strftime("%H"))
    minuto = str(datetime.now().strftime("%M"))
    segundo = str(datetime.now().strftime("%S"))

    
    return [int(hora), int(minuto), int(segundo)]

def DescargarArchivo(URL):
    file = req.get(URL, allow_redirects=False)
    return file

while 2 > 1:

    if ObtenerHora() == horaDescarga:
        cheapestsFile = open(DescargarArchivo("https://api.preciodelaluz.org/v1/prices/cheapests?zone=PCB&n=2"), "r")
        
        cheapestsFile.close()
