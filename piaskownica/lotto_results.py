import requests

# Pobranie tekstu ze strony (jako tafla tesktu).
multi = 'http://qlikviewdev5/QvAJAXZfc/opendoc.htm?document=Deal%20Administration%20D2D%20Process.qvw&host=QVS%40qlikviewdev5'
surowe_info = requests.get( multi)
text = surowe_info.text

print(text)