import os

from .controllers import create_player, create_tournament, create_player_list
from .resume_tournament import partial_tournament
from .tinydb_data import fetch_all_data, update_all_ranking, \
                         display_all_tournaments, display_tournament_data
from .save_load import load_data
from view.views import View


view = View()


def option1():
    create_player()


def option2():
    player_list = fetch_all_data()
    while True:
        try:
            message = ("1 - Lister par ordre alphabétique\n"
                       "2 - Lister par classement\n"
                       "Entrez votre choix : ")
            choice = view.display_in(message)
            if choice in {'1', '2'}:
                break
            else:
                message = ("Choix invalide. Entrez un chiffre compris "
                           "entre 1 et 2")
                view.display_out(message)
        except ValueError:
            message = ("Choix invalide. Entrez un chiffre compris "
                       "entre 1 et 2")
            view.display_out(message)
    if choice == '1':
        player_list = sorted(player_list, key=lambda x: x.surname,
                             reverse=False)
        player_list = sorted(player_list, key=lambda x: x.name,
                             reverse=False)
    if choice == '2':
        player_list = sorted(player_list, key=lambda x: x.ranking,
                             reverse=False)
    message = "ID | Nom            | Prénom           | Classement"
    view.display_out(message)
    for player in player_list:
        message = "%-4s %-16s %-16s %3s" % (player.t_id, player.name,
                                            player.surname,
                                            player.ranking)
        view.display_out(message)
    message = "Appuyez sur Entrée pour continuer..."
    view.display_in(message)


def option3():
    update_all_ranking()


def option4():
    if os.path.isfile('./db.json'):
        while True:
            try:
                message = ("Reprendre le tournoi en cours ? Vous ne pouvez pas"
                           " commencer un nouveau tournoi en parallèle. \n"
                           "1 - Oui\n"
                           "2 - Non, plus tard\n"
                           "3 - Supprimer les données du tournoi\n"
                           "Entrez le chiffre correspondant à votre choix : ")
                choice = view.display_in(message)
                if choice in {'1', '2', '3'}:
                    break
                else:
                    message = ("Choix invalide. Entrez un chiffre compris "
                               "entre 1 et 3")
                    view.display_out(message)
            except ValueError:
                message = ("Choix invalide. Entrez un chiffre compris "
                           "entre 1 et 3")
                view.display_out(message)
        if choice == '1':
            data = load_data()
            partial_tournament(data[0], data[1], data[2],
                               data[3], data[4], data[5], data[6])
        elif choice == '2':
            pass
        elif choice == '3':
            os.remove("db.json")
    else:
        player_list = create_player_list()
        create_tournament(player_list)


def option5():
    tournaments_list = display_all_tournaments()
    message = ("ID | Nom du Tournoi       | Lieu où s'est déroulé le "
               "tournoi | Date de début")
    view.display_out(message)
    i = 1
    for tournament in tournaments_list:
        message = "%-4s %-22s %-34s %5s" % (i, tournament.name,
                                            tournament.location,
                                            tournament.start_date)
        view.display_out(message)
        i += 1

    while True:
        try:
            message = "Entrez l'ID d'un tournoi pour plus de détails : "
            choice = int(view.display_in(message))
            if 0 < choice < len(tournaments_list) + 1:
                break
            else:
                message = "Erreur, veuillez entrer un choix valide."
                view.display_out(message)
        except ValueError:
            message = "Erreur, veuillez entrer un choix valide."
            view.display_out(message)

    while True:
        try:
            message = ("1 - Liste des joueurs du tournoi\n"
                       "2 - Liste des tours\n"
                       "3 - Liste des matchs\n"
                       "0 - Retour au menu\n"
                       "Entrez votre choix : ")
            choice2 = int(view.display_in(message))
            if choice2 in {0, 1, 2, 3}:
                break
            else:
                message = "Erreur, veuillez entrer un choix valide."
                view.display_out(message)
        except ValueError:
            message = "Erreur, veuillez entrer un choix valide."
            view.display_out(message)

    if choice2 == 1:
        while True:
            try:
                message = ("1 - Lister par ordre alphabétique\n"
                           "2 - Lister par classement\n"
                           "3 - Lister par total de points\n"
                           "Entrez votre choix : ")
                choice3 = int(view.display_in(message))
                if choice3 in {1, 2, 3}:
                    break
                else:
                    message = "Erreur, veuillez entrer un choix valide."
                    view.display_out(message)
            except ValueError:
                message = "Erreur, veuillez entrer un choix valide."
                view.display_out(message)
        display_tournament_data(choice, choice2, choice3)
    elif choice != 0:
        display_tournament_data(choice, choice2, 0)


def main_menu():
    while True:
        option = view.print_menu()
        if option == '1':
            option1()
        elif option == '2':
            option2()
        elif option == '3':
            option3()
        elif option == '4':
            option4()
        elif option == '5':
            option5()
        elif option == '6':
            message = "Fermeture du programme"
            view.display_out(message)
            exit()
        else:
            message = "Choix invalide. Entrez un chiffre compris entre 1 et 6"
            view.display_out(message)
