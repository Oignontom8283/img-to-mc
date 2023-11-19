import argparse, inspect

from img_to_mc import image, object



program_description = ""


#  =====================================
#     Handling command line arguments   
#  =====================================

excluded_parameters = [ # the parameters to exclude from the list of parameters
        'self',
        'progress_connect',
        'finish_connect',
        'error_connect'
    ]

parser = argparse.ArgumentParser(description='') # init scripts settings

signature = inspect.signature(object.itm_Image.Convert) # Recovery of parameters from the Convert function

convert_param_list = signature.parameters.items()


# put in a list all Convert parameters plus others except those excluded
script_settings = {}
for setting_name, settings in convert_param_list:

    if setting_name not in excluded_parameters:

        name    = setting_name
        type    = settings.annotation
        default = settings.default

        script_settings[name] = (type, default)

# add others parameter
script_settings["gui"] = (bool, False)


# Define command ligne options
for key, setting in script_settings.items():
    
    Name = key

    parser.add_argument(f'--{Name}')



#  ======================
#       Test section   
#  ======================


args = parser.parse_args()
args = args._get_kwargs()

print(script_settings)
print()

# Traiter les argument
convert_args = {}
for param_name, value in args:
    default_value = script_settings[param_name][1]
    param_type = script_settings[param_name][0]

    print()
    print(f'Value : {value}')
    print(f'param_name : {param_name}')
    print(f'default_value : {type(default_value)}')
    print(f'param_type : {param_type}')

    if default_value == inspect._empty and value == None:
        raise ValueError(f"The argument '{param_name}' is mandatory")

    if value == None and default_value != None:
        new_value = default_value
    else:
        new_value = value

    try:
        new_value = param_type(new_value)
    except:
        raise SyntaxError(f"The value '{new_value}' of argument '{param_name}' is not type '{param_type}'")

    convert_args[param_name] = new_value


# print('')
# print(f'Default arguments : {script_settings}')
# print('')
# print(f'Argument get : {args}')
# print('')
# print(f'Finish argument : {convert_args}')




# imaget = image.load_file('test_image/image2.jpg')

# def Convert_progress(x, y, color, progress, nomber_pixls):
#     print(f'x:{str(x):4} y:{str(y):4} | {str(color):20} | {progress}/{str(nomber_pixls):5} = {progress/nomber_pixls*100} %')

# def Convert_finish(number_pixels):
#     print(f"programme finish | Total pixels : {number_pixels}")

# def Convert_error(e):
#     print(f'ERROR : {e}')

# image_formate = imaget.Convert( ,progress_connect=Convert_progress, finish_connect=Convert_finish, error_connect=Convert_error)


# print(image_formate.save('function.mcfunction'))
