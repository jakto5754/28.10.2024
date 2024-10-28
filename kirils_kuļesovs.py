# Piedzīvojums Spoku Mājā
import random

# Inicializē mainīgos
player_alive = True

ghost_var = 0

# Definē funkciju, kas sāk spēli un vada ciklu, kamēr spēlētājs ir dzīvs
def start_game():
    while player_alive:
        entrance()

def handle_command(choice):
    if choice == "inventory":
        show_inventory()
        return True
    return False


def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "iekša":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        elif handle_command(choice):
            continue
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi' un 'dzīvojamo istabu'.")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba"]:
        choice = input(">>> ").lower()
        if choice == "virtuve":
            kitchen()
        elif choice == "dzīvojamā istaba":
            living_room()
        elif choice == "istaba":
            living_room()
        elif handle_command(choice):
            continue
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def kitchen():
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod rūsinātu nazi. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
    choice = ""
    while choice not in ["ņem", "aizvērtu"]:
        choice = input(">>> ").lower()
        if handle_command(choice):
            continue
        elif choice == "ņem":
            add_to_inventory("nazis")
            if ghost_var == 0:
                ghost_var = 1
                ghost_event()
            if ghost_var == 1:
                continue
        elif choice == "aizvērtu":
            print("Jūs nolēmāt neņemt nazi.")
            kitchen_b()

def ghost_event():
    global ghost_var
    print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if handle_command(choice):
            continue
        elif choice == "cīnīties":
            if is_in_inventory("nazis"):
                print("Tu uzvarēji spoku ar nazi! Tu atgriezies foajē.")
                foyer()
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game()
        elif choice == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        else:
            print("Nepareiza izvēle.")

def kitchen_b():
    print("Kur tu var iet talāk? Foaje vai ēdamistaba?")
    choice = ""
    while choice not in ["foaje", "ēdamistaba"]:
        if handle_command(choice):
            continue
        elif choice == "foaje":
            foyer()
        elif choice == "ēdamistaba":
            dining()
        elif choice == "edamistaba":
            dining()

def dining():
    print("gfhgfh")
    choice = ""



def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vai tu vēlies 'skatīties' spogulī vai iet 'atpakaļ'?")
    choice = ""
    while choice not in ["skatīties", "atpakaļ"]:
        choice = input(">>> ").lower()
        if handle_command(choice):
            continue
        elif choice == "skatīties":
            print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
            end_game()
        elif choice == "atpakaļ":
            foyer()
        else:
            print("Nepareiza izvēle.")

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga, tu varētu tās 'atvērt'.")
    choice = ""
    while choice != "atvērt":
        choice = input(">>> ").lower()
        if handle_command(choice):
            continue
        elif choice == "atvērt":
            if "atslēga" in inventory:
                print("Tu atvēri durvis un izbēgi no spoku mājas! Tu uzvari!")
                end_game()
            else:
                print("Durvis ir aizslēgtas. Tev nepieciešama atslēga.")
                basement()
        else:
            print("Nepareiza izvēle.")
            foyer()

inventory = {}

def add_to_inventory(item, quantity=1):
    if item in inventory:
        print(f"tev jau ir {item}")
    else:
        inventory[item] = quantity
        print(f"{quantity} {item}")

def is_in_inventory(item):
    return item in inventory

def show_inventory():
    if not inventory:
        print("nav")
    else:
        print("gggg")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
print("Sveicināts Piedzīvojums Spoku Mājā!")
start_game()
