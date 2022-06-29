''' Una tienda oferce un descuento del 15% sobre el total de
la compra y un cliente desea saber cuanto pagará finalmente
'''


compra = float(input('Ingrese el precio  '))

descuento = compra * 0.15
total = compra - descuento

print(f'Tiene un descuento de $ {descuento:.2f}. Va a pagar $ {total:.2f}')


