from click import argument
import requests
import sys, os

orangutan = 'https://zajecia-programowania-xd.pl/flagi'

def pobierz_tekst_ze_strony_www(orangutan):

    surowe_info = requests.get( orangutan)
    text = surowe_info.text
    return text



def stworz_liste_flag():

    tekst_strony_www = pobierz_tekst_ze_strony_www( orangutan)

    # Przygotowanie listy linków ze strony :)
    lista_linii = tekst_strony_www.split('</p>')
    
    linki = []
    for linia in lista_linii:

        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append( link)
    
    return linki

linki = stworz_liste_flag()
print(linki)

if __name__ == '__main__':
        argument = sys.argv[1]
        lista_flag = stworz_liste_flag(argument)
        print(argument)