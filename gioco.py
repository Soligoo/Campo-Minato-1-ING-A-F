import random
#indicatori per il colore dei numeri
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

#questa funzione da i colori ai numeri
def colore_num(n_bomb):
    global c
    c=""
    if n_bomb == 1:
        c=BLUE+str(n_bomb)+RESET
    if n_bomb == 2:
        c=GREEN+str(n_bomb)+RESET
    if n_bomb == 3:
        c=RED+str(n_bomb)+RESET
    if n_bomb == 4:
        c=MAGENTA+str(n_bomb)+RESET
    if n_bomb == 5:
        c=YELLOW+str(n_bomb)+RESET
    if n_bomb == 6:
        c=CYAN+str(n_bomb)+RESET
    if n_bomb == 7:
        c=WHITE+str(n_bomb)+RESET
    if n_bomb == 8:
        c=BLACK+str(n_bomb)+RESET
    return c 

# ottiene dall'user dei parametri con cui creare la scacchiera di gioco;
# l=larghezza
# h=altezza
# n=numero di bombe

def myinput():
    global l,h,n3
    l = int(input("inserisci la larghezza "))
    h = int(input("inserisci l'altezza "))
    n3 = int(input("inserisci il numero di bombe "))
    

# r1 è una lista bidimensionale quindi si possono inserire nella forma r1[a][b]:
# a la posizione della lista scelta (riga)
# b la posizione dell'oggetto della lista a (colonna) 
def informazioni(l,h,n3):
    global r1,r2,cordinate,cordinate_random
    r1=[["[ ]" for i in range(l)] for j in range(h)]
    r2 = [["[■]" for i in range(l)]for j in range(h)]

# cordinate è una lista di tutte le coordinate di r1 es: (0,0),...,(l-1,h-1)
    cordinate=[(x,y) for x in range(l) for y in range(h)]
    
# .shuffle viene usato per riordinare in modo randomico le coordinate in modo da poter dare una posizione casuale in seguito alle bombe
    cordinate_random=cordinate.copy()
    random.shuffle(cordinate_random)
    return l,h,n3

def ins_bomb(n3):
# nella seguente funzione si utilizzano i dati forniti prima per modificare la scacchiera e aggiungere le bombe nelle coordinate casuali
# ottenute in precedenza
    for j in range(n3):
        posA, posB=cordinate_random[j]
        r1[posB][posA]=RED +"[x]"+RESET


#questa funzione utilizza le cordinate ottenute in precedenza e cerca nelle 8 posizioni intorno ad essa la presenza
#di bombe, nel caso viene trovata una bomba si aggiunge +1 a n_bomb che è il numero totale di bombe nelle 8 posizioni,
#finita la ricerca la casella avra all'interno il numero di bombe intorno ad essa 
def pos_num():
    cord2=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    
    for x,y in cordinate:
        
        n_bomb=0
        if r1[y][x] != RED+ "[x]"+ RESET:
            for x2,y2 in cord2:
                
                nx = x+x2
                ny = y+y2
                if 0<=nx<l and 0<=ny<h:
                    if r1[ny][nx] == RED +"[x]"+RESET:
                        n_bomb +=1
                        print(x,y, "TROVATA! in:", nx,ny)
            colore_num(n_bomb)
                        
            if n_bomb!=0:
                r1[y][x] = ("["+c+"]")

#questa funzione stampa due scacchiere, una di debug(r1) e l'altra di gioco(r2), quando poi si vuole veramente giocare si usa
#la scacchiera r2
def stampa_griglie(r1, r2):
    print("Griglia nascosta (con bombe):")
    for row in r1:
        print(" ".join(row))
    
    print("\nGriglia visibile all'utente:")
    for row in r2:
        print(" ".join(row))

# questa funzione va ad aprire tutte le caselle "libere" se la casella scelta è una casella vuota
def libere(yin,xin):
    cord2=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    if r1[yin][xin] == "[ ]":
        for x2,y2 in cord2:
            nx= xin+x2
            ny=yin+y2
            if 0<=nx<l and 0<=ny<h and r1[ny][nx] != RED +"[x]"+RESET:
                r2[ny][nx] = r1[ny][nx]

#main loop di gioco
#l'utente da questo momento in poi deve dare in input le cordinate della casella che vuole "scoperchiare" o su quale
#vuole mettere una bandiera, se sbaglia e scoperchia una bomba il gioco viene perso, l'utente puoi puo scegliere se 
#giocare ancora o meno
v1=True
v2=True
while v1:

    myinput()
    informazioni(l,h,n3)
    ins_bomb(n3)
    pos_num()
    v2 = True
    while v2:
        if all("[■]" not in row for row in r2):
        
            stampa_griglie(r1,r2)
            print("HAI VINTO")
            game=input("vuoi fare un altra partita? y/n")
            print(game)
            
            if game.lower() != "y":
                v1=False
                
                break

        stampa_griglie(r1,r2)
        xin=int(input("inserisci la cordinata x "))
        yin=int(input("inserisci la cordinata y "))
        sob= input("inserisci 's' per scoperchiare 'b' per inserire una bandiera ")
        if sob == "s":
            if r1[yin][xin] == RED +"[x]"+RESET:
                print("HAI PERSO!!")
                for row in r1:
                    print(row)
                game=input("vuoi fare un altra partita? ")
                print(game)

                if game.lower() != "si":
                    v1=False

                    break
            else:
                r2[yin][xin] = r1[yin][xin]
                libere(yin,xin)
        else:
            r2[yin][xin] = "🚩"
            





    






