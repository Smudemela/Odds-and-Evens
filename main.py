from random import randint

welcome_banner = """
                Welcome to Odds and Evens!

    This game simulates a hand game between two 
    players. Each player holds up a hidden amount
    of fingers on one hand. One player chooses 
    whether the sum will be "odd" or "even". Then,
    each player shows their hand, and you take the
    total of the number of fingers and see who wins.

    For example, if player1 chooses "odd" and the
    sum of the fingers is 4, player1 loses.
"""

print(welcome_banner)

player_name = input("Whats your name? ")
num_player_finger = int(input("How many fingers do you want to hold up? "))
num_computer = randint(1,5)
player_choice = input("odd or even ")

if num_player_finger < 1 or num_player_finger > 5:
    print("Invalid Fingers")
    num_player_finger = randint(1,5)
    
if player_choice != "odd" and player_choice != "even":
    print("Invalid Choice")
    player_choice = "even"
 
sum_fingers =  num_player_finger + num_computer

print(num_computer)
print(num_player_finger)

if sum_fingers % 2 == 0 and player_choice == "even" :
   print("Player wins!")

elif sum_fingers % 2 != 0 and player_choice == "odd" :
   print("Player wins!")  
else:
    print("The computer wins!")


    