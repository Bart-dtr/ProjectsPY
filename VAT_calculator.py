Price_1_nett = 10000
Price_2_nett = 5000

TAX_1 = 23
calculated_TAX_1 = (1 + TAX_1 / 100)

Price_1_gross = Price_1_nett * calculated_TAX_1
Price_2_gross = Price_2_nett * calculated_TAX_1

print("TAX 23 =", Price_1_gross)
print("TAX 23 =", Price_2_gross)

TAX_2 = 8
calculated_TAX_2 = (1 + TAX_2 / 100)

Price_1_gross = Price_1_nett * calculated_TAX_2
Price_2_gross = Price_2_nett * calculated_TAX_2

print("TAX 8 =", Price_1_gross)
print("TAX 8 =", Price_2_gross)

TAX_3 = 5
calculated_TAX_3 = (1 + TAX_3 / 100)

Price_1_gross = Price_1_nett * calculated_TAX_3
Price_2_gross = Price_2_nett * calculated_TAX_3

print("TAX 5 =", Price_1_gross)
print("TAX 5 =", Price_2_gross)
