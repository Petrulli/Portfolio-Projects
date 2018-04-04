import random

highest = 10
answer = random.randrange(highest)
guess = int(input("Chute um número de 0 até %d:" %highest))
while (int(guess) != answer):
    if(int(guess) < answer):
        print("A resposta é maior")
    else:
        print("A resposta é menor")

    guess = input("Chute um número de 0 ate %d:" %highest)      
input("você acertou!!")
    
        
