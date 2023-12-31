# img-to-mc
  **FR** : Ce programme a pour but de à partir d'une image la convertir en une fonction Minecraft (.mcfunction pour les Data-pack) permettant l'affichage d'image dans le jeu.
  
  **AN** : The purpose of this program is to convert an image into a Minecraft function (.mcfunction for Data-pack) enabling image display in the game.


#### Warning :
> **AN** : Using too large a quantity of particles can cause lags and a very significant loss of FPS
> One or more images that are too resource-intensive can prevent the world from loading when it opens.


#### Avertissements :
> **FR** : L'utilisation d'une trop grande quantité de particule peut anthrène des lags est perte de FPS très conséquente 
> Une ou des images trop gourmandes en ressource peuvent empêcher le chargement du monde à son élancement
  
*************************************

### Project progress :

| Step              | Statue           |
|-------------------|------------------|
| Prototy           | Finish           |
| Backend           | Finish           |
| Use command line  | Finish           |
| GUI               | Not started      |
| Vidéo ?           | Food for thought |

*************************************

### Addiction

> The project requires [Python 3.6.3](https://www.python.org/downloads/release/python-363/) !

| Packages                                                            | Version |
|---------------------------------------------------------------------|---------|
| Pillow [ⓘ](https://pypi.org/project/Pillow/)                       | 8.4.0   |
| PyQt5 [ⓘ](https://pypi.org/project/PyQt5/)                         | 5.15.6  |
| typing [ⓘ](https://pypi.org/project/typing/)                       | 3.7.4.3 |
| typing_extensions [ⓘ](https://pypi.org/project/typing-extensions/) | 4.1.1   |


<div id="diaporama" style="max-width: 600px; position: relative; margin: auto;">
    <div class="mySlides" style="display: none;">
        <img src="https://raw.githubusercontent.com/votre-utilisateur/votre-repo/main/image1.jpg" style="width:100%">
    </div>

    <div class="mySlides" style="display: none;">
        <img src="https://raw.githubusercontent.com/Oignontom8283/img-to-mc/main/src/icon.ico" style="width:100%">
    </div>

    <!-- Ajoutez autant d'images que nécessaire -->

    <button class="prev" onclick="plusSlides(-1)" style="position: absolute; top: 50%; left: 10px; width: auto; padding: 16px; margin-top: -22px; font-size: 20px; font-weight: bold; color: white; background-color: black; border: none; cursor: pointer; border-radius: 5px;">❮</button>
    <button class="next" onclick="plusSlides(1)" style="position: absolute; top: 50%; right: 10px; width: auto; padding: 16px; margin-top: -22px; font-size: 20px; font-weight: bold; color: white; background-color: black; border: none; cursor: pointer; border-radius: 5px;">❯</button>

    <script>
        var slideIndex = 1;
        showSlides(slideIndex);

        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function showSlides(n) {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            if (n > slides.length) {
                slideIndex = 1;
            }
            if (n < 1) {
                slideIndex = slides.length;
            }
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            slides[slideIndex - 1].style.display = "block";
        }
    </script>
</div>

