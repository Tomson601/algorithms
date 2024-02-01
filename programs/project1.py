import json

database_file = "database.json"

with open(database_file) as outfile:
    data = outfile.read()

if data != "":
    database = json.loads(data)
else:
    database = []
    print("Baza danych jest pusta!")


def update_db():
    with open(database_file, "w") as json_file:
        json.dump(database, json_file, indent=2)


def give_next_id():
    if database == []:
        return 0
    max_id = database[0]["ID"]
    print(max_id)
    for line in database:
        if max_id < line["ID"]:
            max_id = line["ID"]
    return max_id+1


def add_user():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    identifier = give_next_id()

    user_obj = {
        "ID": identifier,
        "name": name,
        "surname": surname,
        "is_active": True
    }
    database.append(user_obj)
    update_db()
    return print(f"Utworzono użytkownika: {user_obj}")


def delete_user():
    u_id = int(input("Podaj id użytkownika, którego chcesz usunąć: "))
    max_u_id = give_next_id()-1

    if u_id > max_u_id:
        return print("Nie znaleziono użytkownika z podanym u_id.")
    else:
        for user in database:
            if user["ID"] == u_id:
                database.remove(user)
                update_db()
                print(f"Pomyślnie usunięto użytkownika")
                return 0
    return print("Nie znaleziono użytkownika z podanym u_id.")


def modify_menu(user):
    print(user)
    print("######################\n\t\tZmień:")
    print("1. Imię\n2. Nazwisko\n3. Stan\n0. Wróć")
    print("######################\n")

    user_choice = int(input("Podaj wybór: "))

    if user_choice == 0:
        return 0
    elif user_choice == 1:
        print(f"Obecne imię użytkownika: {user['name']}")
        new_name = input("Podaj nowe imię: ")
        print("")
        user["name"] = new_name
    elif user_choice == 2:
        print(f"Obecne nazwisko użytkownika: {user['surname']}")
        new_surname = input("Podaj nowe nazwisko: ")
        print("")
        user["surname"] = new_surname
    elif user_choice == 3:
        print(f"Obecny stan konta (True/False) użytkownika : {user['is_active']}")
        string = input("Podaj stan konta użytkownika: ")
        if string == "True":
            state = True
        elif string == "False":
            state = False
        else:
            print("Podano złą opcję!")
            return 0

        print("")
        user["is_active"] = state
    else:
        print("Podano złą liczbę.")
        return 0
    print("Pomyślnie zmodyfkikowano użytkownika:")
    print(user)


def modify_user():
    u_id = int(input("Podaj id użytkownika, którego chcesz zmodyfikować: "))
    max_u_id = give_next_id()-1

    if u_id > max_u_id:
        return print("Nie znaleziono użytkownika z podanym u_id.")
    else:
        for line in database:
            if line["ID"] == u_id:
                user = line
                break

        modify_state = modify_menu(user)
        if modify_state == 0:
            return 0
        else:
            update_db()


def menu():
    menu = """
    ################################################
    #       System zarządzania siłownią v1.0       #
    #   1. Sprawdź listę użytkowników              #
    #   2. Dodaj użytkownika                       #
    #   3. Usuń użytkownika                        #
    #   4. Zmodyfikuj użytkownika                  #
    #   0. Zakończ działanie systemu               #
    ################################################
    """
    return menu


def interpret_instruction(choice):
    if choice == 0:
        print("Do widzenia!")
    elif choice == 1:
        for line in database:
            print(line)
    elif choice == 2:
        add_user()
    elif choice == 3:
        delete_user()
    elif choice == 4:
        modify_user()
    else:
        print(f"Nie prawidłowy wybór ({choice})")


user_choice = -1

while user_choice != 0:
    print(menu())
    user_choice = int(input("Wybór użytkownika: "))
    interpret_instruction(user_choice)
