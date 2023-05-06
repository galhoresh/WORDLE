from colorama import Fore
from colorama import Style


def printChoice():
    input_test = False
    while (input_test == False):
        choice = input("Choose Your Display Type:\n1: For colourful printing\n2: For black and white printing\n")
        try:
            assert choice in ("1", "2")
            input_test = True
        except:
            print("Bad input, try again")
    return int(choice)


def printValues(words, results, print_choice):
    if print_choice == 1:
        for i in range(5):
                if results[-1][i] == "T":
                    print(f"{Fore.GREEN}", (words[-1][i]), f"{Style.RESET_ALL}", end=" ")
                elif results[-1][i] == "P":
                    print(f"{Fore.YELLOW}", words[-1][i], f"{Style.RESET_ALL}", end=" ")
                else:
                    print(f"{Fore.RED}", (words[-1][i]), f"{Style.RESET_ALL}", end=" ")
    else:
        for i in range(len(words)):
            print(words[i] + "\n" + str(results[i]) + "\n")
