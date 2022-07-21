import sys
actualShop = None
shop = None

for line in sys.stdin:
    line = line.strip()
    nextShop, amount = line.split('-')
    if actualShop == nextShop:
        maxAmount = amount
    else:
        if actualShop:
            print(actualShop + ' ' + amount)
        actualShop = shop

print(actualShop +' '+ maxAmount)
