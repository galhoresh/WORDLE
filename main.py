from Game import Game
from Menu import Menu
from Printer import printChoice
from Statistics import Statistics
from WordArray import getWord

menu = Menu()
statistics = Statistics()

while True:
    menu.print_menu()
    choice = menu.askForInput()
    if choice == 1:  # start game
        print_choice = printChoice()
        word = getWord()
        game = Game(print_choice,word)
        game.Play()
    if choice == 2:  # end game
        break
    if choice == 3:  # statistics
        statistics.showStatistics()

