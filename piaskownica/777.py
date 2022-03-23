import random

# n-symbol described how many numbers have to choosed from list of symbols called content list.
n_symbol = 3 
content_list = ['7','7','7','7','$','$','$','$','!','!','!','!','0','0','0','0','3','3','3','3']

# Meaning of symbols from content lis:
# 7 = 100 PLN
# $ = 200 PLN
# ! = *2 PLN
# 0 = 50 PLN
# 3 = 5 PLN

# choosing 3 symbols from content list and printing as 3 list.
win = random.sample(content_list, n_symbol)
win1 = random.sample(content_list, n_symbol)
win2 = random.sample(content_list, n_symbol)

print(win)
print(win1)
print(win2)

# this part checking programm drew three the same symbols in the straight line  in print1, print2, print3 and printed how many $$ you won.
lucky_list = win [0], win [1], win [2]
lucky_list1 = win1 [0], win1[1], win1[2]
lucky_list2 = win2 [0], win2[1], win2[2]


list_7 ='7','7','7'
list_dol = '$','$','$'
list_exc = '!','!','!'
list_0 = '0','0','0'
list_3 = '3','3','3'

if lucky_list == list_7:
   print('you won 300 PLN')
if lucky_list == list_dol:
   print('you won 600 PLN')
if lucky_list == list_exc:
   print('your reward will be multiply x2')
if lucky_list == list_0:
   print('you won 150 PLN')
if lucky_list == list_3:
   print('you won 15 PLN')

if lucky_list1 == list_7:
   print('you won 300 PLN')
if lucky_list1 == list_dol:
   print('you won 600 PLN')
if lucky_list1 == list_exc:
   print('your reward will be multiply x2')
if lucky_list1 == list_0:
   print('you won 150 PLN')
if lucky_list1 == list_3:
   print('you won 15 PLN')

if lucky_list2 == list_7:
   print('you won 300 PLN')
if lucky_list2 == list_dol:
   print('you won 600 PLN')
if lucky_list2 == list_exc:
   print('your reward will be multiply x2')
if lucky_list2 == list_0:
   print('you won 150 PLN')
if lucky_list2 == list_3:
   print('you won 15 PLN')

#This part checking if program drew three the same symbols in cross lines and printed how many $$ you won.

if win[0] == '7'  and win1 [1] == '7' and win2 [2] == '7':
   print('you won 300 PLN')

if win[0] == '$'  and win1 [1] == '$' and win2 [2] == '$':
   print('you won 600 PLN')

if win[0] == '!'  and win1 [1] == '!' and win2 [2] == '!':
   print('your reward will be multiply x2')

if win[0] == '0'  and win1 [1] == '0' and win2 [2] == '0':
   print('you won 150 PLN')

if win[0] == '3'  and win1 [1] == '3' and win2 [2] == '3':
   print('you won 15 PLN')

if win[2] == '7'  and win1 [1] == '7' and win2 [0] == '7':
   print('you won 300 PLN')

if win[2] == '$'  and win1 [1] == '$' and win2 [0] == '$':
   print('you won 600 PLN')

if win[2] == '!'  and win1 [1] == '!' and win2 [0] == '!':
   print('your reward will be multiply x2')

if win[2] == '0'  and win1 [1] == '0' and win2 [0] == '':
   print('you won 150 PLN')

if win[2] == '3'  and win1 [1] == '3' and win2 [0] == '3':
   print('you won 15 PLN')
   