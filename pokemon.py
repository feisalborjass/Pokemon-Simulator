#Authors: Feisal Borjas, Noah Colaco
#Date: Tuesday, May 23, 2017
#File Name: pokemon.py
#Description: This program is a text-based version of the role-playing game, "Pokemon." The user will be able to choose a pokemon of their own and
#fight others with it. Each pokemon will have their own damage/HP attributes that will increase if they defeat other pokemon in the wild. Some in-game
#mechanics include a pokemon center to heal when not in a fight, a run away option when fighting in the wild, and a gym to fight other trainers in.
#To win, the player must defeat all trainers in the gym. The game is considered a loss if the user's pokemon reaches 0 HP. 

import random #Import random so random numbers can be used.


def helpMessage(): #Make 'helpMessage()' a function that displays the help menu.
    print('--------------------------------------------------------------------------------------------------------')
    print('Welcome to Pokemon! In this game, you\'ll enter a world where you can train a pokemon of your \
own and fight others. To win, you must earn your title as a master pokemon trainer by defeating the trainers \
in the gym. However, your pokemon will be too weak to beat the gym once you first get it, so it is a good idea \
to make it stronger first by fighting other pokemon in the wild.')
    print('')
    print('Fighting is simple. You enter "a" to attack and then the enemy attacks you. If you don\'t think you will \
win the fight, you can enter "r" to run for a 50% chance of getting away. If your pokemon\'s health is low, eneter \
pc to go to the pokemon center and heal while not in a battle.')
    print('')
    print('If your pokemon reaches 0 health, the game is considered a loss. With the use of strategy, you\'ll be able \
to beat the gym leader and win the game. Good luck!')   #Display the help menu.
    print('--------------------------------------------------------------------------------------------------------')

def errorMessage(): #Make a function called 'errorMessage()' that displays a message when there is an error.
    print('This should not happen.') #Display 'This should not happen'.

def programInputMessage(): #Make a function called 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
    print('Enter "1" to start the program') #Display a message telling the user to press "S" to start the program.
    print('Enter "2" to display the help menu') #Disply a message telling the user to press "H" to display the help menu.
    print('Enter "3" to quit the program') #Display a message telling the user to press "Q" to quit the program.

def getProgramInput(): #Make 'getProgramInput()' a function that gets an input from the user for what they want to do in the program.
    while True: #Set up a loop that repeats itself until the user enters a number 
        try:
            user_input = int(input("Enter a number: ")) #Get the input from the user
            if user_input == 1: #Check if 'user_input' is 1.
                return user_input #Return 'user_input' back to the variable it is being used in.
            elif user_input == 2: #Check if 'user_input' is 2.
                return user_input #Return 'user_input' back to the variable it is being used in.
            elif user_input == 3: #Check if 'user_input' is 3.
                return user_input #Return 'user_input' back to the variable it is being used in.
            else: #Check if everything else in the 'if' statement is False.
                blankLine() #Display a blank line
            break
        except ValueError: #Execute if user does not enter in a number.
            print("Error. Enter a valid command") #Tell them to enter a valid number.
            lineBreak() #Display a line of characters that separates the previous line from the next.
            programInputMessage() #Get an input from the user for if they want to start or quit the program, or if they want the help menu.
            blankLine() #Display a blank line

def checkProgramChoice(user_input): #Make a function called 'programChoice()' that makes decisions on whether to display the help menu, start the program or quit the program based on the user input.
    if user_input == 1: #Check if the 'user_input' is 1.
        program = 's' #Make 'program' equal 's'.
    elif user_input == 2: #Check if the 'user_input' is 2.
        program = 'h' #Make 'program' equal 'h'.
    elif user_input == 3: #Check if the 'user_input' is 3.
        program = 'q' #Make 'program' equal 'q'.
    else: #Check if everything else in the 'if' statement is False.
        print('Error. Enter a Valid Command') #Display a message telling the user to enter a valid command.
        program = 'error' #Make 'program' equal 'error'.
    return program #Return 'program' to the variable it is being used

def gameInputMessage(): #Make a function called 'gameInput()' that gets an input from the user for what action they want to perform in the game when they are not doing anything else.
    print('Enter "1" to go to the wild') #Display a message telling the user to enter "W" to enter the wild.
    print('Enter "2" to go to the pokemon center and heal') #Display a message telling the user to enter "PC" to go to the pokemon center.
    print('Enter "3" to check your pokemon') #Display a message telling the user to enter a "C" to check your pokemon.
    print('Enter "4" to go to the gym and fight the other trainers (WARNING: Once you enter the gym you cannot leave!)') #Display a message telling the user to enter "G" to go to the gym.
    print('Enter "5" to quit the game and go to the main menu') #Display a message telling the user to enter 'Q' to quit the game and go to the main menu.

def getGameInput(): #Make 'getGameInput()' a function that gets the input from the user for what they want to do in the game.
    while True: #Set up a loop that repeats itself until the user enters a number 
        try:
            game_input = int(input("Enter a number: ")) #Get the input from the user
            if game_input == 1: #Check if 'game_input' is 1.
                return game_input #Return 'game_input' back to the variable it is being used in.
            elif game_input == 2: #Check if 'game_input' is 2.
                return game_input #Return 'game_input' back to the variable it is being used in.
            elif game_input == 3: #Check if 'game_input' is 3.
                return game_input #Return 'game_input' back to the variable it is being used in.
            elif game_input == 4: #Check if 'game_input' is 4.
                return game_input #Return 'game_input' back to the variable it is being used in.
            elif game_input == 5: #Check if 'game_input' is 5.
                return game_input #Return 'game_input' back to the variable it is being used in.
            else: #Check if everything else in the 'if' statement is False.
                blankLine() #Display a blank line
            break
        except ValueError: #Execute if user does not enter in a number.
            print("Error. Enter a valid command") #Tell them to enter a valid number.
            lineBreak() #Display a line of characters that separates the previous line from the next.
            gameInputMessage() #Use the 'gameInputMessage()' that displays the different options the user has in the main game.
            blankLine() #Display a blank line
    
def checkGameChoice(game_input): #Make a function called 'gameChoice()' that makes decisions for what the user wants to do in the game based on the user's input.
    if game_input == 1: #Check if 'game_input' is 1.
        game = 'w' #Make 'game' equal 'w'.
    elif game_input == 2: #Check if 'game_input' is 2.
        game = 'pc' #Make 'game' equal 'pc'.
    elif game_input == 3: #Check if 'game_input' is 3.
        game = 'c' #Make 'game' equal 'c'.
    elif game_input == 4: #Check if 'game_input' is 4.
        game = 'g' #Make 'game' equal 'g'.
    elif game_input == 5: #Check if 'game_input' is 5.
        game = 'q' #Make 'game' equal 'q'.
    else: #Check if everything else in the 'if' statement is False.
        print('Error. Ener a valid command') #Display a message telling the user to enter a valid command.
        game = 'error' #Make 'game' equal 'error'.
    return game #Return 'game' back to the variable it is being used in.

def getUserName(): #Make 'userName()' a function that gets an input for the name of the user.
    user_name = input('Please enter your name: ') #Get an input from the user for their name.
    user_name = str(user_name) #Cast 'user_name' as a string.
    return user_name #Return 'user_name' back to the variable it is being used in.


def pokemonChoice(user_name): #Make 'pokemonChoice' a function that gets the professor to explain what to do and gets an input from the user for what starting pokemon they want.
    #print ASCII of professor
    print('PROFESSOR OAK: Woah, I didn\'t see you there ' + user_name + '! I\'m the professor. You can call me Professor Oak.\
 I will be guiding you as you start your journey as a pokemon trainer.\
 Pokemon are these incredible creatures that range in size, colour, type, strength, and more!\
 Before you go, I have three pokemon you can choose from to become your loyal companion.') #Display the message that the professor gives the user.
    blankLine() #Display a blank line
    print('Now then, which pokemon would you like ' + user_name + '?') #Get the professor to explain what to do.
    print('Choices: Pikachu, Squirtle, Charmander.') #Print the different choices the user has.
    #print ASCII of pikachu, charmander, squirtle
    pokemon_input = input('Enter the name of the starting pokemon you want: ') #Get an input from the user for what they want for their starting pokemon.
    return pokemon_input #Return 'pokemon_input' back to the variable it is being used in.

def pokemonChecker(pokemon_input): #Make a function called 'pokemonChecker()' that checks if the user entered in a valid pokemon.
    checker = True #Make 'checker' True.
    while checker == True: #Set up a loop that repeats itself as long as checker is True.
        if pokemon_input == 'Pikachu' or pokemon_input == 'pikachu': #Check if the user entered 'Pikachu'.
            return pokemon_input #Return the input of the user back to the variable it is being used in the main code.
        elif pokemon_input == 'Squirtle' or pokemon_input == 'squirtle': #Check if the user entered 'Squirtle'.
            return pokemon_input #Return the input of the user back to the variable it is being used in the main code.
        elif pokemon_input == 'Charmander' or pokemon_input == 'charmander': #Check if the user entered 'Charmander'.
            return pokemon_input #Return the input of the user back to the variable it is being used in the main code.
        else: #Check if everything else in the 'if' statement is False.
             print('PROFESSOR OAK: Oops that\'s not one of the options I gave you. Please choose a Pokemon out of the options I gave you.') #Display a message telling the user to enter a valid pokemon name.
             pokemon_input = input('Enter the name of the starting pokemon you want: ') #Get an input from the user for what they want for their starting pokemon.


