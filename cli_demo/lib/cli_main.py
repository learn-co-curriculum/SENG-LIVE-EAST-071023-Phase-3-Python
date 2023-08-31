
from pet import Pet


# Print methods
def print_welcome_message():
    print("Welcome to the Pet Owner Command Line Interface")

def print_main_menu() :
    print("+----------------------+")
    print("| Dog Walker Main Menu |")
    print("+----------------------+")
    print("| Options :            |")
    print("| 1. View Data         |")
    print("| 2. Modify Data       |")
    print("| e: Exit the program  |")
    print("+----------------------+")

def print_view_data_menu():
    print("+----------------------+")
    print("| View Data Menu       |")
    print("+----------------------+")
    print("| Options :            |")
    print("| 1. Print All Pets    |")
    print("| 2. Print pet by ID   |")
    print("| e: Exit Menu         |")
    print("+----------------------+")

def print_pet_row_header():
    print("+----+--------+---------------------+-----+")
    print("| id |  name  |        breed        | age |")
    print("+----+--------+---------------------+-----+")

def print_pet_row_footer():
    print("+----+--------+---------------------+-----+")

def print_pet_row(pet):
    print("|{:3d} |{:8s}|{:21s}|  {:2d} |".format(pet.id, pet.name, pet.breed, pet.age))

def print_all_pets( ):
    print("Printing pets table...")
    all_pets = Pet.all()
    print_pet_row_header()
    for pet in all_pets:
        print_pet_row(pet)
    print_pet_row_footer()

def print_pet_by_id ( id ):
    pet = Pet.find_by_id(id)
    if pet is not None:
        print_pet_row_header()
        print_pet_row(pet)
        print_pet_row_footer()
    else:
        print("Could not find pet")


def view_data_menu():
    looping = True
    while(looping):
        print_view_data_menu()
        command = input("Input your Command :")
        command = command.lower()

        if command == "1":
            print_all_pets()
        elif command == "2":
            pet_id = input("Input id to search for:")
            pet_id = int(pet_id)
            print_pet_by_id(pet_id)

        elif command == "e":
            looping = False
            print("Exiting to main menu...")
        else:
            print("Command not recognized, try again...\n")


def modify_data_menu():
    pass

# Main Method Code
if __name__ == "__main__":

    print_welcome_message()

    looping = True
    while (looping):
        print_main_menu()
        command = input("Input your Command :")

        command = command.lower()

        if command == "1":
            view_data_menu()
        elif command == "2":
            modify_data_menu()
        elif command == "e":
            looping = False
            print("Thank you for using my CLI.")
            print("Exiting...")
        else:
            print("Command not recognized, try again...\n")