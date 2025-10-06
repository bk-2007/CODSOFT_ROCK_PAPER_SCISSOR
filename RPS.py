import random as r
import time
class RPS:
    def __init__(self):
        self.user_score=0
        self.computer_score=0
        self.choices=['rock','paper','scissors']
        self.round=0

    
    def user_choice(self):
        self.user_input=input('\nenter your choice(rock,paper,scissors):\n').lower()
        if self.user_input in self.choices:
            return self.user_input
        else:
            print('invalid input please enter again\n')

    def computer_choice(self):
        self.computer_input=r.choice(self.choices)
        
        
    def game_logic(self,computer_input,user_input):
        if self.user_input==self.computer_input:
            return 'tie'
        elif (self.user_input=='rock'and self.computer_input=='scissors') or \
             (self.user_input=='scissors'and self.computer_input=='paper') or \
             (self.user_input=='paper'and self.computer_input=='rock'):
            self.user_score+=1
            return 'user_wins'
        else:
            self.computer_score+=1
            return 'computer_wins'
        
    def play_game(self,computer_input,user_input,game_logic):
               print(f'\nYOUR CHOICE:{self.user_input}')
               print(f'\nCOMPUTER CHOICE:{self.computer_input}\n')
               print('READY! SET! GO!\n')
               time.sleep(1)
               print(f'THE RESULTS OF ROUND {self.round} \n')
               time.sleep(1)
               if game_logic=='tie':
                   print(f'ITS TOUGH BUT IT IS A TIE FOR THIS ROUND\n')
               elif game_logic=='user_wins':
                   print(f'YOU ARE THE WINNER OF THIS ROUND,HURRAY YOU KILLED IT!\n')    
               elif game_logic=='computer_wins':
                    print(f'COMPUTER IS THE WINNER OF THIS ROUND\n')    
               print(f'SCORE->YOUR SCORE:{self.user_score}  COMPUTER SCORE:{self.computer_score}\n')     
    def play(self):
         print("-"*30)
         print('WELCOME to ROCK PAPER SCISSORS')
         print("-"*30)
         while True:
              self.round+=1
              users_choice=self.user_choice()
              computers_choice=self.computer_choice()
              results=self.game_logic(computers_choice,users_choice)
              self.play_game(computers_choice,users_choice,results)
              play_again=input('\nDO YOU WANT TO PLAY AGAIN(YES/NO):\n').upper()
              if play_again!='YES':
                   print('\nTHANKS FOR PLAYING \n')
                   print(f'FINAL SCORES->YOUR SCORE:{self.user_score}  COMPUTER SCORE:{self.computer_score}')
                   break
                   
game=RPS()
game.play()                   