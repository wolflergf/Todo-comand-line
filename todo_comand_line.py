print(
    """
__        __   _ _    ____                       _____         
\ \      / /__| | |  / ___|___  _ __ ___   ___  |_   _|__      
 \ \ /\ / / _ \ | | | |   / _ \| '_ ` _ \ / _ \   | |/ _ \     
  \ V  V /  __/ | | | |__| (_) | | | | | |  __/   | | (_) |    
 __\_/\_/ \___|_|_|  \____\___/|_| |_| |_|\___|   |_|\___/     
|_   _|__         __| | ___   | |   (_)___| |_                 
  | |/ _ \ _____ / _` |/ _ \  | |   | / __| __|                
  | | (_) |_____| (_| | (_) | | |___| \__ \ |_                 
  |_|\___/  __  _\__,_|\___/  |_____|_|___/\__|___ _   _ _____ 
 / ___/ _ \|  \/  |  / \  | \ | |  _ \  | |   |_ _| \ | | ____|
| |  | | | | |\/| | / _ \ |  \| | | | | | |    | ||  \| |  _|  
| |__| |_| | |  | |/ ___ \| |\  | |_| | | |___ | || |\  | |___ 
 \____\___/|_|  |_/_/   \_\_| \_|____/  |_____|___|_| \_|_____|
    """
)

file_name = "todo_list.txt"


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()  # Fixed the file reading issue
        return content
    except FileNotFoundError:  # Corrected the exception type
        return "File not found."


def choice(user_choice):
    if user_choice == "1":
        file_content = read_file(file_name)
        print(file_content)
    elif user_choice == "4":
        print("Exiting the program.")
        exit()  # Exit the script if the user chooses option 4


while True:
    user_choice = input(
        """\nFollow the Menu Below and choose an option:
      1 - Show to-do list
      2 - Add to-do
      3 - Delete a to-do
      4 - Exit
    Enter your choice: """
    )
    choice(user_choice)
