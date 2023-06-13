#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('digite um número'))
s = n1 + n1
m = n1 * 3
e = n1 ** (1/2)
print('O valor é {}, o dobro é {}, o triplo {} e a raíz quadrada é {}'.format(n1, s, m, e))