#Canelle Wagner, 20232321
#Alex Maggioni, Matricule

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size
        self.image_folder = "images_pays" # images_pays ou images
        self.result_folder = "results_pays" # results_pays ou results

    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        # TODO
        # a completer
            
        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            
        # lecture des images à partir du dossier "images" : "1.png2, "2.png", "3.png", ... "<N>.png"   
        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)

        with open(cards_file, 'r') as f:
            cards = [line.strip().split() for line in f]

        # placement des images sur les cartes visuelles, rotations apreciees
        # ajout de la bordure sur les cartes visuelles
        for card_index, symbols in enumerate(cards, 1):
            # Calculate grid dimensions
            grid_rows = grid_cols = int(math.ceil(math.sqrt(len(symbols))))
            # Pour être plus esthétique avec par exemple 6 symboles par carte, veillez décommenter la ligne suivante 
            #grid_rows = math.ceil(len(symbols)/grid_cols)

            card_image = Image.new('RGB', (grid_cols*self.pic_size + 2* self.border_size , grid_cols*self.pic_size + 2* self.border_size), 'white')

            for index, symbol in enumerate(symbols):
                # Calculer la position
                col = index % grid_cols
                row = index // grid_rows
                x = self.border_size + col * self.pic_size
                y = self.border_size + row * self.pic_size

                # Ouvrir l'image
                image_path = os.path.join(self.image_folder, f"{symbol}.png")
                symbol_image = Image.open(image_path)

                # Faire une rotation aléatoire de l'image
                rotated_symbol = symbol_image.rotate(random.randint(0, 360), expand=1)

                # Redimensionner l'image après rotation
                resized_symbol = rotated_symbol.resize((self.pic_size, self.pic_size))

                # Créer un masque pour la transparence en extrayant le canal alpha de l'image redimensionnée
                mask = resized_symbol.convert("RGBA").split()[-1] 

                # Coller le symbole (image) sur la carte
                card_image.paste(resized_symbol, (x, y), mask=mask)

            # sauvegarde des cartes dans le dossier "results" : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            filename = os.path.join(self.result_folder, f"card{card_index}.jpg")
            card_image.save(filename)

            if verbose:
                print(f"Card {card_index} saved as {filename}.")

# Test
#creator = Creator()
#creator.make_cards(verbose=True)

