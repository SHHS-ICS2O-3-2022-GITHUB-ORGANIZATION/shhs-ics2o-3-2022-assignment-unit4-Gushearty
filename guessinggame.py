import random #lets you use random number generators

low = int(input("input a low number: ")) # lets user pick a low number
hi = int(input("input a higher number: ")) # lets user pick a high number
print("")# adds a space to avoid it looking to crammed

ans = random.randint(low, hi)#picks a random number
guess = 0 #
guesses = 0#

while guess != ans: #if you dont get the answer right it keeps repeating
    guess = int( input("Guess a number in between "+str(low)+" and "+str(hi)+": " ) )#asks user for a guess
    print("")#space
    
    if guess != ans:#after you guess and get it wrong it tells you if the answer is higher or lower
    
        if guess < ans:#is the answer higher then the guess?
            print("the answer is higher then the number you picked")
            print("")#space
            
        elif guess > ans:#is the answer lower then the guess?
            print("the answer is lower then the number you picked")
            print("")#space
        
    guesses = guesses + 1 #increases amount of guesses

if guesses == 1:#if you got it in one try it displays a different message
    print("you got it in one try! good job")       
else: #if you didnt it tells you how many guesses you took
    print("good job, you got the number right in "+str(guesses)+" tries") 

