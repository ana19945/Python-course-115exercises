#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('digite a altura: '))
largura = float(input('digite a largura: '))
área = altura * largura
print('A parede tem a dimensão de {} x {} e sua área é de {}m².'.format(altura, largura, área))
tinta = área / 2
print('Para pintar a parede você precisará de {}l de tinta.'.format(tinta))