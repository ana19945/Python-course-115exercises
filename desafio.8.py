#Escreva um programa que leia um valor em metros e o exiba em convertido em centímetros e milímetros
metros = float(input('Digite um valor: '))
cm = metros * 100 #não entendi pq a multiplicação não funcionou
mm = metros * 1000
km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
dm = metros * 10
print('São {} metros, {} cm, {} mm, {} km, {} hm, {} dam, {} dm'.format(metros, cm , mm, km, hm, dam, dm ))