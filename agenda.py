import datetime
import time

class Client:
    nom = ""
    cognoms=""
    data_de_naixement=""
    telefon=""
    def esdata(data):
      try:
        datetime.datetime.strptime(data_de_naixement, '%Y-%m-%d')
        return true
      except:
        print("mal format de data (m/dd/yyyy)")
        return false
    
    def setnom(self,nom):
        if str(nom): 
            self.nom=nom
        else:
           print("nom en mal format") 
         
    def setcognoms(self,cognoms):
        if str(cognoms): 
            self.cognoms=cognoms
        else:
           print("cognom en mal format") 
         
    def setdata_de_naixement(self,data_de_naixement):
        
            try:
               validate_date=time.strptime(data_de_naixement,"%d/%m%Y")
               self.data_de_naixement= data_de_naixement
            except:
                print("mal format data")
    def settelefon(self,telefon):
        if int(telefon):
            telefon=str(telefon)
            if len(telefon)==9:
                self.telefon=telefon
            else:
               print("telefon s' ha escrit en mal format.") 

    def imprimeixnom(self):
        print(self.nom)
        
    def imprimeixcognoms(self):
        print(self.cognoms)
        
    def imprimeixdata_de_naixement(self):
        print(self.data_de_naixement)
        
    def imprimeixtelefon(self):
        print(self.telefon)
    def getnom(self):
        return self.nom
    def getcognoms(self):
        return self.cognoms
    def getdata_de_naixement(self):
        return self.data_de_naixement
    def gettelefon(self):
        return self.telefon
        

    print("Selecciona una opció")

    print("\t1 - Introdueix dades a l'agenda triadaaaa.")

    print("\t2 - Importa agenda de l'arxiu desitjat.")

    print("\t3 - Mostra dades de l'agenda actual.")

    print("\t4 - Exporta l'agenda actual a l'arxiu desitjat.")
    
    print("\t5 - salirr")
    
llistaClients=[]
while True: 
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=="1":
        client = Client()
        print("Introdueix nom")
        nom = input()
        client.setnom(nom)
        cognoms= input("inserta cognoms")
        client.setcognoms(cognoms)
        print("Introdueix data de naixement")
        data_naixement= input("inserta data naixement (m/dd/yyyy)")
        
        client.setdata_de_naixement(data_naixement)
        print("Introdueix telefon")
        telefon = input("inserta telefon")
        client.settelefon(telefon)
        llistaClients.append(client)
        
    elif opcionMenu=="2":
        
        nomAgenda=input("Introdueix el nom de l' agenda amb extenció .txt: ")
       
        try:
            f = open(nomAgenda, "r")
            del llistaClients[:]
            for linea in f.readlines():
                linea = linea.split(":")
                client=Client()
                client.setnom(linea[0])
                client.setcognoms(linea[1])
                client.setdata_de_naixement(linea[2])
                linea[3]=int(linea[3])
                client.settelefon(linea[3]) 
                llistaClients.append(client)            
        except:
            print("El ficher no existeix")
            
        f.close()
    elif opcionMenu=="3":

        for x in llistaClients:
            x.imprimeixnom()
            x.imprimeixcognoms()
            x.imprimeixdata_de_naixement()
            x.imprimeixtelefon()
            print("---------------------")

    elif opcionMenu=="4":
        nom=input("introdueix nom d' arxiu acabat en .txt")
        f = open (nom,'w+')
        for x in llistaClients:
            f.write(x.getnom())
            f.write(":")
            f.write(x.getcognoms())
            f.write(":")
            f.write(x.getdata_de_naixement())
            f.write(":")
            f.write(x.gettelefon())
            f.write("\n")
            
            
        f.close()     
    elif opcionMenu=="5":
        break
    else:

        print ("")

        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
        
            
