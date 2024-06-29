print('laterais')
l= float(input('qual e a Largur: '))
a = float(input('qual e a Altura: '))
print('frentes')
l_2= float(input('qual e a Largur: '))

a2 = l * a 
area = a2 * 2
a_2 = l * a 


print('calculo das laterais: largura: {} é da altura: {} e igual a {:.2f}m²'.format(l, a, area))
print('calculo da frente: largura: {} é da altura: {} e igual a {:.2f}m²'.format(l, a, a2))

soma = area + a2
total = soma * 120 
custo = soma * 30
print('a soma da frente e das laterais:{:.2f}'.format(soma))
print('o total disso tudo ficaria R${:.2f}'.format(total))
print('e o custo disso tudo seria R${:.2f}'.format(custo))