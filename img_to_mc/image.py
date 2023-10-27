from PIL import Image as PilImage, PngImagePlugin

from .object import itm_Image

def load(image):
    image = itm_Image(image)
    return image

def load_file(path:str):
    image_file = PilImage.open(path)

    image = itm_Image(image_file)

    return image