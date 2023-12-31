import os

from args import command_line_arguments
from img_to_mc import image, object


argv = command_line_arguments(object.itm_Image.Convert, [
        'progress_connect',
        'finish_connect',
        'error_connect'
    ],
    {
        'image_file': (str, command_line_arguments.OBLIGATORY),
        'save_file': (str, './output/{img_name}.mcfunction')
    }
)


all_args = argv.get_arguments()
other_args = argv.get_otherArgs()
funct_args = argv.get_functArgs()

image_file_path = other_args['image_file']
save_file_path = other_args['save_file'].format(img_name=os.path.splitext(os.path.basename(image_file_path))[0])


imaget = image.load_file(image_file_path)

def Convert_progress(x, y, color, progress, nomber_pixls):
    print(f'x:{str(x):4} y:{str(y):4} | {str(color):20} | {progress}/{str(nomber_pixls):5} = {progress/nomber_pixls*100} %')

def Convert_finish(number_pixels):
    print(f"Programme finish | Total particles : {number_pixels}")

def Convert_error(e):
    print(f'ERROR : {e}')

image_formate = imaget.Convert(**funct_args ,progress_connect=Convert_progress, finish_connect=Convert_finish, error_connect=Convert_error)


save_success = image_formate.save(save_file_path)

# Si l'anre
if save_success:

    if os.path.exists(save_file_path) and os.path.getsize(save_file_path) > 0:
        print(f'The process went well. The result was saved in "{os.path.abspath(save_file_path)}"')

    else:
        print(f"An error has occurred. The {save_file_path} file was not saved or is empty.")

else:
    print(f"An error occurred when saving the {save_file_path} file")