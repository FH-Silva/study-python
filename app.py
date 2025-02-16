import os
import math

# Variaveis
velocidade, v_inicial, tempo, altura, a_inicial, resultado, gravidade = 0,0,0,0,0,0,9.8

# Funções
def boas_vindas():
    print ("""

██████╗░███████╗███╗░░░███╗░░░░░░██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░██╗
██╔══██╗██╔════╝████╗░████║░░░░░░██║░░░██║██║████╗░██║██╔══██╗██╔══██╗██║
██████╦╝█████╗░░██╔████╔██║█████╗╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║██║
██╔══██╗██╔══╝░░██║╚██╔╝██║╚════╝░╚████╔╝░██║██║╚████║██║░░██║██║░░██║╚═╝
██████╦╝███████╗██║░╚═╝░██║░░░░░░░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝██╗
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░░░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝

    """)

def calcular_velocidade():
    os.system("cls")
    print("Opção escolhida foi Cálculo da Velocidade.")
    
    print("""
Fórmula: V = V0 + g * t
            
    Sendo,
    V = Velocidade (m/s)
    V0 = Velocidade Inicial (m/s)
    t = Tempo (s)
    g = Gravidade, considerando g = 9,8 m/s²
          """)
    
    v_inicial = int(input("Informe o valor da Velocidade Inicial: "))
    tempo = int(input("Informe o valor do Tempo: "))
    
    velocidade = v_inicial + gravidade * tempo
    
    print(f"O resultado obtido foi: V = {velocidade}m/s")
    
def calcular_posicao():
    os.system("cls")
    print("Opção escolhida foi Cálculo da Altura.")
    
    print("""
Fórmula: h = h0 + V0 * t + (g * t² / 2)
            
    Sendo,
    h = Altura
    h0 = Altura Inicial
    V0 = Velocidade Inicial (m/s)
    t = Tempo (s)
    g = Gravidade, considerando g = 9,8 m/s²
          """)
    
    altura = a_inicial + v_inicial * tempo + (gravidade * math.exp2(tempo) // 2)
    
    print(f"O resultado obtido foi: {altura}m")

def calcular_tempo():
    os.system("cls")
    print("Opção escolhida foi Cálculo do Tempo.")
    
    print("""
Fórmula: t = √(2 * h / g) 
            
    Sendo,
    t = Tempo (s)
    h = Altura
    g = Gravidade, considerando g = 9,8 m/s²
          """)
    
    altura = int(input("Informe o valor da altura: "))
    
    tempo = round(math.sqrt(2 * altura // gravidade), 2)
    
    print(f"O resultado obtido foi: {tempo}s")


def main():

# Entrada
    boas_vindas()

    """ Cria um loop que ao digitar qualquer caractere que não seja 1, 2 ou 3 repete o bloco """
    while True:
        
        try:
            escolha_formula = int(input("""
Escolha uma opção. 
                                        
1. Calcular Velocidade 
2. Calcular Posição 
3. Calcular Tempo 
                                        
Digite:  """))
    
            if escolha_formula == 1 or 2 or 3:
            
                match escolha_formula:
                    case 1:
                        calcular_velocidade()
        
                    case 2:
                        calcular_posicao()
        
                    case 3:
                        calcular_tempo()
                break
  
        except:
            print("Valor Inválido")
            

main()