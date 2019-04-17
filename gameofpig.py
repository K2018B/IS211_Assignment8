#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Week 8 Assignment"""

import random
import argparse
import time

parser = argparse.ArgumentParser(description = "The PIG game")
parser.add_argument("--player1", type = str, help = "Please type 'human' or 'computer'")
parser.add_argument("--player2", type = str, help = "Please type 'human' or 'computer'")
parser.add_argument("--timed", type = str, help = "Please type 'y'")
arg = parser.parse_args()

if arg.player1 is not None:
    player1 = arg.player1    
else:
    player1 = "human"    

if arg.player2 is not None:
    player2 = arg.player2    
else:
    player2 = "human" 

class Player():
    def __init__(self,):        
        self.score = 0
        self.name = None        
        self.roll = "yes"
        self.hold = "no"

    def choice(self):
        while True:
            option = raw_input("Hold(h) or Roll(r) ?")
            if option.lower() in ['hold', 'h']:                
                self.hold = "yes"
                break
            elif option.lower() in ['roll', 'r']:                
                self.hold = "no"
                break

class ComputerPlayer(Player):   

    def choice(self):
        if self.score < 25 or self.score < (100 - self.score):
            print "The Computer Player is holding...."
            time.sleep(2)
            self.hold = "yes"
        else:
            time.sleep(2)
            print "The Computer Player is rolling...."
            self.hold = "no"

class PlayerFactory():
    def __init__(self):
        return None
    
    def chooseplayertype(self, playertype):        
        if playertype == "human":
            return Player()
        elif playertype == "computer":
            return ComputerPlayer()        

class Die():
    
    def __init__(self):
        self.face = 1        
    def rolldice(self):
        self.face = random.randint(1,6)        
    
class PigGame():
    """
    Run the main game
    """ 
    def __init__(self, die, playerone, playertwo):
        self.die = die
        self.playerone = playerone
        self.playertwo = playertwo
        self.player = None
        self.timer_start = time.time()
        
        if arg.player1 == "human" or arg.player1 is None:            
            self.playerone.name = "Player One"
        else:
            self.playerone.name = "Player One(Computer)"

        if arg.player2 == "human" or arg.player2 is None:            
            self.playertwo.name = "Player Two"
        else:
            self.playertwo.name = "Player Two(Computer)"
        
        choose_player = random.randint(1,2)
        if choose_player == 1:
            print("Player one will start")
            self.player = playerone
        else:
            print("Player two will start")
            self.player = playertwo
        self.rolldice()
            
    def rolldice(self):
        self.playerscore = 0
        self.die.rolldice()
        dicenum = int(self.die.face)
        print ("You rolled", dicenum, self.player.name)
        if dicenum == 1:
            self.playerscore = 0
            print "1 is rolled which equals to zero points...Next Player's turn"
            self.switchplayer()
        else:
            self.playerscore = self.playerscore + dicenum
            self.player.choice()
            if(self.player.hold == "no"):
                self.player.score = self.player.score + self.playerscore
                print("Your score is ", playerone.score, "Player One")
                print("Your score is ", playertwo.score, "Player Two")
                if self.player.score >= 100:
                    print("You're a Winner!!!", self.player.name)
                else:           
                    self.rolldice()
            else:                
                self.player.score = self.player.score + self.playerscore
                print("Your score is ", playerone.score, "Player One")
                print("Your score is ", playertwo.score, "Player Two")
                if self.player.score >= 100:
                    print("You're a Winner!!!", self.player.name)
                else:           
                    self.switchplayer()

    def switchplayer(self):
        if self.player == self.playerone:            
            self.player = self.playertwo
            self.rolldice()
        else:
            self.player = self.playerone           
            self.rolldice()

class PigGameProxyPatternTimed(PigGame):   

    def rolldice(self):         
        self.playerscore = 0
        self.die.rolldice()
        dicenum = int(self.die.face)
        print ("You rolled", dicenum, self.player.name)
        if dicenum == 1:
            self.playerscore = 0
            print "1 is rolled which equals to zero points...Next Player's turn"
            self.switchplayer()
        else:
            self.playerscore = self.playerscore + dicenum
            self.player.choice()
            if(self.player.hold == "no"):
                self.player.score = self.player.score + self.playerscore
                print("Your score is ", playerone.score, "Player One")
                print("Your score is ", playertwo.score, "Player Two")
                print("Time remaining:",(round(60 - (time.time() - self.timer_start))), "sec.")
                if self.player.score >= 100:
                    print("You're a Winner!!!", self.player.name)
                elif (time.time() - self.timer_start) >= 60 :
                    print("Times UP!!!")
                    if playerone.score > playertwo.score:
                        print("***Player One is the WINNER!!!***")
                    else:
                        print("***Player Two is the WINNER!!!***") 
                else:                    
                    self.rolldice()
            else:                
                self.player.score = self.player.score + self.playerscore
                print("Your score is ", playerone.score, "Player One")
                print("Your score is ", playertwo.score, "Player Two")                    
                print("Time remaining:",(round(60 - (time.time() - self.timer_start))), "sec.")
                if self.player.score >= 100:
                    print("You're a Winner!!!", self.player.name)
                elif (time.time() - self.timer_start) >= 60 :
                    print("Times UP!!!")
                    if playerone.score > playertwo.score:
                        print("***Player One is the WINNER!!!***")
                    else:
                        print("***Player Two is the WINNER!!!***")                        
                else:                    
                    self.switchplayer()

    def switchplayer(self):
        if self.player == self.playerone:            
            self.player = self.playertwo
            self.rolldice()
        else:
            self.player = self.playerone           
            self.rolldice()    
    
    
if __name__ == "__main__":    
    print (
           raw_input("Welcome to the Pig Game\n"
                     "***A random selection will be performed to select which player starts***\n"
                     "...hit enter to continue..."))
    die = Die()
    plfact = PlayerFactory()

    
    playerone = plfact.chooseplayertype(player1)
    playertwo = plfact.chooseplayertype(player2)
    if arg.timed is None:        
        PigGame(die, playerone, playertwo)
    elif arg.timed == "y":
        print("***Timed Game Choosen***\n ***Players with the Highest score after 60 seconds WINS!!!****")
        PigGameProxyPatternTimed(die, playerone, playertwo)
    else:
        PigGame(die, playerone, playertwo)
