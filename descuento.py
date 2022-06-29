''' Una tienda oferce un descuento del 15% sobre el total de
la compra y un cliente desea saber cuanto pagará finalmente
'''


compra = float(input('Ingrese el precio  '))

descuento = 15 * compra / 100

total = compra - descuento

print(f'Tiene un descuento de $ {descuento}. Va a pagar $ {total}')


