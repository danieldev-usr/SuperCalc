from ast import Pow
import os
import time
import math

#nao sei pq mas achei melhor jogar aqui em cima kkk

def resolver_equacao_quadratica(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Duas raízes reais distintas: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Uma raiz real dupla: x = {x}"
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        return f"Duas raízes complexas conjugadas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

def transformacao_de_medidas():
    print(f""" {green}
    [1] Metro cúbico para Decímetro cúbico (m³/dm³)
    [2] Centímetro cúbico para Milímetro cúbico (cm³/mm³)
    [3] Decímetro cúbico para Milímetro cúbico (dm³/mm³)
    [4] Mililitro para Litro (ml/l)
    [5] Litro para Centilitro (l/cl)
    [6] Litro para Mililitro (l/ml)
    [7] Metro cúbico para Litro (m³/l)
    [8] Decímetro cúbico para Litro (dm³/l)
    [9] Centímetro cúbico para Mililitro (cm³/ml)
    """)

    opcao = input(f"{red}Digite a opção desejada: ")

    if opcao == '1':
        metros_cubicos = float(input("Digite o valor em metros cúbicos: "))
        decimetros_cubicos = metros_cubicos * 1000
        print(f"{metros_cubicos} m³ equivale a {decimetros_cubicos} dm³")

    elif opcao == '2':
        centimetros_cubicos = float(input("Digite o valor em centímetros cúbicos: "))
        milimetros_cubicos = centimetros_cubicos * 1000
        print(f"{centimetros_cubicos} cm³ equivale a {milimetros_cubicos} mm³")

    elif opcao == '3':
        decimetros_cubicos = float(input("Digite o valor em decímetros cúbicos: "))
        milimetros_cubicos = decimetros_cubicos * 1000
        print(f"{decimetros_cubicos} dm³ equivale a {milimetros_cubicos} mm³")

    elif opcao == '4':
        mililitros = float(input("Digite o valor em mililitros: "))
        litros = mililitros / 1000
        print(f"{mililitros} ml equivale a {litros} l")

    elif opcao == '5':
        litros = float(input("Digite o valor em litros: "))
        centilitros = litros * 100
        print(f"{litros} l equivale a {centilitros} cl")

    elif opcao == '6':
        litros = float(input("Digite o valor em litros: "))
        mililitros = litros * 1000
        print(f"{litros} l equivale a {mililitros} ml")

    elif opcao == '7':
        metros_cubicos = float(input("Digite o valor em metros cúbicos: "))
        litros = metros_cubicos * 1000
        print(f"{metros_cubicos} m³ equivale a {litros} l")

    elif opcao == '8':
        decimetros_cubicos = float(input("Digite o valor em decímetros cúbicos: "))
        litros = decimetros_cubicos * 1000
        print(f"{decimetros_cubicos} dm³ equivale a {litros} l")

    elif opcao == '9':
        centimetros_cubicos = float(input("Digite o valor em centímetros cúbicos: "))
        mililitros = centimetros_cubicos
        print(f"{centimetros_cubicos} cm³ equivale a {mililitros} ml")

    else:
        print("Opção inválida!")


black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

#2

def limpar():os.system("clear")

print ("""

Criado por: Wan - 09/08/22 - 10/08/22
Python 3.7
ATUALIZAÇÃO 09/02/2024

[Aguarde um instante...]

""")

time.sleep(2)

limpar()

print(f"{red}------Calculadora------")

print(f"""{green}
[01] Somar volume de um cubo
[02] Somar volume de um prisma (3 valores)
[03] Somar volume de um cilindro
[04] Somar massa (Newton)
[05] Somar gastos eletricos (KwH)
[06] Somar porcentagem da perda de peso
[07] Transformação de medidas 
[08] Porcentagem
[09] Teorema de Pitagoras
[10] Equação Quadratica
[00] Feedbacks e erros
""")

while True:

    x = input(f"{red}[Selecione]: ")

    if x == '01':

        print(f"{blue} ")

        ladoa = float(input("Digite o lado A do cubo: "))

        ladob = float(input("Digite o lado B do cubo: "))

        ladoc = float(input("Digite o lado C do cubo: "))

        v1c = ladoa * ladob

        v2c = v1c * ladoc

        print(" ")

        print(f" v = {ladoa} x {ladob} x {ladoc}")

        print(f" v = {v1c} x {ladoc}")

        print(f" v = {v2c}")

        print(" ")

    elif x == '02':

        print(f"{purple}")

        ladoap = float(input("Digite a base do prisma (1/2): "))

        ladobp = float(input("Digite a base do prisma (2/2): "))

        ladocp = float(input("Digite a altura do prisma: "))

        v1p = ladoap * ladobp

        v2p = v1p / 2

        v3p = v2p * ladocp

        print(" ")

        print(f"At = {ladoap} x {ladobp} ÷ 2 = {v2p}")

        print(f"v = {v2p} x {ladocp}")

        print(f"v = {v3p}")

        print(" ")

    elif x == '03':

        print(f"{cyan}")

        pi = 3.14

        raio = float(input("Digite o valor do raio: "))

        altura = float(input("Digite o valor da altura: "))

        v1s = raio / 2

        v2s = v1s * v1s

        v3s = v2s * pi

        v4s = v3s * altura

        print(" ")

        print(f"V = π x {v1s}² x {altura}")

        print(f"V = π x {v2s} x {altura}")

        print(f"V = {v3s} x {altura} ")

        print(f"V = {v4s}")

        print(' ')

    elif x == '04':

        print(f"{yellow} ")

        vlm = float(input("Digite o volume: "))

        dns = float(input("Digite a densidade: "))

        sm = vlm*dns

        print(f"{vlm} x {dns} = {sm}")

        print(" ")

        

    elif x == '05':

        print(f"{white} ")

        watts = float(input("Watt do aparelho: "))

        tmp = int(input("Horas de uso do aparelho: "))

        cw = float(input("Custo do Watt na sua regiao: "))

        d = watts*tmp

        e = d / 1000

        print(" ")

        print(f"{watts} x {tmp} ÷ 1000 = {e}")

        vdc = e * tmp * cw * 30

        print(f"Voce gasta R${vdc} mensalmente")

        print(" ")

    elif x == '06':

        print(f"{green}")

        pesoI = float(input("Digite o peso inicial: "))

        pesoA = float(input("Digite o peso atual: "))

        calc11 = pesoI - pesoA

        calc22 = calc11 / pesoI

        calc33 = calc22* 100

        

        print(" ")

        print(f"{pesoI} - {pesoA} = {calc11}")

        print(f"{calc11} ÷ {pesoI} = {calc22} ")

        print(f"{calc22} x 100 = {calc33}%")

        print(" ")

    elif x == "07":
    	print("xx")
    	transformacao_de_medidas()

    elif x == "08":

        print(f"{purple} ")

        pv1 = float(input("Digite a porcentagem: "))

        pv2 = float(input("Digite o valor para calcular: "))

        rgdt = pv1 * pv2 / 100

        print(rgdt, "%")

    elif x == "09":

        print(f"{cyan}")

        print("obs; apenas calculamos o valor da hipotenusa!!!")

        cateto1 = float(input("Digite o valor do cateto B: "))

        cateto2 = float(input("Digite o valor do cateto A: "))

        sm1 = cateto1 * cateto1

        sm2 = cateto2 * cateto2

        sm3 = sm1 + sm2

        math.sqrt(sm3)

        print("a² = b² + c²")

        print(f"a² = {cateto1}² + {cateto2}²")

        print(f"a² = {sm1} + {sm2}")

        print(f"a² = {sm3}")

        print(f"a = √{sm3}")

        a = math.sqrt(sm3)

        print(f"a = {a}")

    elif x == "10":
    	print(f"{blue}")
    	a = float(input("Digite o coeficiente a: "))
    	b = float(input("Digite o coeficiente b: "))
    	c = float(input("Digite o coeficiente c: "))
    	print(resolver_equacao_quadratica(a, b, c))


    elif x == "00":

        print(" ")
        print(f"{purple}")

        print("Instagram para contato: @wan.cxx")

        print("Telegram para contato: @BaalZevuv6")

        print("Email para contato: zdanxhacking@gmail.com")

        print("    ")

        print("    ")

        print("MIT license")

        print("""

        MIT License

Copyright (c) 2022 Daniel 

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.

        

        """)
 
