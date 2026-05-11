from datetime import datetime
 #datu strukstūras
class Klients:
    def __init__(self, vards, rindas_numurs):
        self.vards=vards
        self.rindas_numurs=rindas_numurs

class kabine:
    def __init__(self, id):
        self.id=id
        self.statuss="brīva"
        self.klienta_vards=""
        self.sakuma_laiks=None

#istēmas dati
rinda = []
kabines=[kabine(1), kabine(2), kabine(3)]
videjais_laiks=3
nakamais_numurs=1

def pievienot_rindai(vards):
    global nakamais_numurs
    klients=Klients(vards,nakamais_numurs)
    rinda.append(klients)
    nakamais_numurs+=1
    return klients.rindas_numurs

def aiznemt_kabini(id, vards):
    for kabine in kabines:
        if kabine.statuss=="aizņemta":
            return False
        kabine.statuss="aizņemta"
        kabine.klienta_vards=vards
        kabine.sakuma_laiks=datetime.now()
        return True
    return False

def gaidisanas_laiks():
    return len(rinda)*videjais_laiks

def nakamais_klients():
    if len(rinda)==0:
        return "Rindā nav klientu"
    return rinda [0].vards

def brivas_kabines():
    skaits=0
    for kabine in kabines:
        if kabine.statuss=="brīva":
            skaits+=1
    return skaits

def info_ekrana():
    info=(f"Brīvās kabīnes: {brivas_kabines()}\n" f"Rindā: {len(rinda)} klienti\n" f"Nākamais: {nakamais_klients()}\n" f"Gaidīšanas laiks: {gaidisanas_laiks()} min")
    return info

#Pievienojam klientus rindai
pievienot_rindai ("Līga")
pievienot_rindai("Marta")

#Aizņemam kabīni
aiznemt_kabini(2, "Līga")

#Izvadām
print(info_ekrana())