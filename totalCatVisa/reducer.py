import sys
actualCat = None
total = None

print('Categoria        Monto Total         (Pagado Con Visa)')

for line in sys.stdin:
    line = line.strip()
    nextCat, amount = line.split('-')
    if actualCat == nextCat:
        total += amount
    else:
        if actualCat:
            print(actualCat + ' ' + total)
            total = 0
            actualShop = nextCat

print(actualShop +' '+ total)