def pokemonChoiceDecider(pokemon_input, pokemon_list, pikachu_health, pikachu_damage, squirtle_health, squirtle_damage, charmander_health, charmander_damage): #Make a function called 'pokemonChoiceDecider()' that makes decisions for what pokemon the user wants to start with based on the user's input.
    checker = True #Make 'checker' equal True.
    while checker == True: #Set up a loop that repeats itself as long as check is True.
        if pokemon_input == 'pikachu' or pokemon_input == 'Pikachu': #Check if 'pokemon_input' is 'pikcahu' or 'Pikachu'.
            pokemon_list.append(pikachu_health) #Add 'pikachu_health' to the 'pokemon_list'.
            pokemon_list.append(pikachu_damage) #Add 'pikachu_damage' to the 'pokemon_list'.
            pokemon_list.append('Pikachu') #Add 'Pikachu' to the list.
            checker = False #Make 'checker' False.
        elif pokemon_input == 'squirtle' or pokemon_input == 'Squirtle': #Check if 'pokemon_input' is 'squirtle' or 'Squirtle'.
            pokemon_list.append(squirtle_health) #Add 'squirtle_health' to the 'pokemon_list'.
            pokemon_list.append(squirtle_damage) #Add 'squirtle_damage' to the 'pokemon_list'.
            pokemon_list.append('Squirtle') #Add 'Squirtle' to the list.
            checker = False #Make 'checker' False.
        elif pokemon_input == 'charmander' or pokemon_input == 'Charmander': #Check if 'pokemon_input' is 'charmander' or 'Charmander'.
            pokemon_list.append(charmander_health) #Add 'charmander_health' to the 'pokemon_list'.
            pokemon_list.append(charmander_damage) #Add 'charmander_damage' to the 'pokemon_list'.
            pokemon_list.append('Charmander') #Add 'Charmander' to the list.
            checker = False #Make 'checker' False.
        else: #Check if everything else in the if statement is False.
            print('Enter a valid pokemon') #Tell the user to enter a valid pokemon.
            pokemon_input = input('Enter the name of the starting pokemon you want: ') #Get an input from the user for what they want for their starting pokemon.
    return pokemon_list #Return 'pokemon_list' back to the list in the main code.


def showPokemon(pokemon_list): #Make a function called 'showPokemon()' that makes decisions for what the user wants to do in the game based on the user's input.
    print('')   #print blank line
    pikachu = pokemon_list.count('Pikachu') #Make 'pikachu' store the value of how many times 'pikachu_health' appears in the 'pokemon_list'.
    squirtle = pokemon_list.count('Squirtle') #Make 'squirtle' store the value of how many times 'squirtle_health' appears in the 'pokemon_list'.
    charmander = pokemon_list.count('Charmander') #Make 'charmander' store the value of how many times 'charmander_health' appears in the 'pokemon_list'.
    if pikachu > 0: #Check if 'pikachu' is greater than 0.
        print('--Pikachu-- ' + 'HP: ' + str(pokemon_list[0]) + ' Damage: ' + str(pokemon_list[1])) #Display the health and damage of pikachu.
        print('') #Print a blank space.
    else: #Check if the 'if' statement is False.
        nothing = True #Make 'nothing' True so that nothing happens.
    if squirtle > 0: #Check if 'squirtle' is greater than 0.
        print('--Squirtle-- ' + 'HP: ' + str(pokemon_list[0]) + ' Damage: ' + str(pokemon_list[1])) #Display the health and damage of squirtle.
        print('') #Print a blank space.
    else: #Check if the 'if' statement is False.
        nothing = True #Make 'nothing' True so that nothing happens.
    if charmander > 0: #Check if 'charmander' is greater than 0.
        print('--Charmander-- ' + 'HP: ' + str(pokemon_list[0]) + ' Damage: ' + str(pokemon_list[1])) #Display the health and damage of charmander.
        print('') #Print a blank space.
    else: #Check if the 'if' statement is False.
        nothing = True #Make 'nothing' True so that nothing happens.

def pokemonChance(): #Make 'pokemonChance()' a function that randomly chooses which pokemon will appear in the wild.
    chance = random.randint(1,3) #Make 'chance' store a random number between 1 and 3.
    if chance == 1: #Check if 'chance' is 1.
        print('A wild Pikachu has appeared!') #Tell the user that a wild Pikachu appeared.
    elif chance == 2: #Check if 'chance' is 2.
        print('A wild Squirtle has appeared!') #Tell the user that a wild Squirtle appeared.
    elif chance == 3: #Check if 'chance' is 3.
        print('A wild Charmander has appeared!') #Tell the user that a wild Charmander appeared.
    else: #Check if everything else in the 'if' statement is False.
        errorMessage() 
    return chance #Return 'chance' back to the variable it is being used in.

def nameOfPokemon(chance): #Make 'nameOfPokemon()' a function that figures out what pokemon appeared and store it in a variable in the main code.
    if chance == 1: #Check if 'chance' is 1.
        name = 'Pikachu' #Make 'name' equal 'Pikachu'.
    elif chance == 2: #Check if 'chance' is 2.
        name = 'Squirtle' #Make 'name' equal 'Squirtle'.
    elif chance == 3: #Check if 'chance' is 3.
        name = 'Charmander' #Make 'name' equal 'Charmander'.
    else: #Check if everything else in the if statement is False.
        errorMessage() #Display an error message.
    return name     #returns name of pokemon that appeared

def userPokemonName(pokemon_input): #Make 'userPokemonName()' a function that stores the name of the pokemon you chose. 
    if pokemon_input == 'Pikachu' or pokemon_input == 'pikachu': #Check if the 'pokemon_input' was Pikachu.
        pokemon_input = 'Pikachu' #Make 'pokemon_input' equal 'Pikachu'.
    elif pokemon_input == 'Squirtle' or pokemon_input == 'squirtle': #Check if the 'pokemon_input' was Squirtle.
        pokemon_input = 'Squirtle' #Make 'pokemon_input' equal 'Squirtle'.
    elif pokemon_input == 'Charmander' or pokemon_input == 'charmander':  #Check if the 'pokemon_input' was Charmander.
        pokemon_input = 'Charmander' #Make 'pokemon_input' equal 'Charmander'.
    else: #Check if everything else in the if statement is False.
        errorMessage() #Display an error message.
    return pokemon_input    #returns name of pokemon that appeared

def couldNotRunMessage(): #Make a function called 'couldNotRunMessage()' that tells the user their attempt to run away failed.
    print('Run away attempt failed!') #Display a message saying their attempt to run away failed.

def runSuccessMessage(): #Make a function called 'runSuccessMessage()' that tells the user their attempt to run away was sucessful.
    print('Run away attempt successful. You are going back to town.') #Display a message telling the user their attempt to run away was sucessful.

def wildFightMessage(): #Make 'wildFightMessage()' a function that displays the options the user has when they are fighting in the wild.
    print('')   #print blank line
    print('')   #print blank line
    print('Enter "A" to attack the pokemon') #Display a message telling the user to enter "F" to fight the pokemon.
    print('Enter "R" to run away from the wild pokemon') #Display a message telling the user to enter "R" to run away from the wild pokemon.

def wildFight(): #Make 'wildFight()' a function that gets an input from the user for what they want to do when a wild pokemon appears.
    wild_fight = input() #Get an input from the user for what action they want to do in the game.
    wild_fight = str(wild_fight) #Cast 'wild_fight' as a string.
    return wild_fight #Return 'wild_fight' back to the variable it is being used in.

def wildFightChoice(wild_fight): #Make 'wildFightChoice()' a function that makes decisions about the fight based on what the user decided to do.
    if wild_fight == 'a' or wild_fight == 'A': #Check if 'wild_fight' is uppercase or lower case 'a'.
        fight_choice = 'a' #Make 'fight_choice' equal 'a'.
    elif wild_fight == 'r' or wild_fight == 'R': #Check if 'wild_fight' is uppercase or lower case 'r'.
        fight_choice = 'r' #Make 'fight_choice' equal 'r'.
    else: #Check if everything else in the 'if' statement is False.
        print('Error. Enter a valid command') #Display a message telling the user to enter a valid command.
        fight_choice = 'error' #Make 'fight_choice' equal 'error'.
    return fight_choice #Return 'fight_choice' back to the variable it is being used in.

def generatePikachuHealth(): #Make 'generatePikachuHealth()' a function that randomly generates health for Pikachu.
    health = random.randint(33, 36) #Make 'health' equal a random number between 33 and 36. 
    return health #Return 'health' back to the variable it is being used in the main code.

def generatePikachuDamage(): #Make 'generatePikachuDamage()' a function that randomly generates damage for Pikachu.
    damage = random.randint(5,10) #Make 'damage' equal a random number between 5 and 10. 
    return damage #Return 'damage' back to the variable it is being used in the main code.

def generateSquirtleHealth(): #Make 'generateSquirtleHealth()' a function that randomly generates health for Squirtle.
    health = random.randint(40, 43) #Make 'health' equal a random number between 40 and 43. 
    return health #Return 'health' back to the variable it is being used in the main code.

