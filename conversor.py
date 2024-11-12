peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
polegada = altura * 0.393701
libras = peso * 2.20462
if polegada > 12 and altura > 100:
    conversaoaltura = altura/100
    conversaopolegada= polegada/12
print('\33[1;34m{:.2f}\33[m kg = \33[1;31m{:.2f}\33[m lbs'.format(peso,libras)) 
print('\33[1;34m{:.2f}\33[m m = \33[1;31m{:.2f}\33[m in'.format(conversaoaltura,conversaopolegada)) 