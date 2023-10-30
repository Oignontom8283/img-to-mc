from img_to_mc import image as itmImage

image = itmImage.load_file('test_image/image2.jpg')

def Convert_progress(x, y, color, progress, nomber_pixls):
    print(f'x:{str(x):4} y:{str(y):4} ; {str(color):20} ; {progress}/{str(nomber_pixls):5} = {progress/nomber_pixls*100}%')

debug_info = False
image_formate = image.Convert(2, 3.5, 'normal', 60, 0.8, Print_progress_info=debug_info, progress_connect=Convert_progress)

# print(image_formate.get_content())

print(image_formate.save('function.mcfunction'))


























# import sys
# from PyQt5.QtWidgets import QApplication, QFileDialog

# def save(content):
#     app = QApplication(sys.argv)
    
#     options = QFileDialog.Options()
#     options |= QFileDialog.ReadOnly  # Pour enregistrer en mode écriture

#     # Spécifiez le nom de fichier par défaut dans le dernier argument
#     file_path, _ = QFileDialog.getSaveFileName(None, "Enregistrer le fichier", "mon_fichier.txt", "Fichiers texte (*.txt);;Tous les fichiers (*)", options=options)
    
#     if file_path:
#         try:
#             with open(file_path, 'w') as file:
#                 file.write(content)
#             print(f"Fichier enregistré avec succès à l'emplacement : {file_path}")
#         except IOError as e:
#             print(f"Erreur lors de l'enregistrement du fichier : {str(e)}")
#     else:
#         print("Annulation de l'enregistrement")

# # Exemple d'utilisation
# content = "Ceci est le contenu de mon fichier."
# save(content)
