from PIL import Image as PilImage, PngImagePlugin

from .object import itm_Image, itm_ImgMinecraft

def load(image):
    image = itm_Image(image)
    return image

def load_file(path:str):
    image_file = PilImage.open(path)

    image = itm_Image(image_file)

    return image