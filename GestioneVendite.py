class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice=codice
    self.fornitore=fornitore
    self.marca=marca
    self.prezzo=prezzo
    self.quantita=quantita    
    

  def scheda_articolo(self):
    return f"""
    codice: {self.codice}
    fornitorre: {self.fornitore}
    marca: {self.marca}
    prezzo: {self.prezzo}
    quantita: {self.quantita}"""

  def modifica_scheda(self):
    self.fornitore = input("Inserisci il nuovo fornitore: ")
    self.marca = input("Inserisci la nuova marca: ")
    self.prezzo = float(input("Inserisci il nuovo prezzo: "))
    self.quantita = int(input("Inserisci la nuova quantita: "))


class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      super().__init__(codice, fornitore, marca,prezzo, quantita) 
      self.pollici=pollici
      self.tipo=tipo

    def scheda_articolo(self):
      return(f"Codice: {self.codice}\nFornitorre: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantita: {self.quantita}\nPollici: {self.pollici}\nTipo: {self.tipo}")
       
    
class Frigorifero(Articolo):
    def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
      super().__init__(codice, fornitore, marca,prezzo, quantita)
      self.dimensioni=dimensioni
      self.modello=modello
      
    def scheda_articolo(self):
      return(f"Codice: {self.codice}\nFornitorre: {self.fornitore}\nMarca: {self.marca}\nPrezzo: {self.prezzo}\nQuantita: {self.quantita}\nDimensioni: {self.dimensioni}\nModello: {self.modello}")
      
    
t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())

t1.modifica_scheda()
print(t1.scheda_articolo())
#9.47
class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    self.codice=codice
    self.data=data
    self.piva=piva
    self.indirizzo=indirizzo
    self.listaOrdine=[]
    

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"
    else:
      print("L'articolo non è presente")
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno

  def rimuovi_articolo(self,articolo):
    if articolo in self.listaOrdine:
      if isinstance(articolo,Televisore):
        tipo_articolo="Televisore"
        self.listaOrdine.remove(articolo)
        print(f"articolo di tipo {tipo_articolo} rimosso dalla lista")

      elif isinstance(articolo,Frigorifero):
        tipo_articolo="Frigorifero"
        self.listaOrdine.remove(articolo)
        print(f"Articolo di tipo {tipo_articolo} rimosso dalla lista")
    else:
      print("Articolo non presente nella lista")
    #10 Implementa il metodo


  def importo_ordine(self):
    sommaT=0
    sommaF=0
    for articolo in self.listaOrdine:
      if isinstance(articolo,Televisore):
        sommaT+=articolo.prezzo
        print(f"\nImporto Televisori= {sommaT}")
      elif isinstance(articolo,Frigorifero):
        sommaF+=articolo.prezzo
        print(f"\nImporto Frigorifero= {sommaF}")
    print(f"\nImporto Totale= {sommaT+sommaF}")
    return(sommaT+sommaF)
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)
    

  def dettaglio_ordine(self):
    sommaT=0
    sommaF=0
    provvigione=0
    for articolo in self.listaOrdine:
      if isinstance(articolo,Televisore):
        sommaT+=articolo.prezzo
        provvigione+=articolo.prezzo*0.03
      elif isinstance(articolo,Frigorifero):
        sommaF+=articolo.prezzo
        provvigione+=articolo.prezzo*0.02
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...

    return([sommaT,sommaF,sommaT+sommaF])
  
t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')


ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)

ordine1.importo_ordine()

importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
#10:18
class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.lista_ordini=[]
    #16 Implementa il costruttore

  def aggiungi_ordine(self,ordine):
    self.lista_ordini.append(ordine)
    print("Ordine avvenuto con successo")
    #17 Implementa il metodo

  def rimuovi_ordine(self,ordine):
    if ordine in self.lista_ordini:
      self.lista_ordini.remove(ordine)
      print("Ordine rimosso con successo")
    else:
      print("Ordine non presente nella lista")

    #18 Implementa il metodo

  def totale_ordini(self):
    #19 Implementa il metodo
    #...
    totT=0
    totF=0
    tot=0
    for vendita in self.lista_ordini:
      importi=vendita.dettaglio_vendita()
      totT+=importi[0]
      totF+=importi[1]
      tot+=importi[2]
      print("--------------------------")
      print(f"\nImporto Televisori= {importi[0]}")
      print(f"\nImporto Frigoriferi= {importi[1]}")
      print(f"\nImporto totTle= {importi[2]}")
      print(f"\nImporto Provvigione= {importi[3]}")
      print("--------------------------")
      print(f"\ntotTle Televisori= {totT}")
      print(f"\nTotale Frigoriferi= {totF}")
      print(f"\nTotale Totale= {tot}")
      print("--------------------------")


    return ([self.totT,self.totF,self.tot])
  
ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")