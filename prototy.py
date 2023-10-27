from PIL import Image

def reduction(
        valeur_initiale,
        plage_max,
        nouvelle_max,
        plage_min = 0,
        nouvelle_min = 0,
    ):
    valeur_convertie = (valeur_initiale - plage_min) * (nouvelle_max - nouvelle_min) / (plage_max - plage_min) + nouvelle_min
    return valeur_convertie

resolution = 4.5
taille_largeur = 7   #10/3ty
taille_hauteur = 9 #17.5/3


image = Image.open("nuit.jpg")
print(type(image))


largeur, hauteur = image.size

image_format = image.resize((round( resolution/100 * largeur ), round( resolution/100 * hauteur )))
image = image_format.convert("RGBA")
largeur, hauteur = image.size
image_format.save("image_test.png")


with open("./function.mcfunction", "w+") as file:

    # Parcourir chaque pixel de l'image
    counte = 0
    for x in range(largeur):
        for y in range(hauteur):

            couleur = image.getpixel((x, y))

            if couleur[3] != 0:
                # Obtenir la couleur du pixel
                red = couleur[0] / 255
                green = couleur[1] / 255
                blue = couleur[2] / 255

                # Afficher la couleur et les coordonnées
                counte += 1
                print(f"Coordonnées : ({x}, {y}), Couleur : {couleur},  {counte}")

                pixX = reduction(x, largeur, 4)
                pixY = -reduction(y, hauteur, 3) + 3

                file.write(f"particle minecraft:dust {red} {green} {blue} 0.8 ~ ~{pixY} ~{pixX} 0.05 0.05 0.05 0.005 1 force @a\n")

            pass

file.close()
image.close()