def generateSquirtleDamage(): #Make 'generateCharmanderDamage()' a function that randomly generates damage for Squirtle.
    damage = random.randint(3,8) #Make 'damage' equal a random number between 3 and 8. 
    return damage #Return 'damage' back to the variable it is being used in the main code.

def generateCharmanderHealth(): #Make 'generateCharmanderHealth()' a function that randomly generates health for Charmander.
    health = random.randint(35, 38) #Make 'health' equal a random number between 35 and 38. 
    return health #Return 'health' back to the variable it is being used in the main code.

def generateCharmanderDamage(): #Make 'generateCharmanderDamage()' a function that randomly generates damage for Charmander.
    damage = random.randint(3,8) #Make 'damage' equal a random number between 3 and 8.  
    return damage #Return 'damage' back to the variable it is being used in the main code.

def showPokemonStats(pokemonName, health, damage): #Make 'showPokemonStats()' a function that shows the stats of the user's pokemon.
    print('YOUR POKEMON: --', pokemonName, '-- HP: ', str(health), ' Damage: ', str(damage)) #Show the stats of the user's pokemon.

def showWildPokemonStats(pokemonName, wild_health, wild_damage): #Make 'showWildPokemonStats()' a function that shows the stats of the enemy's pokemon.
    print('ENEMY POKEMON: --', pokemonName, '-- HP: ', str(wild_health), ' Damage: ', str(wild_damage)) #Show the stats of the enemy's pokemon.

def generateWildHealth(wild_pokemon): #Make 'generateWildHealth()' a function that generates random health of the wild pokemon based on what pokemon it is.
    if wild_pokemon == 1: #Check if 'wild_pokemon' is equal to 1.
        wild_health = generatePikachuHealth() #Make 'wild_health' store a randomly generated pikachu health.
    elif wild_pokemon == 2: #Check if 'wild_pokemon' is equal to 2.
        wild_health = generateSquirtleHealth() #Make 'wild_health' store a randomly generated squirtle health.
    elif wild_pokemon == 3: #Check if 'wild_pokemon' is equal to 3.
        wild_health = generateCharmanderHealth() #Make 'wild_health' store a randomly generated charmander health.
    else: #Check if everything else in the 'if' statement is False.
        errorMessage() #Display an error message.
    return wild_health #Return 'wild_health' back to the variable it is being used in the main code.

def generateWildDamage(wild_pokemon): #Make 'generateWildDamage()' a function that generates random damage of the wild pokemon based on what pokemon it is.
    if wild_pokemon == 1: #Check if 'wild_pokemon' is equal to 1.
        wild_damage = generatePikachuDamage() #Make 'wild_damage' store a randomly generated pikachu damage.
    elif wild_pokemon == 2: #Check if 'wild_pokemon' is equal to 2.
        wild_damage = generateSquirtleDamage() #Make 'wild_damage' store a randomly generated squirtle damage.
    elif wild_pokemon == 3: #Check if 'wild_pokemon' is equal to 3.
        wild_damage = generateSquirtleDamage() #Make 'wild_damage' store a randomly generated charmander damage.
    else: #Check if everything else in the 'if' statement is False.
        errorMessage() #Display an error message.
    return wild_damage #Return 'wild_damage' back to the variable it is being used in the main code.


def tryToRun(): #Make 'tryToRun()' a function that randomly decides if the run away attempt was sucessful.
    chance = random.randint(1, 2) #Make 'chance' equal a random whole number between 1 and 2
    if chance == 1: #Check if 'chance' is equal to 1.
        run = True #Make 'run' equal True.
    else: #Check if everything else in the 'if' statement is False.
        run = False #Make 'run' equal False.
    return run #Return 'run' back to the variable it is being used in the main code.

def userAttackMessage(pokemon_name, wild_pokemon_name): #Make 'userAttackMessage()' a function that tells the user that their pokemon attacked the enemy pokemon.
    print('Your ' + str(pokemon_name) + ' attacks the enemy ' + str(wild_pokemon_name) + '!') #Tell the user that their pokemon attacked the 

def gymMessage(): #Make 'gymMessage()' a function that displays information about the gym once the user enters the gym.
    print('You are going to the gym') #Display 'You are going to the gym'.
    print('Welcome to the gym. To beat the gym, you must win against two trainers and then the gym leader. You are not allowed to leave.') #Provide more information on the gym.
    blankLine() #Display a blank line.

def feisalMessage(): #Make 'feisalMessage()' a function that displays what feisal says the user once they enter the gym.
    print('FEISAL: Hey trainer, I challenge you to a battle! Warning, I never lose!') #Display a message telling the user that feisal challenges them to a battle.
    blankLine() #Display a blank line.
    print('************YOU ARE CHALLENGED BY POKEMON TRAINER FEISAL************') #Tell the user they are challenged by Feisal.

def feisalWinMessage(): #Make 'feisalWinMessage()' a function that displays what feisal says when he beats the user.
    print('FEISAL: I win! My mom will be so happy.') #Display what feisal says when he beats the user.

def feisalLoseMessage(): #Make 'feisalLoseMessage()' a function that displays what feisal says when he is beat by the user.
    print('FEISAL: I can\'t believe I lost... Please don\'t tell my mom!') #Display what feisal says when he is beat by the user.

def noahMessage(): #Make 'noahMessage()' a function that displays what Noah says to the user after they beat feisal.
    blankLine() #Display a blank line.
    print('NOAH: Don\'t underestimate me, I\'m WAY more skilled than Feisal. Let\'s fight!') #Display what Noah says to the user.
    blankLine() #Display a blank line.
    blankLine() #Display a blank line.
    print('************YOU ARE CHALLENGED BY POKEMON TRAINER NOAH************') #Tell the user that Noah challenged them to a battle.

def noahWinMessage(): #Make 'noahWinMessage()' a function that displays a message from Noah once he beats the user.
    print('NOAH: It\'s ok kid, maybe one day you\'ll become at least HALF as good as me.') #Display a message from Noah bragging about his win,

def noahLoseMessage(): #Make 'noahLoseMessage()' a function that displays a message from Noah once the user beats him.
    print('NOAH: You... will... pay... for... this...') #Display a message from Noah telling the user they will pay for this.

def licontiMessage(): #Make 'licontiMessage()' a function that displays once the user beats Noah.
    blankLine() #Display a blank line.
    print('MR. LICONTI: Hmmm... I see you\'ve defeated the two trainers here. \
Those guys are a piece of cake, I\'m the real deal. My name is Mr. Liconti, and \
I\'m the gym leader. If you can beat me, you will become a master pokemon trainer. \
Now then, trainer, I challenge you for a final duel!') #Display a message from Liconti challenging the user to a battle.
    blankLine() #Display a blank line.
    blankLine() #Display a blank line.
    print('************YOU ARE CHALLENGED BY GYM LEADER MR. LICONTI************') #Tell the user that Liconti challenged them to a battle.

def licontiWinMessage(): #Make 'licontiWinMessage()' a function that displays a message from Liconti once he beats the user.
    print('MR. LICONTI: You still require training young one, you need to take it one \
step at a time. I\'ll give you a random piece of advice for your journey: Multitasking is a myth! \
Use it how you wish.') #Display a message from Liconti bragging about his win.

def licontiLoseMessage(): #Make 'licontiLoseMessage()' a function that displays a message from Liconti once the user beats him.
    print('MR. LICONTI: You\'ve come a long way trainer, your power grows strong... \
Congratulations, you\'ve defeated me and earned your title as a master pokemon trainer! Well done.') #Display a message from Liconti congratulating the user about their win.

def runAwayMessage(): #Make 'runAwayMessage()' a function that tells the user that they tried to run away.
    print('You tried to run away.') #Display a message telling the user they tried to run away.

def stayInWildMessage(): #Make 'stayInWildMessage()' a function that tells the user they are going to the wild.
    print('You are making your way to the wild') #Tell the user they are going to the wild.

def gameLoseMessage(): #Make a function called 'gameLoseMessage()' 
    blankLine() #Display a blank line.
    print('You Lost. Would you like to play again?') #Tell the user they lost and ask the user if they want to play
    blankLine() #Display a blank line.

def fightWinMessage(): #Make 'fightWinMessage()' a function that tells the user they won a fight in the wild.
    print('You Won! Your Pokemon\'s health increased by 10 and its damage increased by 1.') #Display a message telling the user that they won so their pokemon's health increased by 10 and their damage increased by 1.

def enemyAttackMessage(): #Make a function called 'enemyAttackMessage()' that tells the user that the enemy attacked them.
    print('The enemy attacks you.') #Display a message telling the user that they enemy attacked you

def beatFeisalMessage(): #Make 'beatFeisalMessage()' a function that tells the user that they beat feisal.
    blankLine() #Display a blank line.
    print('************YOU HAVE DEFEATED POKEMON TRAINER FEISAL************')

def lostToFeisalMessage(): #Make 'lostToFeisalMessage()' a function that tells the user that they lost to feisal.
    blankLine() #Display a blank line.
    print('************YOU HAVE BEEN DEFEATED BY POKEMON TRAINER FEISAL************') #Tell the user that they were defeated by feisal.

