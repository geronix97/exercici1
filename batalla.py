import random
class vaixell:
    posicio1=[]
    posicio2=[]
    posicio3=[]
    posicio4=[]
    tamany=0
    tipus=""
    vida=True
    
    def enfonsat(self):
        if self.tamany==0:
            vida==False
            return self.tipus+"enfonsat!"
        
class Taulell:
    a = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    llistavaixells=[]
    bingo=False
    def setTaulell(self):
        self.a = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    def hiCap(self,objecte,posicio,x,y):
        if posicio==0:
            if objecte.tamany==1:
                if self.a[x][y] == 0:
                    self.a[x][y]=1
                    objecte.posicio1.append(x)
                    objecte.posicio1.append(y)
                    return objecte
                else:
                    return False
                    
            elif objecte.tamany==2:
                 try:
                     if self.a[x][y]==0 and self.a[x+1][y]==0:
                         objecte.posicio1.append(x)
                         objecte.posicio1.append(y)
                         objecte.posicio2.append(x+1)
                         objecte.posicio2.append(y)
                         self.a[x][y]=1
                         self.a[x+1][y]=1
                         return objecte
                     else:
                         return False
                 except:
                     return False
            elif objecte.tamany ==3:
                 try:
                     if self.a[x][y]==0 and self.a[x+1][y]==0 and self.a[x+2][y]==0:
                         objecte.posicio1.append(x)
                         objecte.posicio1.append(y)
                         objecte.posicio2.append(x+1)
                         objecte.posicio2.append(y)
                         objecte.posicio3.append(x+2)
                         objecte.posicio3.append(y)
                         self.a[x][y]=1
                         self.a[x+1][y]=1
                         self.a[x+2][y]=1
                         return objecte
                     else:
                         return False
                 except:
                     return False
            elif objecte.tamany ==4:
                 try:
                     if self.a[x][y]==0 and self.a[x+1][y]==0 and self.a[x+2][y]==0 and self.a[x+3][y]==0:
                         objecte.posicio1.append(x)
                         objecte.posicio1.append(y)
                         objecte.posicio2.append(x+1)
                         objecte.posicio2.append(y)
                         objecte.posicio3.append(x+2)
                         objecte.posicio3.append(y)
                         objecte.posicio4.append(x+3)
                         objecte.posicio4.append(y)
                         self.a[x][y]=1
                         self.a[x+1][y]=1
                         self.a[x+2][y]=1
                         self.a[x+3][y]=1
                         return objecte
                
                     else:
                         return False
                 except:
                     return False   
        elif posicio==1:
            if objecte.tamany==1:
                if self.a[x][y] == 0:
                    objecte.posicio1.append(x)
                    objecte.posicio1.append(y)
                    self.a[x][y]=1
                    return objecte
                else:
                    return False
                    
            elif objecte.tamany==2:
                 try:
                     if self.a[x][y]==0 and self.a[x][y+1]==0:
                         objecte.posicio1.append(x)
                         objecte.posicio1.append(y)
                         objecte.posicio2.append(x)
                         objecte.posicio2.append(y+1)
                         self.a[x][y]=1
                         self.a[x][y+1]=1
                         return objecte
                         
                     else:
                         return False
                 except:
                     return False
            elif objecte.tamany ==3:
                 try:
                     if self.a[x][y]==0 and self.a[x][y+1]==0 and self.a[x][y+2]==0:
                         objecte.posicio1.append(x)
                         objecte.posicio1.append(y)
                         objecte.posicio2.append(x)
                         objecte.posicio2.append(y+1)
                         objecte.posicio3.append(x)
                         objecte.posicio3.append(y+2)
                         self.a[x][y]=1
                         self.a[x][y+1]=1
                         self.a[x][y+2]=1
                         return objecte
                         
                     else:
                         return False
                 except:
                     return False
            elif objecte.tamany ==4:
                 try:
                     if self.a[x][y]==0 and self.a[x][y+1]==0 and self.a[x][y+2]==0 and self.a[x][y+3]==0:
                         objecte.posicio1.append(x)
                         objecte.posicio1.append(y)
                         objecte.posicio2.append(x)
                         objecte.posicio2.append(y+1)
                         objecte.posicio3.append(x)
                         objecte.posicio3.append(y+2)
                         objecte.posicio4.append(x)
                         objecte.posicio4.append(y+3)
                         self.a[x][y]=1
                         self.a[x][y+1]=1
                         self.a[x][y+2]=1
                         self.a[x][y+3]=1
                         return objecte
                     else:
                         return False
                 except:
                     return False
        
    def crearvaixells(self):
       for i in range(4):
            v=vaixell()
            v.tamany=1
            v.tipus="patrulla"
            self.llistavaixells.append(v)
       for i in range(3):
            v=vaixell()
            v.tamany=2
            v.tipus="fragata"
            self.llistavaixells.append(v)
       for i in range(2):
            v=vaixell()
            v.tamany=3
            v.tipus="cuirasats"
            self.llistavaixells.append(v)
            
       for i in range(1):
            v=vaixell()
            v.tamany=4
            v.tipus="portaAvions"
            self.llistavaixells.append(v)
            
    def posicionar(self):
        self.crearvaixells()
        for i in self.llistavaixells:            
            i.posicio1=[]
            i.posicio2=[]
            i.posicio3=[]
            i.posicio4=[]
            x=random.randint(0,9)
            y=random.randint(0,9)
            posicio= random.randint(0,1)
            while self.hiCap(i,posicio,x,y)== False:
                x=random.randint(0,9)
                y=random.randint(0,9)
                posicio= random.randint(0,1)

            
