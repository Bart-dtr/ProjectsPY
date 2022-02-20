
VAT = 23
calculated_VAT = (1 + VAT / 100)

Price_1_nett = 10000
Price_2_nett = 5000

Price_1_gross = Price_1_nett * calculated_VAT
Price_2_gross = Price_2_nett * calculated_VAT

print(Price_1_gross)
print(Price_2_gross)