def beatNoahMessage(): #Make 'beatNoahMessage()' a function that tells the user that they beat Noah.
    blankLine() #Display a blank line.
    print('************YOU HAVE DEFEATED POKEMON TRAINER NOAH************') #Tell the user that they defeated Noah.

def lostToNoahMessage(): #Make 'lostToNoahMessage()' a function that tells the user that they lost to Noah.
    blankLine() #Display a blank line.
    print('************YOU HAVE BEEN DEFEATED BY POKEMON TRAINER NOAH************') #Tell the user that they were defeated by Noah.

def beatLicontiMessage(): #Make 'beatLicontiMessage()' a function that tells the user that they beat Liconti.
    blankLine() #Display a blank line.
    print('************YOU HAVE DEFEATED GYM LEADER LICONTI************') #Tell the user that they defeated Liconti.

def lostToLicontiMessage(): #Make 'lostToLicontiMessage()' a function that tells the user that they lost to Liconti.
    blankLine() #Display a blank line.
    print('************YOU HAVE BEEN DEFEATED BY GYM LEADER LICONTI************') #Tell the user that they were defeated by Liconti.

def gameWinMessage(): #Make 'gameWinMessage()' a function that tells the user they won the entire game.
    print('You have won the game! You could play again if you wish. What would you like to do?') #Tell the user they won the entired game and ask what they wanna do next.

def quitGameMessage(): #Make 'quitGameMessage()' a function a telling the user they are quitting the game.
    print('Quitting Game')  #Tell the user they are quitting the game.

def professorMessage(): #Make 'professorMessage()' a function that displays final instructions from the professor
    print('PROFESSOR OAK: Now you have your very own pokemon! You can fight enemies in the wild to make your pokemon \
stronger. Once you think you\'re ready, you can try to beat the gym and earn your title as a master trainer. Be wary \
though, you must protect that pokemon with your life. Now then, best of luck on your journey!') #prints professor's message

def gymFightMessage():  #Make 'gymFightMessage()' a function that prompts the user to attack during a gym fight
    print('Enter "a" to attack')    #prints message

def showPokemonArt(pokemon_name, pikachu, squirtle, charmander): #Show the ASCII art of the pokemon.
    if pokemon_name == 'Pikachu': #Check if 'pokemon_name' is 'Pikachu.
        print(pikachu) #Display the ASCII art of pikachu.
    elif pokemon_name == 'Squirtle': #Check if 'pokemon_name' is 'Squirtle.
        print(squirtle) #Display the ASCII art of squirtle.
    elif pokemon_name == 'Charmander': #Check if 'pokemon_name' is 'Charmander.
        print(charmander) #Display the ASCII art of charmander.
    else: #Check if everything else in the 'if' statement is False.
        errorMessage() #Display an error message.

def blankLine(): #Make 'blankLine()' a function that displays a blank line.
    print('')   #print blank line

def pokemonCenterMessage(): #Make 'pokemonCenterMessage()' a function that tells the user that they are going to the pokemon center.
    print('You are going to the pokemon center') #Dislay a message telling the user they are going to the pokemon center.

def pokemonHealedMessage(user_pokemon_name):    #make 'pokemonHealedMessage()' a function that indicates user pokemon has been healed
    print('Your ' + user_pokemon_name + ' has been healed!')    #prints healed message

def checkPokemonMessage():
    print('You are checking your pokemon') #Display 'you are checking your pokemon'.

def lineBreak(): #Make 'lineBreak()' a function that displays a line of characters that separates the previous line from the next.
    print('--------------------------------------------------------------------------------------------------------')

def pikachuDrawing(): #Make 'pikachuDrawing()' a function that displays the ASCII art drawing of pikachu.
    pikachu = '''
                       
                                             ,-.
                                          _.|  '
                       ---PIKACHU---    .'  | /
                                      ,'    |'
                                     /      /
                       _..----""---.'      /
 _.....---------...,-""                  ,'
 `-._  \\                                /
     `-.+_            __           ,--. .
          `-.._     .:  ).        (`--"| \\
               7    | `" |         `...'  \\
               |     `--'     '+"        ,". ,""-
               |   _...        .____     | |/    '
          _.   |  .    `.  '--"   /      `./     j
         \\' `-.|  '     |   `.   /        /     /
         '     `-. `---"      `-"        /     /
          \       `.                  _,'     /
           \        `                        .
            \                                j
             \                              /
              `.                           .
                +                          \\
                |                           L
                |                           |
                |  _ /,                     |
                | | L)'..                   |
                | .    | `                  |
                '  \\'   L                   '
                 \\  \\   |                  j
                  `. `__'                 /
                _,.--.---........__      /
               ---.,'---`         |   -j"
                .-'  '....__      L    |
              ""--..    _,-'       \ l||
                  ,-'  .....------. `||'
               _,'                /
             ,'                  /
            '---------+-        /
                     /         /
                   .'         /
                 .'          /
               ,'           /
             _'....----""\"\"" 
'''
    return pikachu #Return the ASCII art back to the variable it is being used in.

def squirtleDrawing(): #Make 'squirtleDrawing()' a function that displays the ASCII art drawing of squirtle.
    squirtle = """
              ---SQUIRTLE---
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \\
      ,'                           .
      .'\\               ,"".       `
     ._.'|             / |  `       \\
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \\
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \\  .     `
`.""\""\"'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\\          \\  \\     \\
\\_ .          |   `""\""'    `.           . \\     \\
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"\""`-.
             \\ `.     .          /      |  '      |  ,'          `.
              \\  v.__  .        '       .   \\    /| /              \\
               \\/    `""\"""""""`.       \\   \\  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \\         ."     `.  |/        j     `    |
               /    `.     \\       /         \\ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \\          \\      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'
"""
    return squirtle #Return the ASCII art back to the variable it is being used in.

def charmanderDrawing(): #Make 'charmanderDrawing()' a function that displays the ASCII art drawing of charmander.
    charmander = """
           ---CHARMANDER---
                       _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \\
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \\ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         ""\""'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\\                .      |
           |                '     \\                `._  ,'
           |                 '     \\                 .'|
           |                 .      \\                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \\                |       |           ,'   /
          ,' \\               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'---""\\"\""'        `' '! |! /
                            `" " -'
                            """
    return charmander #Return the ASCII art back to the variable it is being used in.

def bulbasaurDrawing(): #Make 'bulbasaurDrawing()' a function that displays the ASCII art drawing of bulbasaur.
    bulbasaur = """
                   
                    ---BULBASAUR---        /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \\.\\
       ____      |___._.  |       __               \\ `.
     .'    `---""       ``"-.--"'`  \\               .  \\
    .  ,            __               `              |   .
    `,'         ,-"'  .               \\             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  ""\"\""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \\`._        ___....----"'  ,'   .'  \\ |   '  \\  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''""\""\"`.,^.`.--' 


 """
    return bulbasaur #Return the ASCII art back to the variable it is being used in.

def pidgeyDrawing(): #Make 'pidgeyDrawing()' a function that displays the ASCII art drawing of pidgey.
    pidgey = """
           ---PIDGEY---
                   .,
            , _.-','
          ""|"    `""\\"".,
         /'/       __.-'-"/
        ','  _,--""      '-._
    _...`...'.""\""\"".\""-----'
 ,-'          `-.) /  `.  \\
+---."-.    |     `.    .  \\
     \  `.  |       \\   |   L
      `v  ,-j        , .'   |
     .'\\,' /        /,'      -._
    ,____.'        .            `-.
        |         /                `-.
       /          `.                  `-.
      /             `. |                 `.                  _.
     .                `|                 ,-.             _.-" .
    j                  |                 |  \\         _.'    /
    .                  |               .'    \\     ,-'      /
    |                  |            ,-.\\      \\  ,'      _.-
    |                . '  `.       |   `      `v'  _,.-"/
    ||    \          |  ` |(`'-`.,.j         \\ `.-'----+---.
    |'|   |L    \  | |   `|   \'              L \\___      /
    ' L   |`     L | |     `.                 | j   `"\""-'
       `-'||\\    | ||j       `.       ._    ` '.
          `\ '"`^"- '          `.       \\    |/|
            `._                  `-.     \\   Y |
    __,..-""`..`._                  `-._  `\\ `.|
   +.....>+----.' ""----.........,--"\"" `--.'.'
       ,' _\\  ,..--.-"' __>---'  |
      --""  "'  _." }<""          `---""`._
               /..."  L__.+--   _,......'..'
                 /.-""'/   \\ ,-'
                     .' ,-""'
                    /.-' 
    """
    return pidgey #Return the ASCII art back to the variable it is being used in.

def gengarDrawing(): #Make 'gengarDrawing()' a function that displays the ASCII art drawing of gengar.
    gengar = """
                             ---GENGAR---
                 |`._         |\\
                 `   `.  .    | `.    |`.
                  .    `.|`-. |   `-..'  \\           _,.-'
                  '      `-. `.           \\ /|   _,-'   /
              .--..'        `._`           ` |.-'      /
               \\   |                                  /
            ,..'   '                                 /
            `.                                      /
            _`.---                                 /
        _,-'               `.                 ,-  /"-._
      ,"                   | `.             ,'|   `    `.
    .'                     |   `.         .'  |    .     `.
  ,'                       '   ()`.     ,'()  '    |       `.
'-.                    |`.  `.....-'    -----' _   |         .
 / ,   ________..'     '  `-._              _.'/   |         :
 ` '-"" _,.--"'         \   | `"+--......-+' //   j `"--.. , '
    `.'"    .'           `. |   |     |   / //    .       ` '
      `.   /               `'   |    j   /,.'     '
        \ /                  `-.|_   |_.-'       /\\
         /                        `""          .'  \\
        j                                           .
        |                                 _,        |
        |             ,^._            _.-"          '
        |          _.'    `'""`----`"'   `._       '
        j__     _,'                         `-.'-."`
          ',-.,' 
    """
    return gengar #Return the ASCII art back to the variable it is being used in.

