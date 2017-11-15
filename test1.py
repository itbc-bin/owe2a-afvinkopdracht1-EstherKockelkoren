def main():
    bestand = open("alpaca.fa") # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand

    headers, seqs = lees_inhoud(bestand) 
       
    zoekwoord = input("Geef een zoekwoord op: ")
    for element in seqs:
        if zoekwoord in element:
            if zoekwoord != "":
                print("Het is gevonden in de sequentie: ", element)
    for element in headers:
        if  zoekwoord in element:
            if zoekwoord != 0:
                print("Het is dus gevonden met:", element)
    

    print(is_dna(seqs))
    knipt(seqs)
    print(seqs)

    
    
def lees_inhoud(bestand):
    try:
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            seq += line

        sequences = seq.split(">")
        sequences.pop(0)
        #print(sequences[0])

        for index in range(len(sequences)):



            header, seq = sequences[index].split("\n",1)
            seq = seq.replace("\n" , "")
            #print(header)
            #print(seq)
            headers.append(header)
            seqs.append(seq)
    except Exception as err:
        print("Fout bij: ", err1)

    return headers, seq
             


    
def is_dna(seqs):
    try:
    
        if 'M' in seqs:
            print("Het is een eiwitsequentie.")
        else:
            print("Het is een mRNA sequentie.")
        for index in seqs:
            if index == 'A' or index == 'C' or index == 'T' or index == 'G':
                return 'True'
            else:
                index = False
                return 'False'
    except Exception as err2:
        print(err2)

def knipt(seqs):
    try:

        enzymen_file= open('enzymen.txt', 'r')

        enzymen_list = enzymen_file.readlines()


        #in lijst zetten
        enzymen2d_list = []

        for regel in enzymen_list:
            regel = regel.rstrip().replace("^", "")
            naam = regel.split(' ')[0]
            knipplek = regel.split(' ' )[1]
            templist = [naam, knipplek]
            enzymen2d_list.append(templist)

        
        enzymen_file.close()

        for i in range(len(enzymen2d_list)):
            kaas = seqs.find(enzymen2d_list[i][1])
            
        
            #Als die niet gevonden is geeft die een -1 en anders de plaats
            if kaas >= 0:
                #print bij de 0, dus bij de enzymen
                print("Er is een match met: ", enzymen2d_list[i][0], "op plaats", kaas)
    except Exception as err3:
        print(err3)
              
           
        


main()
