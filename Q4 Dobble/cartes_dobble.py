#CE FICHIER NE SERT QU'A APPELER ET TESTER VOTRE CODE. 
#VOUS NE DEVRIEZ PAS AVOIR BESOIN DE LE MODIFIER, SAUF POUR 
#AJOUTER VOUS-MÊME D'AUTRES TESTS SI VOUS LE VOULEZ.
#NE PAS REMETTRE SUR STUDIUM. REMETTEZ SEULEMENT dobble_generator.py, dobble_verificator.py et dobble_creator.py

#THIS FILE IS ONLY USED TO CALL AND TEST YOUR CODE.
#YOU SHOULD NOT HAVE TO MODIFY IT, EXCEPT FOR ADDING 
#NEW CUSTOM TESTS IF YOU WISH TO DO SO.
#DO NOT SUBMIT ON STUDIUM. ONLY SUBMIT dobble_generator.py, dobble_verificator.py and dobble_creator.py

import dobble_generator
import dobble_verificator
import dobble_creator
import sys
import os.path

def test_general():
    card_verificator = dobble_verificator.Verificator()
    success = True 

    # test du verificateur de cartes
    # cards verificator test
    input_tests = [("cartes_test1.txt",0),
                   ("cartes_test2.txt",1),
                   ("cartes_test3.txt",2),
                   ("cartes_test4.txt",2),
                   ("cartes_test5.txt",1),
                   ("cartes_test6.txt",0)]
    for tested_input, expected_return in input_tests :
        verification_result = card_verificator.verify(tested_input, False)
        if verification_result == expected_return :
            print("Test reussis / Test passed")
        else :
            print("Echec du test / Failed test")
            success = False

    # test du generateur de cartes
    # cards generator test
    cards_file = "cartes.txt"
    order_tests = [(3,0),(4,2),(5,0),(6,2),(7,0)]
    for tested_order, expected_return in order_tests :
        # generation des cartes
        # cards generation
        card_generator = dobble_generator.Generator(tested_order)
        card_generator.generate(cards_file)

        # verification des cartes
        # cards verification
        verification_result = card_verificator.verify(cards_file, False)
        if verification_result == expected_return :
            print("Test reussis / Test passed")
        else :
            print("Echec du test / Failed test")
            success = False

    # test du createur de cartes
    # cards creator test
    if os.path.isdir("./results") :
        print("Test reussis / Test passed")
        if os.path.isfile("./results/card1.jpg") :
            print("Test reussis / Test passed")
        else :
            print("Echec du test / Failed test")
            success = False
    else :
        print("Echec du test / Failed test")
        success = False

    return success


if __name__ == '__main__':

    # pour tester le jeu
    # to test the game
    test_general()
    
    # lecture de l'entree de l'utilisateur
    # reading user input
    args = sys.argv[:]
    order = 7
    if len(args) >= 2 :
        order = int(args[1])
    cards_file = "cartes.txt"

    # generation des cartes
    # card generation
    card_generator = dobble_generator.Generator(order)
    card_generator.generate(cards_file, True)

    # verification des cartes
    # card verification
    card_verificator = dobble_verificator.Verificator()
    verification_result = card_verificator.verify(cards_file, True)

    if verification_result == 2 :
        print("Échec de la génération des cartes / Failed to generate cards")
    else :
        if verification_result == 1 :
            print("Avertissements lors de la génération des cartes / Warnings when generating cards")
        # creation des cartes visuelles
        # creation of visual cards
        card_creator = dobble_creator.Creator(300,10)
        card_creator.make_cards(cards_file, True)


