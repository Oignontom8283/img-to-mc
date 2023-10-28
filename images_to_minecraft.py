from PIL import Image as PilImage, PngImagePlugin


class Image:


    def load(self, Image):
        image = images_to_minecraft_Img(Image)
        return image

    def load_file(self, path:str):
        image_file = PilImage.open(path)

        image = images_to_minecraft_Img(image_file)

        return image


class images_to_minecraft_Img():

    def __init__(self, image) -> None:
        
        try:
            image_format = image.convert("RGBA")
        except Exception as e:
            raise TypeError(f'File is not conpatible Error : {e}')


        self.image = image_format


    def Convert(self):
        print(f'convert {self.image}')


class itm_ImgMinecraft():

    def __init__(self) -> None:
        pass

    def save(self):
        pass

    def get_file_content(self):
        pass