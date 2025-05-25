# Player state
inventory = []
notebook = []
game_over = False
current_room = 1

# Puzzle answers
box_code_room1 = "4132"
final_password = "freedom"
keycard_code = "7291"

def intro():
    print("You wake up in a mysterious room.")
    print("You see a table, a drawer, and a locked box.")
    print("Type commands like: look table, open drawer, use box, use door.")
    print("Other commands: inventory, notebook.")

def process_command(command):
    global game_over, current_room

    if current_room == 1:
        if "look" in command and "table" in command:
            print("On the table is a diary. It reads: 'Some numbers are hidden in the corners.'")
            if "Diary hint: Numbers are hidden in the corners" not in notebook:
                notebook.append("Diary hint: Numbers are hidden in the corners")

        elif "open" in command and "drawer" in command:
            print("You opened the drawer and found a note that says: 'The code is 4132'.")
            if "Note: Code is 4132" not in inventory:
                inventory.append("Note: Code is 4132")

        elif "use" in command and "box" in command:
            if "Note: Code is 4132" in inventory:
                code = input("Enter the 4-digit code for the box: ").strip()
                if code == box_code_room1:
                    print("The box opens! Inside is another note: 'Final password is freedom.'")
                    if "Final password: freedom" not in notebook:
                        notebook.append("Final password: freedom")
                else:
                    print("Wrong code. The box remains locked.")
            else:
                print("You don't know the code yet.")

        elif "use" in command and "door" in command:
            if "Final password: freedom" in notebook:
                code = input("Enter the password to unlock the door: ").strip()
                if code == final_password:
                    print("The door opens! You enter the next room...")
                    current_room = 2
                    room2_intro()
                else:
                    print("Wrong password. The door is still locked.")
            else:
                print("You see a password-locked door. You need to find the password.")

    elif current_room == 2:
        if "look" in command and "bookshelf" in command:
            print("You find a hidden book. Inside it says: 'Keycard is behind the painting.'")

        elif "look" in command and "painting" in command:
            print("You remove the painting and find a keycard with the number 7291.")
            if "Keycard: 7291" not in inventory:
                inventory.append("Keycard: 7291")

        elif "use" in command and "console" in command:
            if "Keycard: 7291" in inventory:
                code = input("Enter the keycard number to activate console: ").strip()
                if code == keycard_code:
                    print("Console activated. The wall slides open revealing a final door.")
                    current_room = 3
                    room3_intro()
                else:
                    print("Wrong keycard number.")
            else:
                print("You need to find the keycard first.")

    elif current_room == 3:
        if "look" in command and "panel" in command:
            print("The panel reads: 'Answer this to escape: What has keys but can't open locks?'")
        
        elif "answer" in command:
            response = input("Your answer: ").strip().lower()
            if "piano" in response:
                print("Correct! The door opens and you step into the sunlight. You win!")
                game_over = True
            else:
                print("Incorrect. Try again.")

    elif "inventory" in command:
        print("Your Inventory:")
        for item in inventory:
            print("- " + item)

    elif "notebook" in command:
        print("Your Notebook:")
        for note in notebook:
            print("- " + note)

    else:
        print("Unknown command. Try: look/open/use/inventory/notebook/answer.")

def room2_intro():
    print("\nRoom 2:")
    print("You are in a library. There's a bookshelf, a large painting, and a control console.")
    print("Try commands like: look bookshelf, look painting, use console.")

def room3_intro():
    print("\nFinal Room:")
    print("This is a small high-tech chamber with a glowing panel.")
    print("Try: look panel, answer")

def main():
    intro()
    while not game_over:
        command = input("\nWhat do you want to do? ").strip().lower()
        process_command(command)

if __name__ == "__main__":
    main()
