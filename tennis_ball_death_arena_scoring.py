"""By Maxwell M. Banks
Wednesday 6/19/19
Scoring system for the game "Tennis Ball Death Arena"
"""

import sys
import os
import math 

class Player:
    """A class that holds the player's name and throws for the 
    game
    
    Attributes:
        name(str): The name of the player holding the class
        throws(list): A list of the throws of the players, starting
          with None values and being filled by tuple values as the 
          game progresses
    """
    def __init__(self, name):
        self.name = name
        self.throws = [None] * 10

    def __repr__(self):

        return ("{}:\n+").format(self.name, self.throws)

    def __eq__(self, other):

        return self.name == other.name and\
        self.throws == throws.name

    def add_throw(self, score_code):
        current_throw = 0
        for i in range(10):
            if self.throws[i] is None:
                current_throw = i
                break
        
        self.throws[current_throw] = (get_score(score_code), score_code)
    def get_total(self):
        score = 0
        for x in self.throws:
            score += x[0]

        return score
def get_score(score_code):
    return int(score_code)
    score_list = list(score_code)
    print(score_list)
    return 3
    

def print_scores(list_of_players):
    """
    Args:
        list_of_players(list): A list of the Player class in the given game
    """
    print_state = '   '
    for player in list_of_players: 
        print_state += player.name + '\t\t'
    
    print(print_state)

    for n in range(9):
        print_state = str(n + 1) + ': '
        for player in list_of_players:
            print_state += str(player.throws[n])
            print_state += '\t'
        print(print_state)
    print_state = '10:'
    for player in list_of_players:
        print_state += str(player.throws[9])
        print_state += '\t'
    print(print_state)
    print_state = "Fn:"
    for player in list_of_players:
        print_state += str(player.get_total())
        print_state += '\t\t'
    print(print_state)
    print(rankings(list_of_players))

def create_file(file_name, list_of_players):
    """Creates a file for the recorded game data and saves it into
    that file to be added to records in a folder called "TBDA Scores"
    which will be checked if it exists, if it does it will add it to
    it if it doesn't it will create it and then add it in
    Args:
        file_name(str): A string that is the name of the file
          in practice it will generally be "yyyymmdd-hhmm.txt" for the
          given data by the user.
        list_of_players(list): A list of players that contains all of
          their game information
    """
    file = open(file_name, 'w')
    print_state = '   '
    for player in list_of_players: 
        print_state += player.name + '\t\t'

    file.write(print_state + '\n')

    for n in range(9):
        print_state = str(n + 1) + ': '
        for player in list_of_players:
            print_state += str(player.throws[n])
            print_state += '\t'
        file.write(print_state + '\n')
    print_state = '10:'
    for player in list_of_players:
        print_state += str(player.throws[9])
        print_state += '\t'
    file.write(print_state + '\n')
    print_state = "fn:"
    for player in list_of_players:
        print_state += str(player.get_total())
        print_state += '\t\t'
    file.write(print_state + '\n\n')
    file.write(rankings(list_of_players))

def rankings(list_of_players):
    sorted = sort_players(list_of_players)
    print_state = ""
    print_state += '1st' + sorted[0].name
    print_stae += '2nd' + sorted[1].name
    try:
        sorted[]
    for player in sorted:
        print_state += player.name

def main():
    os.system('clear')
    player_name = 'a'
    list_of_players = []
    print("What is todays date? (yyyymmdd)")
    date = input("ex. Oct. 31 2013 -> 20131031 ")
    print("what is the time? (24h clock, hhmm): ")
    time = input("ex. 4:20 pm -> 1620 ")
    ##NAME NEEDS TO BE UNDER 16 CHARECTORS
    player_name = input('Input the players name: ')
    while player_name != "":
        list_of_players.append(Player(player_name))
        player_name = input('Input the players name: ')
        
    for round in range(10):
        print('Round ' + str(round + 1))
        for player in list_of_players:
            throw = input('Throw code for ' + str(player.name) + ': ')
            player.add_throw(throw)
            print(get_score(throw))
    print_scores(list_of_players)
    file_name = str(date) + '_' + str(time) + '.txt'
    create_file(file_name, list_of_players)
    



if __name__ == '__main__':
    main()
