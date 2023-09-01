
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

# Menus
def view_data_menu():
    looping = True
    while(looping):
        print_view_data_menu()
        command = input("Input your Command :")
        command = command.lower()

        #Print All Pets
        if command == "1":
            print_all_pets()
        #Print Pet by ID
        elif command == "2":
            pet_id = input("Input id to search for:")
            pet_id = int(pet_id)
            print_pet_by_id(pet_id)
        #Exit this sub menu
        elif command == "e":
            looping = False
            print("Exiting to main menu...")
        else:
            print("Command not recognized, try again...\n")

def create_new_pet_menu():
    print("Create a new pet:")
    
    name = input("input a name:")
    breed = input("input a breed:")
    age = input("input an age:")
    age = int(age)
    owner_id = input("Input the id of the owner:")
    owner_id = int(owner_id)

    pet = Pet(owner_id, name, breed, age)

    print("Here is the generated pet")
    print_pet_row_header()
    print_pet_row(pet)
    print_pet_row_footer()

    print("Would you like to save it to the database?")
    deciding = True
    while deciding:
        decision = input("(Y/N) :")
        if decision.lower() == "y":
            pet.save()
            deciding = False
            print("Your pet has been created and saved to the database!")
            print("returning to Modify Menu....\n")
        elif decision.lower() == "n":
            print("Pet Creation canceled")
            print("returning to Modify Menu....\n")
            deciding = False
        else:
            print("Decision must be either 'Y' or 'N'")


def modify_data_menu():
    # TODO give user extra modification options
    # for now just create new pet
    create_new_pet_menu()

    print("Returning to Main Menu ... \n")

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