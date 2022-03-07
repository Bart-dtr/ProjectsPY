
import random

# this value described how many numbers should be choosed 5 among 42.
n_num = 5

# this is list of numbers which are involved in the raffle
mini = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ',' 10 '
,' 11 ',' 12 ',' 13 ',' 14 ',' 15 ',' 16 ', ' 17 ', ' 18 ', ' 19 ', ' 20 ', ' 21 '
, ' 22 ', ' 23 ', ' 24 ', ' 25 ',' 26 ',' 27 ',' 28 ',' 29 ',' 30 ',' 31 ',' 32 '
,' 33 ', ' 34 ', ' 35 ', ' 36 ',' 37 ',' 38 ',' 39 ',' 40 ',' 41 ',' 42 ']

n_num2 = 6
# this value described how many numbers should be choosed 6 among 49
big = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ',' 10 '
,' 11 ',' 12 ',' 13 ',' 14 ',' 15 ',' 16 ', ' 17 ', ' 18 ', ' 19 ', ' 20 ', ' 21 '
, ' 22 ', ' 23 ', ' 24 ', ' 25 ',' 26 ',' 27 ',' 28 ',' 29 ',' 30 ',' 31 ',' 32 '
,' 33 ', ' 34 ', ' 35 ', ' 36 ',' 37 ',' 38 ',' 39 ',' 40 ',' 41 ',' 42 ',' 43 ', 
' 44 ',' 45 ',' 46 ',' 47 ',' 48 ',' 49 ']

n_num3 = 10
# this value described how many numbers should be choosed 10 among 80
multi = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ',' 10 '
,' 11 ',' 12 ',' 13 ',' 14 ',' 15 ',' 16 ', ' 17 ', ' 18 ', ' 19 ', ' 20 ', ' 21 '
, ' 22 ', ' 23 ', ' 24 ', ' 25 ',' 26 ',' 27 ',' 28 ',' 29 ',' 30 ',' 31 ',' 32 '
,' 33 ', ' 34 ', ' 35 ', ' 36 ',' 37 ',' 38 ',' 39 ',' 40 ',' 41 ', ' 42 ', ' 43 ', 
' 44 ', ' 45 ', ' 46 ', ' 47 ', ' 48 ', ' 49 ',' 50 ',' 51 ',' 52 ',' 53 ',' 54 ',' 55 '
,' 56 ', ' 57 ', ' 58 ', ' 59 ', ' 60 ', ' 61 ', ' 62 ', ' 63 ', ' 64 ', ' 65 ',' 66 '
,' 67 ',' 68 ',' 69 ',' 70 ',' 71 ',' 72 ',' 73 ', ' 74 ', ' 75 ', ' 76 ',' 77 ',' 78 ',' 79 ',' 80 ']


# random choose 5 numbers (n_num) from number list (mini)
rand_digits = random.sample(mini, n_num)
rand_digits1 = random.sample(big, n_num2)
rand_digits2 = random.sample(multi, n_num3)

mini_list =  rand_digits
lotto_list = random.sample(mini_list, n_num)
list = ''.join(lotto_list)

print('Mini lotto:',list)

big_list =  rand_digits1
lotto_list1 = random.sample(big_list, n_num2)
list1 = ''.join(lotto_list1)

print('Lotto:',list1)

multi_list =  rand_digits2
lotto_list2 = random.sample(multi_list, n_num3)
list2 = ''.join(lotto_list2)

print('Multi Multi:',list2)
