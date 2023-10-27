from img_to_mc import image as itmImage

image = itmImage.load_file('image2.jpg')

debug_info = False
image_formate = image.Convert(3, 3, 'normal', 100, 0.8, Print_progress_info=debug_info)

print(image_formate.get_content())

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
