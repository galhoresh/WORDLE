class Menu():

    def print_menu(self):
        menu = {
            1: 'Start Game',
            2: 'Exit Program',
            3: 'Watch game statistics'
        }
        for key in menu.keys():
            print(key, menu[key])

    def askForInput(self):
        input_test = False
        while (input_test==False):
            choice = input("Enter your choice: ")
            try:
                assert choice in ("1", "2", "3")
                input_test = True
            except:
                print("Bad input, try again")
        return int(choice)
