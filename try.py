import random
import math


min_bound=int(input("Enter a minimal bound?: "))
max_bound=int(input("Enter a maximum bound?: "))
randomN = random.randint(min_bound,max_bound)

total_chances = math.ceil(math.log(max_bound-min_bound+1,2))
print(total_chances)

guesses= 0
flag = False
while guesses<total_chances:
    guesses+=1
    guess=int(input("Enter your guess?:"))
    if randomN==guess:
        print("Congratulations!number of guess",guesses)
        flag=True
        break
    elif randomN < guess:
        print("Yo guessed too low")
    else:
        print("You guessed too high")
        

if not flag:
   
    print(f"The number is {randomN}")
    print("\tBetter Luck Next time!")

