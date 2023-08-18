import json
import os

def My_Login():
    # ANSI escape code for green text color
    green_text = "\033[92m"
    first_name = input("Enter your first name: ")
    family_name = input("Enter your family name: ")
    name_dict = {
        "first_name": first_name,
        "family_name": family_name
    }
  # Print all in green
    print(f"{green_text}Welcome {first_name} {family_name}")
    print(f"{green_text}Name dictionary: {name_dict}") 
    print(f"{green_text}") # print new line

  # Reset color
    print("\033[0m")

    # Save the dictionary as JSON to a file
    with open("name_data.json", "w") as json_file:
        json.dump(name_dict, json_file, indent=4)
    
# Clear the terminal
def clear_ter():
    clear_terminal = input("Do you want to clear the terminal? (y/n): ")
    if clear_terminal.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')



