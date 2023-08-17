import random
import json
import os

def main():
    while True:
        os.system("cls")
        menu = input("Choisir une option :\n1 : [A]rgent\n2 : [I]nventaire\n3 : [P]ersonnage\n4 : [D]és\n5 : [S]auvergarde\n> ")
        if menu == "A" or menu == "a":
            coin()
        elif menu == "I" or menu == "i":
            stuff()
        elif menu == "P" or menu == "p":
            character()
        elif menu == "D" or menu == "d":
            dice()
        elif menu == "S" or menu == "s":
            save()
        elif menu == "Yaku":
            os.system("cls")
            os.system("curl parrot.live")
        else :
            ()

def coin():
    global players
    all = str()
    for key in players.keys():
        all += "\n" + key
    if all == str():
        os.system("cls")
        print("Vous n'avez aucun personnage")
        os.system("pause")
        main()
    while True:
        if all == "\n" + key:
            name = key
            break
        os.system("cls")
        name = input("La solde de quel personnage voulez vous afficher :" + all + "\n> ")
        if name in players.keys():
            break
    while True:
        os.system("cls")
        menu = input("Solde actuel : " + str(players[name]["coins"]) + "$\nChoisir une option :\n1 : [D]époser\n2 : [R]etirer\n> ")
        if menu == "D" or menu == "d":
            while True:
                os.system("cls")
                add = input("Choisir somme d'argent à déposer :\n> ")
                try :
                    nbr = int(add)
                    players[name]["coins"] += nbr
                    print(add +"$ ont été ajouté à la solde de " + name)
                    os.system("pause")
                    main()
                except :
                    ()
        elif menu == "R" or menu == "r":
            while True:
                os.system("cls")
                substract = input("Choisir somme d'argent à retirer :\n> ")
                try :
                    nbr = int(substract)
                    if players[name]["coins"] - nbr >= 0:
                        players[name]["coins"] -= nbr
                        print(str(nbr) + "$ ont été retiré à la solde de " + name)
                        os.system("pause")
                        main()
                    else :
                        print("Vous ne possédez pas cet argent")
                        os.system("pause")
                        main()
                except :
                    ()
        else :
            ()

def stuff():
    global players
    all = str()
    for key in players.keys():
        all += "\n" + key
    if all == str():
        os.system("cls")
        print("Vous n'avez aucun personnage")
        os.system("pause")
        main()
    while True:
        if all == "\n" + key:
            name = key
            break
        os.system("cls")
        name = input("L'inventaire de quel personnage voulez vous afficher :" + all + "\n> ")
        if name in players.keys():
            break
    while True:
        os.system("cls")
        menu = input("Choisir une option :\n1 : [I]nventaire\n2 : [A]jouter\n3 : [R]etirer\n> ")
        if menu == "I" or menu == "i":
            os.system("cls")
            full = str()
            for x in players[name]["inv"]:
                full = full + "\n" + x
            if full == str():
                print("L'inventaire de " + name + " est vide")
            else:
                print("Voici le contenu de l'inventaire de " + name + " :" + full)
            os.system("pause")
            main()
        elif menu == "A" or menu == "a":
            os.system("cls")
            item = input("Entrer le nom de l'bjet à ajouter dans l'inventaire de " + name + " :\n> ")
            players[name]["inv"].append(item)
            os.system("cls")
            print("L'objet " + item + " a été ajouté dans l'inventaire de " + name)
            os.system("pause")
            main()
        elif menu == "R" or menu == "r":
            while True:
                os.system("cls")
                item = input("Entrer le nom de l'objet à retirer de l'inventaire de " + name + " :\n> ")
                try :
                    players[name]["inv"].remove(item)
                    os.system("cls")
                    print("L'objet " + item + " a été retiré de l'inventaire de " + name)
                    os.system("pause")
                    main()
                except :
                    ()
        else :
            ()