def pokemonLogo(): #Make 'pokemonLogo()' a function that displays the ASCII art of the pokemon logo.
    pokemon = """
                                  ,'\\
    _.----.        ____         ,'  _\\   ___    ___     ____
_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.
\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |
 \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |
   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |
     \\    \\ |   \_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |
      \\    \\ \\      /       `-.`.___,-' |  |\\  /| \      /  | |   |
       \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |
        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
"""
    return pokemon #Return the ASCII art back to the variable it is being used in.


pikachu = pikachuDrawing() #Make 'pikachu' store the ASCII art drawing of Pikachu.
pikachu_health = generatePikachuHealth() #Generate a random health for the user's pokemon.
pikachu_damage = generatePikachuDamage() #Generate a random damage for the user's pokemon.

squirtle = squirtleDrawing() #Make 'pikachu' store the ASCII art drawing of Squirtle.
squirtle_health = generateSquirtleHealth() #Generate a random health for the user's pokemon.
squirtle_damage = generateSquirtleDamage() #Generate a random damage for the user's pokemon.

charmander = charmanderDrawing() #Make 'pikachu' store the ASCII art drawing of Charmander. 
charmander_health = generateCharmanderHealth() #Generate a random health for the user's pokemon.
charmander_damage = generateSquirtleDamage() #Generate a random damage for the user's pokemon.

bulbasaur = bulbasaurDrawing()  #store bulbasaur ASCII
pidgey = pidgeyDrawing()    #store pidgey ASCII
gengar = gengarDrawing()    #store gengar ASCII

pokemon_logo = pokemonLogo()    #store pokemon logo ASCII

fight = True        #initialize variable that will control game loop
second_flag = True  #initialize second flag to True
encounter = True    #initiialize encounter to True
wild = True         #initialize wild to True
fight_win = False   #initializes first gym fight result flag
fight2_win = False  #initializes second gym fight result flag
fight3_win = False  #initializes last gym fight result flag

total_pokemon_health = 0    #initialize total pokemon's health to 0
pokemon_list = []   #Make an empty list for the user's pokemon's damage and health
pokemon_health = 0  #initialize starting pokemon's health to 0
pokemon_damage = 0  #initialize starting pokemon's damage to 0


print(pokemon_logo) #Display the pokemon logo in ASCII art.
programInputMessage() #Tell the user the different program options.
start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.

