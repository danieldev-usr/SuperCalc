from ast import Pow
import os
import time
import math


#2

def limpar():os.system("clear")

print ("""
Criado por: Wan - 09/08/22 - 10/08/22
""")
time.sleep(0.5)
limpar()

print("------Calculadora------")
print("""
[01] Somar volume de um cubo
[02] Somar volume de um prisma (3 valores)
[03] Somar volume de um cilindro
[04] Somar massa (Newton)
[05] Somar gastos eletricos (KwH)
[06] Somar porcentagem da perda de peso
[07] Transformação de medidas (Nao funcional...)
[08] Porcentagem
[09] Teorema de Pitagoras
[00] Feedbacks e erros
""")

while True:
    print(" ")
    x = input("[Selecione]: ")

    if x == '01':
        print(" ")
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
        print(" ")
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
        print(" ")
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
        print(" ")
        vlm = float(input("Digite o volume: "))
        dns = float(input("Digite a densidade: "))
        sm = vlm*dns
        print(f"{vlm} x {dns} = {sm}")
        print(" ")
        
    elif x == '05':
        print(" ")

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
        print(" ")
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

    elif x == "00":
        print(" ")
        print("""
        [1] Metro cubico para Decimetro cubico (m3/dm3)
        [02] Centimetro cubico para Milimetro cubico (cm3/mm3)
        [03] Decimetro cubico  para Milimetro cubico
        [04] Mililitro para litro (ml/l)
        [05] Litro para centilitro (l/cl)
        [06] Litro para Mililitro (l/ml)
        [07] Metro cubico para Litro (m3/l)
        [08] Decimetro cubico para Litro (dm3/l)
        [09] Centimetro cubico para mililitro (cm3/ml)

        """)
        lks = int(input("Digite a opçao: "))
        if lks == "1":
            vldpdt = int(input("Digite os metros: "))
            cont1 = vldpdt * 1000
            print(f"{cont1} DM3")


    elif x == "08":
        print(" ")
        pv1 = float(input("Digite a porcentagem: "))
        pv2 = float(input("Digite o valor para calcular: "))

        rgdt = pv1 * pv2 / 100

        print(rgdt, "%")


    elif x == "09":
        print(" ")
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




    elif x == "00":
        print(" ")
        print("Instagram para contato: @metalheadkkkk")
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
