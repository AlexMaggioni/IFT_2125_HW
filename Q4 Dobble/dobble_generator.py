#Canelle Wagner, 20232321
#Alex Maggioni, Matricule

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random # pour le melange des symboles sur chaque carte # for mixing symbols on each card

class Generator():
    def __init__(self, order = 7):
        self.order = order

    def generate(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Generation des cartes***")

        # TODO
        # a completer

        # melange aleatoire des symboles sur les cartes,
        # pour ne pas avoir des répétitions de symboles sur les mêmes endroits des cartes
        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards

        n = self.order
        self.total_symbols = n**2 + n + 1 # n2 + n + 1 cartes et symboles au total pour que le jeu soit considéré optimal  
        self.cards = []

        # Générer la carte de base (de 1 à n+1)
        # n + 1 symboles au total
        base_card = list(range(1, n + 2)) # rappel : (n + 2) et non (n + 1) car la borne supérieure dans la fonction range est exclusive
        self.cards.append(base_card)


        # Générer les n groupes de n cartes
        for i in range(n):
            for j in range(n):
                # Chaque carte contiendra un symbole de la carte de base
                card = [base_card[i]]
                # Ajouter n symboles à la carte, en s'assurant qu'il n'y a pas de répétitions et que chaque symbole est unique dans le jeu
                for k in range(n):
                    # Calculer le symbole à ajouter à la carte
                    # (n + 2) est le début de l'index des symboles supplémentaires (après ceux de la carte de base)
                    # (n * k) avance de n positions à chaque fois pour éviter les répétitions
                    # ((i * k + j) % n) assure que chaque carte a exactement un symbole en commun avec chaque autre carte
                    symbol = (n + 2) + (n * k) + ((i * k + j) % n)
                    card.append(symbol)
                self.cards.append(card)

        # Générer le dernier ensemble de cartes
        for i in range(n) : 
            # Commencer chaque nouvelle carte avec le dernier symbole de la carte de base
            card = [base_card[-1]]
            for j in range(n) : 
                # Calculer le symbole à ajouter à la carte
                # n+2 est le point de départ après les symboles de la carte de base
                # j s'incrémente pour parcourir les symboles suivants
                # i*n décale l'indice de n places pour chaque nouveau groupe de cartes généré
                symbol = n+2 + j + i*n
                card.append(symbol)
            self.cards.append(card)

        # Mélanger les symboles 
        for card in self.cards:
            random.shuffle(card)

        # Mélanger les cartes
        random.shuffle(self.cards)

        # TODO
        # a completer


        # ecriture des cartes dans le fichier cards_file
        # writing cards in the cards_file file
            
        with open(cards_file, 'w') as f:
            for card in self.cards:
                f.write(' '.join(str(symbol) for symbol in card) + '\n')

            
        # TODO
        # a completer
        if verbose:
            print(f"{len(self.cards)} cartes générées avec succès et écrites dans {cards_file}")

        return self.cards
    
# Test
#generator = Generator(order=7)
#cards_3 = generator.generate(verbose=True)