#            self.printar()
        
#    def introduir(self,num1,num2,lletra):
#          self.a[num1][num2]=lletra
    def hit(self,x,y):
        posicio=[]
        self.a[x][y]=2
        for i in self.llistavaixells:
            #print("posicio1")      
            try:    
                if i.posicio1[0]== x and i.posicio1[1]==y:
                    i.tamany-=1
                    
                    if i.tamany==0:
                        print("-----------------------")
                        print("| "+i.tipus+" enfonsat!"+" |")
                        print("-----------------------")
                        self.llistavaixells.remove(i)
                        
                    else:
                        print("-------------------------------")
                        print("| li has donat a un "+i.tipus+" |")
                        print("-------------------------------")
                   
                elif i.posicio2[0]== x and i.posicio2[1]==y:
                    i.tamany-=1
                    if i.tamany==0:
                        print("---------------------------------")
                        print("| "+i.tipus+" enfonsat!"+" |")
                        print("---------------------------------")
                        self.llistavaixells.remove(i) 
                    else:
                        print("-------------------------------")
                        print("| li has donat a un "+i.tipus+" |")
                        print("-------------------------------")
                   
                elif i.posicio3[0]== x and i.posicio3[1]==y:
                    i.tamany-=1
                    if i.tamany==0:
                        print("-----------------------")
                        print("| "+i.tipus+" enfonsat!"+" |")
                        print("-----------------------")
                        self.llistavaixells.remove(i)
                        
                    else:
                        print("-------------------------------")
                        print("| li has donat a un "+i.tipus+" |")
                        print("-------------------------------")

                elif i.posicio4[0]== x and i.posicio4[1]==y:
                    i.tamany-=1
                    self.a[x][y]=2
                    if i.tamany==0:
                        print("-----------------------")
                        print("| "+i.tipus+" enfonsat!"+" |")
                        print("-----------------------")
                        self.llistavaixells.remove(i)
                        
                    else:
                        print("-------------------------------")
                        print("| li has donat a un "+i.tipus+" |")
                        print("-------------------------------")
                
             
            
            except:
                posicio=[]
                
            #print(i.tipus)
            #print(i.tamany)
                
            #print("--")
            #print("next")
    def hitcpu(self,x,y):
        posicio=[]
        self.a[x][y]=2
        for i in self.llistavaixells:
            #print("posicio1")      
            try:    
                if i.posicio1[0]== x and i.posicio1[1]==y:
                    i.tamany-=1
                    
                    if i.tamany==0:
                        print("-----------------------")
                        print("| "+i.tipus+" enfonsat per l' enemic!"+" |")
                        print("-----------------------")
                        self.llistavaixells.remove(i)
                        
                    else:
                        print("-------------------------------")
                        print("| T' han donat a un "+i.tipus+" |")
                        print("-------------------------------")
                   
                elif i.posicio2[0]== x and i.posicio2[1]==y:
                    i.tamany-=1
                    if i.tamany==0:
                        print("---------------------------------")
                        print("| "+i.tipus+" enfonsat per l' enemic!"+" |")
                        print("---------------------------------")
                        self.llistavaixells.remove(i) 
                    else:
                        print("-------------------------------")
                        print("| T' han donat a un "+i.tipus+" |")
                        print("-------------------------------")
                   
                elif i.posicio3[0]== x and i.posicio3[1]==y:
                    i.tamany-=1
                    if i.tamany==0:
                        print("-----------------------")
                        print("| "+i.tipus+" enfonsat per l' enemic!"+" |")
                        print("-----------------------")
                        self.llistavaixells.remove(i)
                        
                    else:
                        print("-------------------------------")
                        print("| T' han donat a un "+i.tipus+" |")
                        print("-------------------------------")

                elif i.posicio4[0]== x and i.posicio4[1]==y:
                    i.tamany-=1
                    self.a[x][y]=2
                    if i.tamany==0:
                        print("-----------------------")
                        print("| "+i.tipus+" enfonsatper l' enemic!"+" |")
                        print("-----------------------")
                        self.llistavaixells.remove(i)
                        
                    else:
                        print("-------------------------------")
                        print("| T' han donat a un "+i.tipus+" |")
                        print("-------------------------------")
                
             
            
            except:
                posicio=[]
                
            #print(i.tipus)
            #print(i.tamany)
                
            #print("--")
            #print("next")
                
    def moure(self):
        moviment=[]
        x=random.randint(0,9)
        y=random.randint(0,9)
        moviment.append(x)
        moviment.append(y)
        return moviment
        
    def gameover(self):
        if len(self.llistavaixells)==0:
            return True
        else:
            return False
    def printar(self):
        llista =""
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
               if self.a[i][j]==2:
                   llista+="X "
               else: 
                   llista+=str(self.a[i][j])+" "
            print(llista)
            llista=""
            
    def printarAmagat(self):
        llista =""
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if self.a[i][j]==2:
                   llista+="X "
                else:
                    llista+="* "
            print(llista)
            llista=""        

