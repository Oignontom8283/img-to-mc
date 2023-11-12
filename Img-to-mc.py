import argparse, inspect

from img_to_mc import image, object


#  =====================================
#     Handling command line arguments   
#  =====================================

excluded_parameters = [ # the parameters to exclude from the list of parameters
        'self',
        'progress_connect',
        'finish_connect',
        'error_connect'
    ]

parser = argparse.ArgumentParser(description="") # init scripts settings

signature = inspect.signature(object.itm_Image.Convert) # Recovery of parameters from the Convert function

convert_param_list = signature.parameters.items()

# put in a list all Convert parameters plus others except those excluded
script_settings = []
for setting_name, settings in convert_param_list:

    if setting_name not in excluded_parameters:

        name    = setting_name
        type    = settings.annotation
        default = settings.default

        script_settings.append([name, type, default])

# add others parameter
script_settings.append(['gui', bool, None]) 


# Define command ligne options
for setting in script_settings:
    
    name = setting[0]

    parser.add_argument(f'--{name}')



#  ==================
#     Test section   
#  ==================

# Get the arguments
args = parser.parse_args()

print(f'\nargument {args._get_kwargs()}\n')