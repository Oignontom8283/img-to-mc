
AN :
Guide to using Img-to-mc from the command line !

To use this application in its command line version, you will need to provide command line arguments to the executable.
To obtain the list of available arguments, give the --help argument to obtain a help message which contains the list of application arguments.
Example: Img-to-mc.exe --help

Img-to-mc is compatible with fully transparent pixels!

To use the application, the --image_width and --image_height arguments must be given with the dimensions of the image in the game (in blocks). 
You must also give the --image_file argument the green path, the file of your image to convert. If you have not given an output file, 
the result will by default be saved in a .mcfunction file with the image name in the output folder.
Example run command: Img-to-mc.exe --image_width 5 --image_height 5 --image_file ".\path\to\your\image.png"

It is advisable to use the --image_resolution (1.0 - 100.0) argument, to adjust the image resolution in the game. 
To limit performance losses, it is advisable to adjust the image_resolution parameter so that your number 
total pixels are less than or equal to approximately 1200 pixels.


For any questions or if you have a problem, use the discussions category of the GitHub repository,
and choose the discussions that best suits you to communicate. → https://github.com/Oignontom8283/img-to-mc/discussions


*************************************************************************************************************************************************************


FR :
Guide d'utilisation de Img-to-mc en ligne de commande !

Pour utiliser cette application dans sa version en ligne de commande, vous devrez fournir des arguments en ligne de commande à l'exécutable.
Pour obtenir la liste des arguments disponibles, donner l'argument --help afin d'obtenir un message d'aide qui contient la liste des arguments de l'application.
Exemple : Img-to-mc.exe --help

Img-to-mc est compatible avec les pixels totalement transparents !

Pour utiliser l'application, les arguments --image_width et --image_height doivent impérativement être donné avec les dimensions de l'image dans le jeu (en blocs).
Vous devez également impérativement donner à l'argument --image_file le chemin vert, le fichier de votre image à convertir. 
Si vous n'avez pas donné de fichier de sortie, le résultat sera par défaut enregistré dans un fichier .mcfunction avec le nom de l'image dans le dossier output. 
Exemple de commande d'exécution : Img-to-mc.exe --image_width 5 --image_height 5 --image_file ".\chemin\vers\votre\image.png"

Il est conseiller d'utiliser l'argument --image_resolution (1.0 - 100.0), 
Pour ajuster la résolution de l'image dans le jeu. Pour limiter les pertes de performance, 
il est conseiller d'ajuster le paramètre image_resolution pour que votre nombre de pixels total sois inférieure ou égale à environ 1200 pixels.


Pour toutes questions ou si vous avez un problème, utilisé la catégorie discutions du dépôt GitHub, 
et choisissez-la discutions qui vous convient le mieux pour communiquer. → https://github.com/Oignontom8283/img-to-mc/discussions