class Joc():
    
    final= False
    def final():
        if final== False:
            print("hola")
        
    def menu(self):
        while True:
            print("Benvingut a hundir la flota")
            
            print("Selecciona una opció")

            print("\t1 - Introdueix vaixells automaticament.")
            
            
            opcionMenu = input("")
           
            if opcionMenu=="1":
                taulellJugador= Taulell()
                taulellCpu= Taulell()
                taulellCpu.llistavaixells=[]
                taulellJugador.llistavaixells=[]
                taulellCpu.setTaulell()
                taulellJugador.setTaulell()
                taulellCpu.posicionar()
                taulellJugador.posicionar()
                while True:
                    print("el teu taulell")
                    taulellJugador.printar()
                    print("Taulell Enemic")
                    taulellCpu.printarAmagat()
                    fila=0
                    columna=0
                    while True:
                        fila = input("numero de fila: ")
                        columna = input("numero de columna: ")
                        if int(fila)<=10 and int(fila) >=0 or int(columna) <=10 and int(columna) >=0:
                            break
                        
                        print("no has introduit be les dades")            
                    taulellCpu.hit(int(fila)-1,int(columna)-1)
                    moviment=taulellCpu.moure()
                    taulellJugador.hitcpu(moviment[0],moviment[1])
                    if taulellJugador.gameover()== True:
                        print("La maquina ha guanyat... un altre cop")
                        break
                    elif taulellCpu.gameover()== True:    
                        print("Has guanyat!")
                        break
            else:
                print("opcio incorrecte")
#taulell.printar()
# taulellJugador= Taulell()
# taulellJugador.posicionar()

partida= Joc()
partida.menu()