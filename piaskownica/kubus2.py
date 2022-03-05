

import requests


link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

kubus_text = kubus_text.replace('<p>', '')
kubus_text = kubus_text.replace('</p>', '')

dlugosc_kubusia = len(kubus_text) 
print(dlugosc_kubusia)

kubus_puchatek_slowa = kubus_text.split()
kubus_puchatek_slowa_n = len(kubus_puchatek_slowa)
print(kubus_puchatek_slowa_n)

slowa = kubus_puchatek_slowa
kubus_n = 0
#for i, s in enumerate(kubus_puchatek_slowa):
#		if 'Kubuś' in s:
#		print(i,s)
#		kubus_n = kubus_n + 1 nnn
#print(kubus_n
#	s = s + " SIEMA"
#	s = s.split()
#	print(i, s)xxxx
for i, s in enumerate(slowa):

	if s == "Kłapouchy":
		print(slowa[i-1], s, slowa[1+1])
