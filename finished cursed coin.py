import colorama
print(colorama.Fore.MAGENTA)
print(colorama.Style.DIM)
print(colorama.Back.BLUE)
import random

coinsleft = random.randint(15, 30)
coinsToRemove = 0
userTurn = True
print('This is aa simple game, a short game ')
input("This is a game where players take turns taking coins from a bucket of coins. or you go up against A.I. (press enter to conitue)")
input("The player who takes the last coin loses. (press enter to conitue)") 
inp = input ("Choose 1 or 2 player ")
one_player=(inp == "2")
if one_player:
    while coinsleft > 0:
        while userTurn == True and coinsleft > 0:

            coinsToRemove = int(input("Player 1 how many coins do you want to remove?"))

            if coinsToRemove > 3:
                print("You can't remove more than three coins at a time!The current coin count is: " + str(coinsleft) )     
            elif coinsleft - coinsToRemove < 0:
                print("There aren't that many coins left!") #Give user error!  
            else:
                coinsleft -= coinsToRemove
                print( "You removed " + str(coinsToRemove) + 
                    " coin(s)! The current coin count is: " + str(coinsleft) )    

                userTurn = False                       

        while userTurn == False and coinsleft > 0:

            coinsToRemove = int(input("Player 2 how many coins do you want to remove?"))

            if coinsToRemove > 3:
                print("You can't remove more than three coins at a time!The current coin count is: " + str(coinsleft) )     
            elif coinsleft - coinsToRemove < 0:
                print("There aren't that many coins left!") #Give user error!  
            else:
                coinsleft -= coinsToRemove
                print( "You removed " + str(coinsToRemove) + 
                    " coin(s)! The current coin count is: " + str(coinsleft) )    

                userTurn = True          

    if userTurn == True:
        print("The A.I took the last coin, it lost. You won the game!")
    else:
        print("You took the last coin, you lost. The A.I. won the game!")

else:
    while coinsleft > 0:
        while userTurn == True and coinsleft > 0:

            coinsToRemove = int(input("How many coins do you want to remove?"))

            if coinsToRemove > 3:
                print("You can't remove more than three coins at a time!The current coin count is: " + str(coinsleft) )     
            elif coinsleft - coinsToRemove < 0:
                print("There aren't that many coins left!") #Give user error!  
            else:
                coinsleft -= coinsToRemove
                print( "You removed " + str(coinsToRemove) + 
                    " coin(s)! The current coin count is: " + str(coinsleft) )    

                userTurn = False                       

        while userTurn == False and coinsleft > 0:

            aiRemoves = random.randint( 1, min(3, coinsleft) ) #Take smaller value between 3 and the coins that are left
            coinsleft -= aiRemoves

            print( "The A.I. removed " + str(aiRemoves) + 
                " coin(s)! The current coin count is: " + str(coinsleft) )    

            userTurn = True 