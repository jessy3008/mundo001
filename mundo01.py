def desafio_001():
  print('olá mundo!')
  print('\033[1;35m-\033[m' * 65)
  
def desafio_002():
  nome = input ("qual é o seu nome? ")
  print('seja bem-vindo(a), {}!'.format(nome))
  print('\033[1;35m-\033[m' * 65)

def desafio_003():
  numero1 = int(input ('digite um número: '))
  numero2 = int(input ('digite outro número: '))
  soma = numero1 + numero2
  print('a soma desses números é:', soma)
  print('\033[1;35m-\033[m' * 65)
  
def desafio_004():
  a = (input("digite algo: "))
  print('o tipo dessa variável é:', type(a))
  print('só tem espaços?', a.isspace())
  print('é um número?', a.isnumeric())
  print('é alfabético?', a.isalpha())
  print('é numérico?', a.isalnum())
  print('está em maiúsculas?', a.isupper())
  print('está em minúsculas?', a.islower())
  print('está capitalizada?', a.istitle())
  print('\033[1;35m-\033[m' * 65)

def desafio_005():
  n = int(input("digite um número e descubra seu antecessor e sucessor: "))

  a = n - 1
  s = n + 1
  print('analisando o valor {}, seu antecessor é {} e seu sucessor é {}' .format(n, a, s))
  print('\033[1;35m-\033[m' * 65)

