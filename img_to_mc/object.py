from typing import Union, Callable
from typing_extensions import Literal

from PIL import Image as PilImage

_files_credits = 'This image generation function in minecraft was created with img-to-mc'

class itm_Image():

    def __init__(self, image) -> None:
        
        try:
            image_format = image.convert("RGBA")

            self.image = image_format

        except Exception as e:
            raise TypeError(f'File is not conpatible | Error : {e}')

    def Convert(self,
            image_largeur: Union[int, float],
            image_hauteur: Union[int, float],
            particle_mod: Literal['force', 'normal'],
            image_resolution: Union[int, float] = 50.0,
            particle_size: Union[int, float] = 1.0,
            particle_speed: Union[int, float] = 0.005,
            particle_count: int = 1,
            particle_axe_X: Union[int, float] = 0.05,
            particle_axe_Y: Union[int, float] = 0.05,
            particle_axe_Z: Union[int, float] = 0.05,
            particle_visibility_selector: str = '@a',
            particle_id: str = 'minecraft:dust', # Identify the particle to use for display
            particle_command: str = 'particle', # Minecraft command to display particles
            Print_progress_info: bool = False,
            progress_connect: Callable = None,
            finish_connect: Callable = None
            ):

        def map_value(
                valeur_initiale,
                plage_max,
                nouvelle_max,
                plage_min = 0,
                nouvelle_min = 0,
            ):
            valeur_convertie = (valeur_initiale - plage_min) * (nouvelle_max - nouvelle_min) / (plage_max - plage_min) + nouvelle_min
            return valeur_convertie
        
        DefaultImage:PilImage.Image = self.image

        default_largeur, default_hauteur = DefaultImage.size

        # init Image after resizeing
        FormatImage = DefaultImage.resize(( round(image_resolution/100 * default_largeur), round(image_resolution/100 * default_hauteur) )) # resize the image to the resolution indicated
        format_largeur, format_hauteur = FormatImage.size
        format_number_pixels = format_largeur * format_hauteur

        #DefaultImage.save('../debug.png')

        Content_file = f'# {_files_credits}\n'
        Progress_counte = 0
        for x in range(format_largeur):
            for y in range(format_hauteur):

                color = FormatImage.getpixel((x, y))

                if color[3] != 0:
                    
                    red = color[0]   / 255
                    green = color[1] / 255
                    blue = color[2]  / 255

                    pixX = map_value(x, format_largeur, image_largeur)
                    pixY = -map_value(y, format_hauteur, image_hauteur) + image_hauteur

                    # append value to content
                    Content_file = Content_file + f'{particle_command} {particle_id} {red} {green} {blue} {particle_size} ^ ^{pixY} ^{pixX} {particle_axe_X} {particle_axe_Y} {particle_axe_Z} {particle_speed} {particle_count} {particle_mod} {particle_visibility_selector}\n'

                    Progress_counte = Progress_counte + 1
                    if Print_progress_info == True: print(f"Coordonnées : ({x}, {y}), Couleur : {color}, Progress : {Progress_counte}/{format_number_pixels}")

                    if progress_connect != None: progress_connect(x, y, color, Progress_counte, format_number_pixels)

        Content_file = Content_file + f'# {_files_credits}\n'
        return itm_ImgMinecraft(Content_file)

class itm_ImgMinecraft():

    def __init__(self, file_content) -> None:
        self.content = file_content

    def save(self, file_path:str):
        """
        If the function was executed correctly without any problems, it returns True.
        If the function was not executed correctly or if there were problems, it returns the error that occurred.
        """

        try:
            with open(file_path, 'w') as file:
                file.write(self.content)

            return True

        except IOError as e:
            return e
        

    def get_content(self):
        return self.content