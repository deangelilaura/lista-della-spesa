lista_spesa = []
def aggiungi_elemento():
    elemento = input("inserisci un elemento alla lista")
    lista_spesa.append(elemento)

def visualizza_elemento():
    for i in range(len(lista_spesa)):
        print(f"{i+1}.{lista_spesa[i]}")

def rimuovi_elemento():
    visualizza_elemento()
    indice = int(input("inserisci un indice"))
    lista_spesa.pop(indice-1)

def conta_elementi():
    print(len(lista_spesa))

def svuota_lista():
    lista_spesa.clear()

while True: 
    scelta = int(input("scegli cosa fare"))
    if scelta ==1:
        aggiungi_elemento()
    elif scelta ==2:
        visualizza_elemento()
    elif scelta ==3:
     rimuovi_elemento
    elif scelta ==4:
     conta_elementi
    elif scelta ==5:
     svuota_lista
    elif scelta ==0:
       break