def desafio_006():
  a = int(input('digite um número: '))
  dobro = a * 2
  triplo = a * 3
  raiz = a ** (1/2)
  print('o dobro de {} vale {}.'.format(a, dobro))
  print('o triplo de {} vale {}.'.format(a, triplo))
  print('a raiz quadrada de {} vale {:.2f}'.format(a, raiz))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_007():
  n1 = float(input('digite a nota 1: '))
  n2 = float(input('digite a nota 2: '))
  media = (n1 + n2) / 2
  print('a média entre {} e {} é: {} ' .format(n1, n2, media))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_008():
  medida = float(input('digite uma distância em metros: '))
  cm = medida * 100
  mm = medida * 1000
  print('a medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_009():
  n = int(input('digite um número para ver a tabuada: '))
  print('{} x {:2} = {}'.format(n, 1, n*1))
  print('{} x {:2} = {}'.format(n, 2, n*2))
  print('{} x {:2} = {}'.format(n, 3, n*3))
  print('{} x {:2} = {}'.format(n, 4, n*4))
  print('{} x {:2} = {}'.format(n, 6, n*6))
  print('{} x {:2} = {}'.format(n, 7, n*7))
  print('{} x {:2} = {}'.format(n, 8, n*8))
  print('{} x {:2} = {}'.format(n, 9, n*9))
  print('{} x {:2} = {}'.format(n, 10, n*10))
  print('\033[1;35m-\033[m' * 65)

def desafio_010():
  valor_real = (float(input('quanto dinheiro você tem na carteira? ')))
  valor_dolar = valor_real / 4.81
  print('com R${} você pode comprar US${:.2f}'.format(valor_real, valor_dolar))
  print('\033[1;35m-\033[m' * 65)

def desafio_011():
  largura = float(input('digite a largura da parede: '))
  altura = float(input('digite a altura da parede: '))
  área = largura * altura
  print('sua parede tem a dimensão de {} X {} e sua área é de {}m²'. format(largura, altura, área))
  tinta = área / 2
  print('para pintar a parede você precisa de {}L de tinta.'.format(tinta))
  print('\033[1;35m-\033[m' * 65)

def desafio_012():
  preco = float(input('qual o preço do produto? R$'))
  preco_com_desconto = preco - (preco * 5 / 100)
  print('o preço sem desconto era R${:.2f}, e o valor do produto com desconto é R$ {:.2f}'.format(preco, preco_com_desconto))
  print('\033[1;35m-\033[m' * 65)

def desafio_013():
  salario1 = float(input('qual é o salário do seu funcionário? R$ '))
  salario2 = salario1 + (salario1 * 15 /100)
  print('Um salário que ganhava R$ {:.2f}, com 15% de aumento receberá R${:.2f}'.format(salario1, salario2))
  print('\033[1;35m-\033[m' * 65)

def desafio_014():
  t_celcius = float(input('informe a temperatura em ºC: '))
  t_fahrenheit = 9 * t_celcius / 5 + 32
  print('a temperatura de {}ºC corresponde a {}ºF!'.format(t_celcius, t_fahrenheit))
  print('\033[1;35m-\033[m' * 65)

def desafio_015():
  dias_alugados = int(input('quantos dias alugados? '))
  km = float(input('quantos km rodados? '))
  pago = (dias_alugados * 60) + (km * 0.15)
  print('o total a pagar é de R${:.2f}'.format(pago))
  print('\033[1;35m-\033[m' * 65)

def desafio_016():
  
  n = float(input("valor: "))
  print("o valor informado foi de {} e sua parte interia é {}".format(n, int(n)))
  print('\033[1;35m-\033[m' * 65)

def desafio_017():
  
  co = float(input("comprimento do cateto oposto: "))
  ca = float(input("comprimento do cateto adjcente: "))
  h = (co * 2 + ca * 2) ** (1/2)
  print("a hipotenusa é {}".format(h))
  print('\033[1;35m-\033[m' * 65)

def desafio_018():
  
  from math import radians, sin, cos, tan

  an = float(input("digite o angulo: "))
  se = sin(radians(an))
  co = cos(radians(an))
  ta = tan(radians(an))
  print("o angulo {} tem como seno {}".format(an, se))
  print("o angulo {} tem como cosseno {}".format(an, co))
  print("o angulo {} tem como tangente {}".format(an, ta))
  print('\033[1;35m-\033[m' * 65)

def desafio_019():
  
  from random import choice

  a1 = input("primeiro aluno: ")
  a2 = input("segundo aluno: ")
  a3 = input("terceiro aluno: ")
  a4 = input("quarto aulno: ")
  l = [a1, a2, a3, a4]
  e = choice(l)
  print("o aluno sorteado foi {}".format(e))
  print('\033[1;35m-\033[m' * 65)

def desafio_020():

  from random import shuffle

  a1 = input("primeiro aluno: ")
  a2 = input("segundo aluno: ")
  a3 = input("terceiro aluno: ")
  a4 = input("quarto aluno: ")
  l = [a1, a2, a3, a4]
  shuffle(l)
  print("ordem de apresentação será ")
  print(l)
  print('\033[1;35m-\033[m' * 65)

# dasafio021 

def desafio_022():
  
  n = input("seu nome: ").strip()
  print("analisando...")
  print("nome em maiúsculo: {}".format(n.upper()))
  print("nome em minúsculo: {}".format(n.lower()))
  print("nome tem {} letras".format(len(n) - n.count(" ")))
  s = n.split()
  print("o primeiro nome é {} e ele possui {} letras".format(s[0], len(s[0])))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_023():
  
  n = int(input("numero: "))
  u = n // 1 % 10
  d = n // 10 % 10
  c = n // 100 % 10
  m = n // 1000 % 10
  print("anisando o numero {}".format(n))
  print("unidade {}".format(u))
  print("dezena {}".format(d))
  print("centena {}".format(c))
  print("milhar {}".format(m))
  print('\033[1;35m-\033[m' * 65)

def desafio_024():
  
  c = input("qual cidade você nasceu?: ").strip()
  print(c[:5].upper() == "SANTOS")
  print('\033[1;35m-\033[m' * 65)

def desafio_025():
  
  n = input("nome completo: ").strip()
  print("esse nome tem Oliveira? {}".format("Oliveira" in n.lower()))
  print('\033[1;35m-\033[m' * 65)

def desafio_026():
  
  f = str(input("digite uma frase:")).upper().strip()
  print("quantidades de vezes que aparece a letra 'A' {}".format(f.count('A')))
  print("a primeira letra 'A' apareceu nessa posição {}".format(f.find('A') +1 ))
  print("a ultima letra 'A' apareceu nessa posição {}".format(f.rfind('A') +1 ))
  print('\033[1;35m-\033[m' * 65)

def desafio_027():

  n = str(input("nome completo: ")).strip()
  name = n.split()
  print("é um prazer te conhecer")
  print("primeiro nome: {}".format(name[0]))
  print("ultimo nome: {}".format(name[len(name) -1]))
  print('\033[1;35m-\033[m' * 65)

def desafio_028():

  from random import randint

  comp = randint(0,5)
  print("=====================")
  print("adivinhe o numero 'dica: é um numero entre 0 e 5'")
  print("====================")

  jog = int(input("advinhe o número: "))

  if jog == comp:
    print("PARABÉNS!!!")

  else:
    print("ERROU!!")
  print('\033[1;35m-\033[m' * 65)

def desafio_029():

  v = float(input("velocidade atual do seu automóvel: "))

  if v > 80:
    print("MULTADO! você passou do limite de velocidade")

    m = (v - 80) * 7

    print("sua multa é de R${}".format(m))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_030():

  num = int(input("número: "))
  r = num % 2

  if r == 0:
    print("o numero {} é PAR".format(num))

  else:
    print("o numero é {} é IMPAR".format(num))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_031():

  d = float(input("qual a distancia da sua viagem?: "))
  print("você vai comecar sua viagem de {}km".format(d))
  p = d * 0.05  if d <= 200  else d * 0.45
  print("sua passagem custará R${}".format(p))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_032():

  from datetime import date

  a = int(input("qual ano quer que seja analizado? caso queria analisar o ano atual digite 0 : "))

  if a == 0:
    a = date.today().year

  if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("o ano {} é bissexto".format(a))

  else:
    print("o ano {} não é bissexto".format(a))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_033():

  p = int(input("primeiro valor: "))
  s = int(input("segundo valor: "))
  t = int(input("terceiro valor: "))
   
  m = p 
  if s < p and s < t:
    m = s

  if t < p and t < s:
    m = t

  
  ma = p
  if s > p and s > t:
    ma = s

  if t > p and t > b:
    ma = t 

  print("menor valor digitado {}".format(m))
  print("maior valor digitado {}".format(ma))
  print('\033[1;35m-\033[m' * 65)
  
def desafio_034():

  s = float(input("qual o salario do funcionario?: R$"))

  if s <= 1250:
    n = s + (s * 15 / 100)

  else:
    n = s + (s * 10 / 100)

  print("quem ganhava R${} passou a ganhar R${}".format(s, n))

print('\033[1;35m-\033[m' * 65)

def desafio_035():

  print("analisando o triangulo...")

  r1 = float(input("primeiro comprimento:"))
  r2 = float(input("segundo comprimento:"))
  r3 = float(input("terceiro comprimento:"))

  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("pode ser feito um triangulo")

  else:
    print("não pode ser um triangulo")
  print('\033[1;35m-\033[m' * 65)