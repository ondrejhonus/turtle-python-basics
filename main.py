from turtle import *
import tutel

again = 'y'
while again.lower() == 'y' or again == '':
    usr_in = input("1. Confused cursor\n2. Anarchy\n3. Race\n4. Spiral\nSelect an effect: ")

    try:
        if usr_in == '1':
            tutel.confused_cursor()
        elif usr_in == '2':
            tutel.anarchy()   
        elif usr_in == '3':
            tutel.race()
        elif usr_in == '4':
            size = input("Set the spiral size: ")
            tutel.spiral(int(size))
        clear()
        hideturtle()
        
    except Terminator:
        print("The turtle graphics window was closed. Exiting.")
        break
    again = input("Want to render again? [Y/n]").lower()