def character():
    global players
    while True:
        os.system("cls")
        menu = input("Choisir une option :\n1 : [P]ersonnage\n2 : [A]jouter\n3 : [G]énérer\n4 : [R]etirer\n> ")
        if menu == "P" or menu == "p":
            os.system("cls")
            if players == {}:
                print("Vous n'avez aucun personnage")
            else:
                print("Voici la liste de vos personnages")
                for key in players.keys():
                    print(key + " :\n   Argent : " + str(players[key]["coins"]) + "$\n   Race : " + players[key]["race"] + "\n   Fruit du démon : " + players[key]["power"])
            os.system("pause")
            main()
        elif menu == "A" or menu == "a":
            while True:
                os.system("cls")
                name = input("Entrer le du personnage à ajouter à la partie :\n> ")
                if name == "":
                    ()
                elif name in players.keys():
                    os.system("cls")
                    print("Le personnage " + name + " existe déjà")
                    os.system("pause")
                else:
                    break
            while True:
                all = str()
                os.system("cls")
                for x in player_data["race"]:
                    all += "\n" + x
                race = input("Selectionner sa race :" + all + "\n> ")
                if race in player_data["race"]:
                    break
                else:
                    ()
            while True:
                all = str()
                os.system("cls")
                for x in player_data["power"]:
                    all += "\n" + x
                power = input("Selectionner son fruit du démon :" + all + "\n> ")
                if power in player_data["power"]:
                    break
                else:
                    ()
            while True:
                all = str()
                os.system("cls")
                for key in player_data["pack"].keys():
                    all += "\n" + key
                pack = input("Selectionner son starter pack :" + all + "\n> ")
                if pack in player_data["pack"].keys():
                    break
                else:
                    ()
            player = {
                "race": race,
                "power": power,
                "coins": 100,
                "inv": player_data["pack"][pack]
            }
            players.update({name: player})
            os.system("cls")
            print("Le personnage " + name + " a été ajouté à la partie")
            os.system("pause")
            main()
        elif menu == "G" or menu == "g":
            while True:
                os.system("cls")
                name = input("Entrer le nom du personnage à ajouter à la partie :\n> ")
                if name == "":
                    ()
                elif name in players.keys():
                    os.system("cls")
                    print("Le personnage " + name + " existe déjà")
                    os.system("pause")
                else:
                    break
            race = player_data["race"][random.randint(0, len(player_data["race"])-1)]
            power = player_data["power"][random.randint(0, len(player_data["power"])-1)]
            inv = list(player_data["pack"].keys())[random.randint(0, len(list(player_data["pack"].keys())))-1]
            player = {
                "race": race,
                "power": power,
                "coins": 100,
                "inv": player_data["pack"][inv]
            }
            players.update({name: player})
            os.system("cls")
            print("Le personnage " + name + " a été ajouté à la partie")
            os.system("pause")
            main()
        elif menu == "R" or menu == "r":
            all = str()
            for key in players.keys():
                all += "\n" + key
            if all == str():
                os.system("cls")
                print("Vous n'avez aucun personnage")
                os.system("pause")
                main()
            while True:
                os.system("cls")
                name = input("Entrer le nom du personnage à retirer :" + all + "\n> ")
                if name in players.keys():
                    players.pop(name)
                    break
                else:
                    ()
            os.system("cls")
            print("Le personnage " + name + " a été retiré de la partie")
            os.system("pause")
            main()
            
def save():
    global players
    while True:
        os.system("cls")
        menu = input("Choisir une option :\n1 : [E]registrer\n2 : [C]harger\n3 : [S]upprimer\n> ")
        if menu == "E" or menu == "e":
            while True:
                while True:
                    os.system("cls")
                    name = input("Choisir le nom de votre sauvegarde\n> ")
                    if name == "":
                        ()
                    else:
                        break
                try:
                    with open("save/" + name + ".json", "w") as file:
                        json.dump(players, file)
                    os.system("cls")
                    print("La sauvegarde " + name + " a été enregistrée")
                    os.system("pause")
                    main()
                except:
                    os.system("cls")
                    print("Ce nom est déjà pris")
                    os.system("pause")

        elif menu == "C" or menu == "c":
            all = str()
            for x in os.listdir("save/"):
                if x == "data.json":
                    ()
                else:
                    all += "\n" + x[:-5]
            while True:
                if all == str():
                    os.system("cls")
                    print("Vous n'avez aucune sauvegarde")
                    os.system("pause")
                    main()
                while True:
                    os.system("cls")
                    name = input("Entrer le nom de la sauvegarde à charger :" + all + "\n> ")
                    if name == "data":
                        ()
                    else:
                        break
                try:
                    players = json.loads(open("save/" + name +".json", "r").read())
                    os.system("cls")
                    print("La sauvegarde " + name + " a été chargée")
                    os.system("pause")
                    main()
                except:
                    ()
        elif menu == "S" or menu == "s":
            all = str()
            for x in os.listdir("save/"):
                if x == "data.json":
                    ()
                else:
                    all += "\n" + x[:-5]
            while True:
                if all == str():
                    os.system("cls")
                    print("Vous n'avez aucune sauvegarde")
                    os.system("pause")
                    main()
                while True:
                    os.system("cls")
                    name = input("Entrer le nom de la sauvegarde à éffacer :" + all + "\n> ")
                    if name == "data":
                        ()
                    else:
                        break
                try:
                    os.remove("save/" + name + ".json")
                    os.system("cls")
                    print("La sauvegarde " + name + " a été éffacée")
                    os.system("pause")
                    main()
                except:
                    ()
        else:
            ()

def dice():
    while True:
        os.system("cls")
        dé = input("Choisir le nombre de faces de votre dé :\n> ")
        try:
            os.system("cls")
            print("Vous avez tiré le numéro", random.randint(1, int(dé)))
            os.system("pause")
            main()
        except:
            ()



try:
    os.mkdir("save")
except:
    ()
try:
    with open("save/data.json", "w") as file:
        json.dump({"race": ["Humain", "Troll", "Elfe", "Orc", "Nain", "Homme poisson"], "power": ["Chauve souris", "Acide", "Cyclope", "Fragmentation", "Eclosion"], "pack": {"Survivor": ["couteau de surive", "briquet", "gourde"], "Chasseur": ["arc", "10 fleches", "gourde"], "Sherif": ["revolver", "10 balles", "gourde"], "Healer": ["bandages", "potion de soin", "gourde"], "Combattant": ["glaive", "bouclier", "gourde"], "Explorateur": ["gps", "lampe torche", "gourde"]}}, file)
        file.close()
except:
    ()

players = {}
player_data = json.loads(open("save/data.json", "r").read())

main()