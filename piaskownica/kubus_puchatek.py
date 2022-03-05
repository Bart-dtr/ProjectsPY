import requests 
link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text #.encode('utf-8')) 
kubus_linie_b = kubus_text.split('</p>')
# Czyszczenie.
kubus_linie = []
for l in kubus_linie_b:
    l = l.strip()
    kubus_linie.append(l)
# Czyszczenie: alternatywa
#kubus_linie = [l.strip()for l kubus_text.split('</p>')]
start = 1000 
end = 1100
tajemniczy_bohater = 'Venom'
bohater_2 = 'dot MS' 
bohater_3 = 'Bartek'
for index, linia in enumerate( kubus_linie):
    if index >= start and index < end:
        linia = linia.replace('Kubuś', tajemniczy_bohater)
        linia = linia.replace('Puchatek', tajemniczy_bohater)
        linia = linia.replace('Królik', bohater_2)
        linia = linia.replace('Prosiaczek', bohater_3)
        print(linia+'</p>')
# print()
# print('<p>Czytała Krystyna Czubówna</p>')
#print( len( kubus_linie ) )