flag = True #Make 'flag' True.
while flag == True: #Setup a loop that repeats itself as long as 'flag' is True.
    if program == 's' or program == 'S': #Check if 'program' is 's' from the 'programChoice()' function.
        pikachu_health = generatePikachuHealth() #Generate a random health for the user's pokemon.
        pikachu_damage = generatePikachuDamage() #Generate a random damage for the user's pokemon.
        squirtle_health = generateSquirtleHealth() #Generate a random health for the user's pokemon.
        squirtle_damage = generateSquirtleDamage() #Generate a random damage for the user's pokemon.
        charmander_health = generateCharmanderHealth() #Generate a random health for the user's pokemon.
        charmander_damage = generateSquirtleDamage() #Generate a random damage for the user's pokemon.
        pokemon_list.clear() #Clear 'pokemon_list' so that no pokemon from the previous game you played are in it.
        user_name = getUserName() #Make 'user_name' equal the function 'userName()' that gets an input from the user for their name and store it in the variable 'user_name'.
        blankLine() #Display a blank line
        pokemon_input = pokemonChoice(user_name) #Make 'pokemon_input' a variable that holds the command for what pokemon the user wants to start with.
        pokemon_input = pokemonChecker(pokemon_input) #Make sure the user inputted a valid pokemon.
        pokemon_list = pokemonChoiceDecider(pokemon_input, pokemon_list, pikachu_health, pikachu_damage, squirtle_health, squirtle_damage, charmander_health, charmander_damage) #Use the function 'pokemonChoiceDecider()' to add the starting pokemon to 'pokemon_list'.
        user_pokemon_name = userPokemonName(pokemon_input) #Hold the user's pokemon name in the variable 'user_pokemon_name'.
        blankLine() #Display a blank line
        showPokemonArt(user_pokemon_name, pikachu, squirtle, charmander) #Show the drawing of the pokemon the user chose in ASCII art.
        blankLine() #Display a blank line
        showPokemonStats(user_pokemon_name, pokemon_list[0], pokemon_list[1]) #Use showPokemonStats function to show the pokemon stats
        blankLine() #Display a blank line
        professorMessage()  #Prints final message from the professor
        blankLine() #Display a blank line
        pokemon_health = pokemon_list[0] #Make 'pokemon_health' equal position zero in the list.
        pokemon_damage = pokemon_list[1] #Make 'pokemon_damage' equal position one in the list.
        total_pokemon_health = pokemon_list[0] #Make 'total_pokemon_health' equal the first position in the list.
        lineBreak() #Display a line of characters that separates the previous line from the next.
        gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
        game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
        game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
        second_flag = True

        while second_flag == True: #Set up a loop that repeats itself as long as 'second_flag' is True.
            if game == 'w': #Check if 'game' is equal to 'w'.
                lineBreak() #Display a line of characters that separates the previous line from the next.
                wild_choice = 'w' #Check if 'wild_choice' is 'w'.
                wild = True #Make 'wild' True.
                while wild == True: #Set up a loop that repeats itself as long as 'wild' is True.
                    if wild_choice == 'w': #Check if 'wild_choice' is equal to 'w'.
                        blankLine() #Display a blank line
                        blankLine() #Display a blank line
                        stayInWildMessage() #Tell the user they are going to the wild.
                        wild_pokemon = pokemonChance() #Randomly choose which pokemon appeared.
                        wild_pokemon_name = nameOfPokemon(wild_pokemon) #Make 'wild_pokemon_name' store the name of the wild pokemon.
                        wild_health = generateWildHealth(wild_pokemon) #Generate a random number for the wild pokemon's health.
                        wild_damage = generateWildDamage(wild_pokemon) #Generate a random number for the wild pokemon's damage.
                        showPokemonArt(wild_pokemon_name, pikachu, squirtle, charmander) #Show the ASCII art of the wild pokemon.
                        showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the wild pokemon.
                        wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                        wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                        fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                        encounter = True #Make 'encounter' True.
                        while encounter == True: #Set up a loop that repeats itself as long as encounter is True.
                            if fight_choice == 'a': #Check if 'fight_choice' is True.
                                if wild_pokemon == 1: #Check if 'wild_pokemon' is 1.
                                    blankLine() #Display a blank line
                                    wild_pokemon_name = 'Pikachu' #Make the 'wild_pokemon_name' store the name 'Pikachu'.
                                    userAttackMessage(user_pokemon_name, wild_pokemon_name) #Tell the user that their pokemon attacked the enemy's pokemon.             
                                    wild_health = wild_health - pokemon_damage #Subtract 'wild_health' by the user's pokemon's damage.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    enemyAttackMessage() #Tell the user that the enemy attacked their pokemon.
                                    wild_damage = generateWildDamage(wild_pokemon)
                                    pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                    pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                        fight = False #Make 'fight' False.
                                        encounter = False #Make 'encounter' False.
                                        wild = False #Make 'wild' False.
                                        second_flag = False #Make 'second_flag' False.
                                        blankLine() #Display a blank line
                                        gameLoseMessage() #Display a message telling the user that they lost the game
                                        blankLine() #Display a blank line
                                        lineBreak() #Display a line of characters that separates the previous line from the next.
                                        print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                        programInputMessage() #Tell the user the different program options.
                                        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                        program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                    else: #Check if the previous 'if' statement is False.
                                        fight = True #Make 'fight' True.
                                        wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                        wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                        fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                    
                                    while fight == True: #Set up a loop that repeats itself as long as 'fight' is True.
                                        if fight_choice == 'r': #Check if 'fight_choice' is 'r'.
                                            runAwayMessage() #Tell the user they tried to run away.
                                            run = tryToRun() #Make 'run' hold True or False to decide if the user's attempt to run away was sucessful.
                                            if run == True: #Check if 'run' is True.
                                                fight = False #Make 'fight' False.
                                                runSuccessMessage() #Tell the user their attempt to run away was sucessful.
                                                blankLine() #Display a blank line
                                                lineBreak() #Display a line of characters that separates the previous line from the next.
                                                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                            elif run == False: #Check if 'run' is False.
                                                couldNotRunMessage() #Tell the user their attempt to run was unsucessful.
                                                blankLine() #Display a blank line
                                                enemyAttackMessage() #Tell the user the enemy attacked their pokemon.
                                                wild_damage = generateWildDamage(wild_pokemon)
                                                pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                                pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.          
                                                if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                                    fight = False #Make 'fight' False.
                                                    encounter = False #Make 'encounter' False.
                                                    wild = False #Make 'wild' False.
                                                    second_flag = False #Make 'second_flag' False.
                                                    blankLine() #Display a blank line
                                                    gameLoseMessage() #Tell the user they lost the game.
                                                    blankLine() #Display a blank line
                                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                                    programInputMessage() #Tell the user the different program options.
                                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                                else: #Check if the previous 'if' statement is False.
                                                    wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                                    wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                                    fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                            else: #Check if the previous 'if' statements are False.
                                                errorMessage() #Display an errorMessage()
                                            
                                        elif fight_choice == 'a': #Check if 'fight_choice' is 'a'.
                                            userAttackMessage(user_pokemon_name, wild_pokemon_name) #Tell the user that they attacked the enemy pokemon.         
                                            wild_health = wild_health - pokemon_damage #Subtract 'wild_health' by the user's pokemon's damage.
                                            showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.          
                                            showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon. 
                                            if wild_health <= 0: #Check if 'wild_health' is less than or equal to 0.
                                                fight = False #Make 'fight' False.
                                                encounter = False #Make 'encounter' False.
                                                wild = False #Make 'wild' False.
                                                total_pokemon_health = total_pokemon_health + 10 #Add 10 to the 'total_pokemon_health'.
                                                pokemon_damage = pokemon_damage + 1 #Add 1 to the 'pokemon_damage'
                                                pokemon_list[1] = pokemon_damage #Make the second position in the list equal 'pokemon_damage'.
                                                blankLine() #Display a blank line
                                                fightWinMessage() #Display a message telling the user they won the fight.
                                                blankLine() #Display a blank line
                                                blankLine() #Display a blank line
                                                lineBreak() #Display a line of characters that separates the previous line from the next.
                                                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                            else: #Check if the previous 'if' statement is False.
                                                enemyAttackMessage() #Tell the uer the enemy attacked their pokemon.
                                                wild_damage = generateWildDamage(wild_pokemon)
                                                pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                                pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.           
                                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the wild pokemon.
                                                if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                                    fight = False #Make 'fight' False.
                                                    encounter = False #Make 'encounter' False.
                                                    wild = False #Make 'wild' False.
                                                    second_flag = False #Make 'second_flag' equal False.
                                                    blankLine() #Display a blank line
                                                    gameLoseMessage() #Display a message telling the user that they lost the game.
                                                    blankLine() #Display a blank line
                                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                                    programInputMessage() #Tell the user the different program options.
                                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.

                                                else: #Check if the previous if statement is False.
                                                    wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                                    wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                                    fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                        else: #Check if the previous 'if' statement is False.
                                            wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                            wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                            fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.

                                    encounter = False #Make 'encounter' False.
                                    wild = False #Make 'wild' False.

                                        
                                elif wild_pokemon == 2: #Check if 'wild_pokemon' is 2.
                                    blankLine() #Display a blank line
                                    wild_pokemon_name = 'Squirtle' #Make 'wild_pokemon_name' equal 'Squirtle'.
                                    userAttackMessage(user_pokemon_name, wild_pokemon_name) #Tell the user that their pokemon attacked the enemy's pokemon.             
                                    wild_health = wild_health - pokemon_damage #Subtract 'wild_health' by the user's pokemon's damage.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    enemyAttackMessage() #Tell the user that the enemy attacked their pokemon.
                                    wild_damage = generateWildDamage(wild_pokemon)
                                    pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                    pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                        fight = False #Make 'fight' False.
                                        encounter = False #Make 'encounter' False.
                                        wild = False #Make 'wild' False.
                                        second_flag = False #Make 'second_flag' False.
                                        blankLine() #Display a blank line
                                        gameLoseMessage() #Display a message telling the user that they lost the game
                                        blankLine() #Display a blank line
                                        lineBreak() #Display a line of characters that separates the previous line from the next.
                                        print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                        programInputMessage() #Tell the user the different program options.
                                        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                        program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                    else: #Check if the previous 'if' statement is False.
                                        fight = True #Make 'fight' True.
                                        wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                        wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                        fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                    
                                    while fight == True: #Set up a loop that repeats itself as long as 'fight' is True.
                                        if fight_choice == 'r': #Check if 'fight_choice' is 'r'.
                                            runAwayMessage() #Tell the user they tried to run away.
                                            run = tryToRun() #Make 'run' hold True or False to decide if the user's attempt to run away was sucessful.
                                            if run == True: #Check if 'run' is True.
                                                fight = False #Make 'fight' False.
                                                runSuccessMessage() #Tell the user their attempt to run away was sucessful.
                                                blankLine() #Display a blank line
                                                lineBreak() #Display a line of characters that separates the previous line from the next.
                                                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                            elif run == False: #Check if 'run' is False.
                                                couldNotRunMessage() #Tell the user their attempt to run was unsucessful.
                                                blankLine() #Display a blank line
                                                enemyAttackMessage() #Tell the user the enemy attacked their pokemon.
                                                wild_damage = generateWildDamage(wild_pokemon)
                                                pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                                pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.          
                                                if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                                    fight = False #Make 'fight' False.
                                                    encounter = False #Make 'encounter' False.
                                                    wild = False #Make 'wild' False.
                                                    second_flag = False #Make 'second_flag' False.
                                                    blankLine() #Display a blank line
                                                    gameLoseMessage() #Tell the user they lost the game.
                                                    blankLine() #Display a blank line
                                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                                    programInputMessage() #Tell the user the different program options.
                                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                                else: #Check if the previous 'if' statement is False.
                                                    wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                                    wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                                    fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                            else: #Check if the previous 'if' statements are False.
                                                errorMessage() #Display an errorMessage()
                                            
                                        elif fight_choice == 'a': #Check if 'fight_choice' is 'a'.
                                            userAttackMessage(user_pokemon_name, wild_pokemon_name) #Tell the user that they attacked the enemy pokemon.         
                                            wild_health = wild_health - pokemon_damage #Subtract 'wild_health' by the user's pokemon's damage.
                                            showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.          
                                            showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon. 
                                            if wild_health <= 0: #Check if 'wild_health' is less than or equal to 0.
                                                fight = False #Make 'fight' False.
                                                encounter = False #Make 'encounter' False.
                                                wild = False #Make 'wild' False.
                                                total_pokemon_health = total_pokemon_health + 10 #Add 10 to the 'total_pokemon_health'.
                                                pokemon_damage = pokemon_damage + 1 #Add 1 to the 'pokemon_damage'
                                                pokemon_list[1] = pokemon_damage #Make the second position in the list equal 'pokemon_damage'.
                                                blankLine() #Display a blank line
                                                fightWinMessage() #Display a message telling the user they won the fight.
                                                blankLine() #Display a blank line
                                                blankLine() #Display a blank line
                                                lineBreak() #Display a line of characters that separates the previous line from the next.
                                                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                            else: #Check if the previous 'if' statement is False.
                                                enemyAttackMessage() #Tell the uer the enemy attacked their pokemon.
                                                wild_damage = generateWildDamage(wild_pokemon)
                                                pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                                pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.           
                                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the wild pokemon.
                                                if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                                    fight = False #Make 'fight' False.
                                                    encounter = False #Make 'encounter' False.
                                                    wild = False #Make 'wild' False.
                                                    second_flag = False #Make 'second_flag' equal False.
                                                    blankLine() #Display a blank line
                                                    gameLoseMessage() #Display a message telling the user that they lost the game.
                                                    blankLine() #Display a blank line
                                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                                    programInputMessage() #Tell the user the different program options.
                                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.

                                                else: #Check if the previous if statement is False.
                                                    wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                                    wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                                    fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                        else: #Check if the previous 'if' statement is False.
                                            wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                            wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                            fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.

                                    encounter = False #Make 'encounter' False.
                                    wild = False #Make 'wild' False.
                                        
                                elif wild_pokemon == 3: #Check if 'wild_pokemon' is 3.
                                    blankLine() #Display a blank line
                                    wild_pokemon_name = 'Charmander' #Make 'wild_pokemon_name' equal 'Charmander'.
                                    userAttackMessage(user_pokemon_name, wild_pokemon_name) #Tell the user that their pokemon attacked the enemy's pokemon.             
                                    wild_health = wild_health - pokemon_damage #Subtract 'wild_health' by the user's pokemon's damage.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    enemyAttackMessage() #Tell the user that the enemy attacked their pokemon.
                                    wild_damage = generateWildDamage(wild_pokemon)
                                    pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                    pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                        fight = False #Make 'fight' False.
                                        encounter = False #Make 'encounter' False.
                                        wild = False #Make 'wild' False.
                                        second_flag = False #Make 'second_flag' False.
                                        blankLine() #Display a blank line
                                        gameLoseMessage() #Display a message telling the user that they lost the game
                                        blankLine() #Display a blank line
                                        lineBreak() #Display a line of characters that separates the previous line from the next.
                                        print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                        programInputMessage() #Tell the user the different program options.
                                        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                        program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                    else: #Check if the previous 'if' statement is False.
                                        fight = True #Make 'fight' True.
                                        wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                        wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                        fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                    
                                    while fight == True: #Set up a loop that repeats itself as long as 'fight' is True.
                                        if fight_choice == 'r': #Check if 'fight_choice' is 'r'.
                                            runAwayMessage() #Tell the user they tried to run away.
                                            run = tryToRun() #Make 'run' hold True or False to decide if the user's attempt to run away was sucessful.
                                            if run == True: #Check if 'run' is True.
                                                fight = False #Make 'fight' False.
                                                runSuccessMessage() #Tell the user their attempt to run away was sucessful.
                                                blankLine() #Display a blank line
                                                lineBreak() #Display a line of characters that separates the previous line from the next.
                                                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                            elif run == False: #Check if 'run' is False.
                                                couldNotRunMessage() #Tell the user their attempt to run was unsucessful.
                                                blankLine() #Display a blank line
                                                enemyAttackMessage() #Tell the user the enemy attacked their pokemon.
                                                wild_damage = generateWildDamage(wild_pokemon)
                                                pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                                pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.          
                                                if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                                    fight = False #Make 'fight' False.
                                                    encounter = False #Make 'encounter' False.
                                                    wild = False #Make 'wild' False.
                                                    second_flag = False #Make 'second_flag' False.
                                                    blankLine() #Display a blank line
                                                    gameLoseMessage() #Tell the user they lost the game.
                                                    blankLine() #Display a blank line
                                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                                    programInputMessage() #Tell the user the different program options.
                                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                                else: #Check if the previous 'if' statement is False.
                                                    wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                                    wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                                    fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                            else: #Check if the previous 'if' statements are False.
                                                errorMessage() #Display an errorMessage()
                                            
                                        elif fight_choice == 'a': #Check if 'fight_choice' is 'a'.
                                            userAttackMessage(user_pokemon_name, wild_pokemon_name) #Tell the user that they attacked the enemy pokemon.         
                                            wild_health = wild_health - pokemon_damage #Subtract 'wild_health' by the user's pokemon's damage.
                                            showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.          
                                            showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon. 
                                            if wild_health <= 0: #Check if 'wild_health' is less than or equal to 0.
                                                fight = False #Make 'fight' False.
                                                encounter = False #Make 'encounter' False.
                                                wild = False #Make 'wild' False.
                                                total_pokemon_health = total_pokemon_health + 10 #Add 10 to the 'total_pokemon_health'.
                                                pokemon_damage = pokemon_damage + 1 #Add 1 to the 'pokemon_damage'
                                                pokemon_list[1] = pokemon_damage #Make the second position in the list equal 'pokemon_damage'.
                                                blankLine() #Display a blank line
                                                fightWinMessage() #Display a message telling the user they won the fight.
                                                blankLine() #Display a blank line
                                                blankLine() #Display a blank line
                                                lineBreak() #Display a line of characters that separates the previous line from the next.
                                                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                            else: #Check if the previous 'if' statement is False.
                                                enemyAttackMessage() #Tell the uer the enemy attacked their pokemon.
                                                wild_damage = generateWildDamage(wild_pokemon)
                                                pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                                pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.           
                                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the wild pokemon.
                                                if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                                    fight = False #Make 'fight' False.
                                                    encounter = False #Make 'encounter' False.
                                                    wild = False #Make 'wild' False.
                                                    second_flag = False #Make 'second_flag' equal False.
                                                    blankLine() #Display a blank line
                                                    gameLoseMessage() #Display a message telling the user that they lost the game.
                                                    blankLine() #Display a blank line
                                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                                    programInputMessage() #Tell the user the different program options.
                                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.

                                                else: #Check if the previous if statement is False.
                                                    wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                                    wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                                    fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                        else: #Check if the previous 'if' statement is False.
                                            wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                            wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                            fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.

                                    encounter = False #Make 'encounter' False.
                                    wild = False #Make 'wild' False.

                            elif fight_choice == 'r': #Check if 'fight_choice' is 'r'.
                                runAwayMessage() #Tell the user they tried to run away.
                                run = tryToRun() #Make 'run' hold True or False to decide if the user's attempt to run away was sucessful.
                                if run == True: #Check if 'run' is True.
                                    wild = False #Make 'wild' False.
                                    encounter = False #Make 'encounter' False.
                                    runSuccessMessage() #Tell the user that their attempt to run was sucessful.
                                    blankLine() #Display a blank line.
                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                    gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                                    game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                                    game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                                elif run == False: #Check if 'run' is False.
                                    couldNotRunMessage() #Tell the user their attempt to run was unsucessful.
                                    blankLine() #Display a blank line
                                    enemyAttackMessage() #Tell the user the enemy attacked their pokemon.
                                    pokemon_health = pokemon_health - wild_damage #Subtract 'pokemon_health' by the wild pokemon's damage.
                                    pokemon_list[0] = pokemon_health #Make the first position in the list equal 'pokemon_health'.
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #Show the stats of the user's pokemon.
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage) #Show the stats of the enemy pokemon.
                                    if pokemon_health <= 0: #Check if 'pokemon_health' is less than or equal to zero.
                                        fight = False #Make 'fight' False.
                                        encounter = False #Make 'encounter' False.
                                        second_flag = False #Make 'second_flag' False.
                                        blankLine() #Display a blank line
                                        gameLoseMessage() #Tell the user they lost the game.
                                        blankLine() #Display a blank line
                                        lineBreak() #Display a line of characters that separates the previous line from the next.
                                        print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                        programInputMessage() #Tell the user the different program options.
                                        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                        program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                    else: #Check if the previous 'if' statement is False.
                                        wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                        wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                        fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                            else: #Check if he previous 'if' statements are False.
                                wildFightMessage() #Show all the options the user has once they encounter and are fighting with the wild pokemon.
                                wild_fight = wildFight() #Make 'wild_fight' store the choice of the user for if they want to attack the wild pokemon or run from it.
                                fight_choice = wildFightChoice(wild_fight) #Decide what to do based on what the user chose to do.
                                          
                    else: #Check if everything else in the if statement is False.
                        errorMessage() #Display a message saying 'This should not happen'.
                        
            elif game == 'pc': #Check if 'game' is equal to 'pc'.
                blankLine() #Display a blank line
                lineBreak() #Display a line of characters that separates the previous line from the next.
                pokemonCenterMessage() #Tell the user they are going to the pokemon center.
                pokemon_list[0] = total_pokemon_health #Make the first position in the list equal the total pokemon health.
                pokemon_health = pokemon_list[0] #Make 'pokemon_health' equal the first position in the list.
                showPokemonArt(user_pokemon_name, pikachu, squirtle, charmander) #Show the drawing of the pokemon the user chose in ASCII art.
                showPokemon(pokemon_list) #Show the health and damage of the user's pokemon.
                pokemonHealedMessage(user_pokemon_name) #Tell the user that their pokemon has been healed.
                blankLine() #Display a blank line.
                lineBreak() #Display a line of characters that separates the previous line from the next.
                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                
            elif game == 'c': #Check if 'game' is equal to 'c'.
                blankLine() #Display a blank line
                lineBreak() #Display a line of characters that separates the previous line from the next.
                checkPokemonMessage() #Tell the user they are checking their pokemon.
                blankLine() #Display a blank line.
                showPokemonArt(user_pokemon_name, pikachu, squirtle, charmander) #Show the drawing of the pokemon the user chose in ASCII art.
                showPokemon(pokemon_list) #Show the health and damage of the user's pokemon.
                blankLine() #Display a blank line
                lineBreak() #Display a line of characters that separates the previous line from the next.
                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
                
            elif game == 'g': #Check if 'game' is equal to 'g'.
                blankLine() #Display a blank line
                lineBreak() #Display a line of characters that separates the previous line from the next.
                gymMessage() #Display a message in the function 'gymMessage()' as soon as the user enters the gym.
                feisalMessage() #Display a message in the function 'feisalMessage()'.
                print(bulbasaur) #Display the ASCII art drawing of bulbasaur.
                wild_pokemon_name = 'Bulbasaur' #Make 'wild_pokemon_name()' store the name 'Bulbasaur'.
                wild_health = random.randint(50, 60) #Make 'wild_health' equal a random number between 50 and 60.
                wild_damage = random.randint(5,7) #Make 'wild_damage' equal a random number between 5 and 7.
                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #show stats of user pokemon
                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #show stats of enemy pokemon
                fight = True    #sets fight to true
                gymFightMessage()   #prompts user to enter a to attack
                fight_choice = input()  #gets user input and stores it as fight_choice
                while fight == True:    #creats a loop for the fight 
                    if fight_choice == 'a': #checks if fight_choice is equal to a
                        userAttackMessage(user_pokemon_name, wild_pokemon_name) #prints message indicating user pokemon attacks enemy      
                        wild_health = wild_health - pokemon_damage  #subtracts enemy health minus pokemon damage
                        showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows enemy pokemon stats
                        showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                        if wild_health <= 0:    #checks if wild pokemon's health is less than or equal to 0
                            fight_win = True    #user wins the fight
                            fight = False #Make 'fight' False.
                            blankLine() #Display a blank line
                            feisalLoseMessage() #message that feisal loses appears
                            beatFeisalMessage() #message that user beat feisal appears
                            blankLine() #Display a blank line
                        else:
                            enemyAttackMessage()    #displays message indicating enemy attacked
                            pokemon_health = pokemon_health - wild_damage   #subtracts user's health minus enemy damage
                            pokemon_list[0] = pokemon_health    #makes pokemon_list[0] equal to pokemon_health
                            showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows user pokemon stats
                            showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                            if pokemon_health <= 0: #checks if user pokemon's health is less than or equal to 0
                                fight = False #Make 'fight' False.
                                second_flag = False #makes 'second_flag' flase
                                blankLine() #Display a blank line
                                feisalWinMessage()  #prints message indicating feisal wins
                                lostToFeisalMessage()   #displays message indicating user lost
                                blankLine() #Display a blank line
                                gameLoseMessage()   #game lost message appears
                                lineBreak() #Display a line of characters that separates the previous line from the next.
                            else:   
                                gymFightMessage()   #prompts user to enter a to attack
                                fight_choice = input()  #gets user input and stores it as fight_choice
                                
                    else:
                        errorMessage()  #prints error message if user input is invalid
                        fight_choice = input()  #gets user input and stores it as fight_choice
                
                if fight_win == True:   #if user wins fight
                    noahMessage()   #prints pokemon trainer noah message
                    blankLine() #Display a blank line
                    print(pidgey)   #displays pidgey ASCII art
                    wild_pokemon_name = 'Pidgey'    #sets wild_pokemon_name to Pidgey
                    wild_health = random.randint(55,65) #generates pidgey health
                    wild_damage = random.randint(7,9)   #generates pidgey damage
                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows user pokemon stats
                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                    fight = True    #sets fight to true
                    gymFightMessage()   #prompts user to attack
                    fight_choice = input()  #gets user input and stores it as fight_choice
                    while fight == True:
                        if fight_choice == 'a': #checks if fight_choice is equal to a
                            userAttackMessage(user_pokemon_name, wild_pokemon_name) #prints message indicating user pokemon attacks enemy      
                            wild_health = wild_health - pokemon_damage  #subtracts enemy health minus pokemon damage
                            showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows enemy pokemon stats
                            showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                            if wild_health <= 0:    #checks if wild pokemon's health is less than or equal to 0
                                fight2_win = True   #sets fight2_win to true meaning user won the fight
                                fight = False #Make 'fight' False.
                                blankLine() #Display a blank line
                                noahLoseMessage()   #displays message indicating noah lost
                                beatNoahMessage()   #displays message indicating user beat noah
                                blankLine() #Display a blank line
                            else:
                                enemyAttackMessage()    #displays message indicating enemy is attacking
                                pokemon_health = pokemon_health - wild_damage   #subtracts enemy pokemon damage from user pokemon health
                                pokemon_list[0] = pokemon_health    #sets pokemon_list[0] to pokemon_health
                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows enemy pokemon stats
                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                                if pokemon_health <= 0: #checks if user pokemon's health is less than or equal to 0
                                    fight = False #Make 'fight' False.
                                    second_flag = False #make second_flag False
                                    noahWinMessage()    #display message indicating noah wins
                                    lostToNoahMessage() #display message indicating user lost to noah
                                    blankLine() #Display a blank line
                                    gameLoseMessage()   #message appears indicating game is lost
                                    lineBreak() #Display a line of characters that separates the previous line from the next.

                                else:
                                    gymFightMessage()   #prompts user to enter a to attack
                                    fight_choice = input()  #gets user input and stores it as fight_choice
                        else:
                            errorMessage()  #prints error message if user input is invalid
                            fight_choice = input()  #gets user input and stores it as fight_choice
                            
                    if fight2_win == True:  #if user wins second fight
                        licontiMessage()    #gym leader liconti message is displayed
                        blankLine() #Display a blank line
                        print(gengar)   #prints gengar ASCII
                        wild_pokemon_name = 'Gengar'    #sets wild pokemon name to gengat
                        wild_health = random.randint(60,75) #sets gengar health
                        wild_damage = random.randint(11,15) #sets gengar damage
                        showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #show user pokemon stats
                        showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #show enemy pokemon stats
                        fight = True    #sets fight to true
                        gymFightMessage()   #prompts user to enter a to attack
                        fight_choice = input()  #gets user input and stores it as fight_choice
                        while fight == True:    #sets loop that runs while fight is true
                            if fight_choice == 'a': #checks if fight_choice is equal to a
                                userAttackMessage(user_pokemon_name, wild_pokemon_name) #prints message indicating user pokemon attacks enemy      
                                wild_health = wild_health - pokemon_damage  #subtracts enemy health minus pokemon damage
                                showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows enemy pokemon stats
                                showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                                if wild_health <= 0:    #if enemy pokemon health is less than or equal to 0
                                    fight = False #Make 'fight' False.
                                    second_flag = False #sets second_flag to False
                                    blankLine() #Display a blank line
                                    licontiLoseMessage()    #displays message indicating liconti lost
                                    beatLicontiMessage()    #displays message indicating user won against liconti
                                    blankLine() #Display a blank line
                                    gameWinMessage()
                                    blankLine() #Display a blank line
                                    lineBreak() #Display a line of characters that separates the previous line from the next.
                                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                    programInputMessage() #Tell the user the different program options.
                                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                else:
                                    enemyAttackMessage()    #displays message indicating enemy is attacking
                                    pokemon_health = pokemon_health - wild_damage   #subtracts wild_damage from pokemon_health
                                    pokemon_list[0] = pokemon_health    #makes pokemon_list[0] equal to pokemon_health
                                    showPokemonStats(user_pokemon_name, pokemon_health, pokemon_damage) #shows user pokemon stats         
                                    showWildPokemonStats(wild_pokemon_name, wild_health, wild_damage)   #shows wild pokemon stats
                                    if pokemon_health <= 0: #if user pokemon health is less than or equal to 0
                                        fight = False   #makes fight true
                                        second_flag = False #makes second_flag false
                                        licontiWinMessage() #message appears indicating liconti wins
                                        lostToLicontiMessage()  #message appears if user loses to gym leader
                                        blankLine() #Display a blank line
                                        gameLoseMessage()   #message appears indicating user lost
                                        lineBreak() #Display a line of characters that separates the previous line from the next.
                                        print(pokemon_logo) #Display the pokemon logo in ASCII art.
                                        programInputMessage()   #displays initial program menu
                                        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                                        program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                                        
                                    else:
                                        gymFightMessage()   #prompts user to enter a to attack
                                        fight_choice = input()  #gets user input and stores it as fight_choice
                            else:
                                errorMessage()  #prints error message if user input is invalid
                                fight_choice = input()  #gets user input and stores it as fight_choice

                    else: #Check if the previous 'if' statement is False.
                        print(pokemon_logo) #Display the pokemon logo in ASCII art.
                        programInputMessage() #Tell the user the different program options.
                        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                        program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                        fight = False #Make 'fight' False.
                        second_flag = False #Make 'second_flag' False.
                    
                else:
                    fight = False #Make 'fight' False.
                    second_flag = False #Make 'second_flag' False.
                    print(pokemon_logo) #Display the pokemon logo in ASCII art.
                    programInputMessage() #Tell the user the different program options.
                    start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                    program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
                
                        
            elif game == 'q': #Check if 'game' is equal to 'q'.
                lineBreak() #Display a line of characters that separates the previous line from the next.
                blankLine() #Display a blank line
                quitGameMessage() #Display a message telling the user they are quitting the game
                blankLine() #Display a blank line.
                second_flag = False #Make 'second_flag' False.
                print(pokemon_logo) #Display the pokemon logo in ASCII art.
                programInputMessage() #Tell the user the different program options.
                start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
                program = checkProgramChoice(start) #Make 'program' equal to the 'programChoice()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
            elif game == 'error': #Check if 'game' is equal to 'error'.
                lineBreak() #Display a line of characters that separates the previous line from the next.
                gameInputMessage() #Use the function 'gameInputMessage()' to display the different options the user has in the main game.
                game_input = getGameInput() #Make 'game_input' a variable that stores what command the user want to do with the game using the function 'gameInput()'
                game = checkGameChoice(game_input) #Make 'game' a variable that makes decisions for what to do in the game based off the command they made that was stored in the variable 'game_input'.
            else: #Check if everything else in the 'if' statement is False.
                errorMessage() #Display an error message.
                
    elif program == 'q': #Check if 'program' is equal to 'q'.
        lineBreak() #Display a line of characters that separates the previous line from the next.
        flag = False #Make 'flag' False.
    elif program == 'h': #Check if 'program' is equal to 'h'.
        helpMessage() #Display the help menu.
        blankLine() #Display a blank line
        programInputMessage() #Tell the user the different program options.
        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
        program = checkProgramChoice(start) #Make 'program' equal to the 'runProgram()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
    elif program == 'error': #Check if 'program' is equal to 'error'.
        lineBreak() #Display a line of characters that separates the previous line from the next.
        programInputMessage() #Tell the user the different program options.
        start = getProgramInput() #Make 'start' equal the funtion of 'programInput()' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
        program = checkProgramChoice(start) #Make 'program' equal to the 'runProgram()' function that will use the user input from the 'programInput() function and make decisions based on what the user inputted.
    else: #Check if everything else in the 'if' statement is False.
        lineBreak() #Display a line of characters that separates the previous line from the next.
        errorMessage() #Display a message saying 'This should not happen
