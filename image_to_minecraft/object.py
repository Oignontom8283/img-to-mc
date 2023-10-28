from typing import Union
from typing_extensions import Literal

from . import _config

from PIL import Image as PilImage

class itm_Image():

    def __init__(self, image) -> None:
        
        try:
            image_format = image.convert("RGBA")
            print(f'type : {type(image_format)}')

            self.image = image_format

        except Exception as e:
            raise TypeError(f'File is not conpatible Error : {e}')


    def Convert(self,
            DefaultImage:PilImage.Image,
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
            Print_progress_info: bool = False
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


        largeur, hauteur = DefaultImage.size

        Content_file = ''

        for x in range(largeur):
            for y in range(hauteur):

                color = DefaultImage.getpixel((x, y))

                if color[3] != 0:
                    
                    red = color[0]   / 255
                    green = color[1] / 255
                    blue = color[2]  / 255

                pixX = map_value(x, largeur, image_largeur)
                pixY = -map_value(y, hauteur, image_hauteur) + image_hauteur

                Content_file = Content_file + f'{_config.command_DisplayParticle} {_config.id_ParticleDisplay} {red} {green} {blue} {particle_size} ^ ^{pixY} ^{pixX} {particle_axe_X} {particle_axe_Y} {particle_axe_Z} {particle_speed} {particle_count} {particle_mod} {particle_visibility_selector}\n'

                

        pass

class itm_ImgMinecraft():

    def __init__(self) -> None:
        pass

    def save(self):
        pass

    def get_file_content(self):
        pass