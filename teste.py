#1) Observe o trecho de código abaixo:
#int INDICE = 13, SOMA = 0, K = 0;
#enquanto K < INDICE faça
#{
#K = K + 1;
#SOMA = SOMA + K;
#}
#imprimir(SOMA);


# Indice = 13

# soma = 0

# k = 0

# while k < Indice:
#     k = k + 1
#     soma = soma + k

# print(soma)

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

#def fibonacci(n):
#    a, b = 0, 1
#    sequencia_fibonacci = [a,b]

#   while b <= n:
#        a, b = b, a + b
#        sequencia_fibonacci.append(b)
#   if n in sequencia_fibonacci:
#        return True
#    else:
#        return False

#numero = int(input('Digite o numero que deseja verificar: '))

#if fibonacci(numero):
#    print('Pertence')
#else:
#    print('Nao pertence')

#3) Descubra a lógica e complete o próximo elemento:
#a) 1, 3, 5, 7, 9

#b) 2, 4, 8, 16, 32, 64, 128

#c) 0, 1, 4, 9, 16, 25, 36,49

#d) 4, 16, 36, 64, 100

#e) 1, 1, 2, 3, 5, 8, 13

#f) 2,10, 12, 16, 17, 18, 19, 200


#5) problema das lampadas:
#Bom basta apenas acender um dos interruptores por um tempo, depois deixamos o segundo e vamos na sala, se estiver acessa
#corresponde ao interruptor dois, se estiver quente ao 1, se estiver fria ao 3.

#5) inveter string:
#def inverter_string(s):
#    string_invertida = ""

#    for i in range(len(s) - 1, -1, -1):
#        string_invertida += s[i]

#    return string_invertida


#string_original = input("Digite uma string: ")

#string_invertida = inverter_string(string_original)

#print("String invertida:", string_invertida)