import requests

# Pobranie tekstu ze strony (jako tafla tesktu).
multi = 'https://lotto.gazeta.pl/lotto/0,113233.html#e=NavLink'
surowe_info = requests.get( multi)
text = surowe_info.text

print(text)