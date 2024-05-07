import random
def main():
    options = ['rock','paper','scissors']
    prev_choices = []
    print("Welcome to Rock Paper Scissors")
    while True:
        plr_input = str(input("Enter rock, paper, or scissors: "))
        while plr_input not in options:
            print("Invalid.")
            plr_input = str(input("Enter rock, paper, or scissors: "))
        prev_choices.append(options.index(plr_input))
def bot(prev_choices):
    newest = prev_choices[-len(prev_choices)]
    spots = [index for index, value in enumerate(prev_choices) if value == newest]
    if len(spots) == 1:
        pass # prevent error while fix
    
