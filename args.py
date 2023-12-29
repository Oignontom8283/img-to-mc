import argparse, inspect
from typing import Callable, Union

class command_line_arguments():

    OBLIGATORY = inspect.Parameter.empty

    def __init__(self, param_extract_func:Callable, excludParams:list, otherParams:dict) -> None:
        self.otherParams = otherParams
        self.excludParams = excludParams

        self.parser = argparse.ArgumentParser(usage='', description='')

        sign = inspect.signature(param_extract_func)
        funcParam_paramList = sign.parameters.items()


        # Mettre dans une liste tous les paramètres de conversion plus les autres sauf ceux exclus
        self.functParams = {}
        for setting_name, settings in funcParam_paramList:

            if setting_name not in self.excludParams and setting_name != 'self':

                type         = settings.annotation
                defaultValue = settings.default

                self.functParams[setting_name] = (type, defaultValue)


        self.script_settings = {}
        self.script_settings.update(self.functParams) # ajout des paramétre extrai de la fonction
        self.script_settings.update(otherParams) # ajouter des otherParam au param du programme


        # Définire la list des arguments du programme avec la list des param
        for key, settings in self.script_settings.items():

            name = key
            self.parser.add_argument(f'--{name}')


        # Récuper la valeur des paramétre donner par l'utilisateur
        self.Args = self.parser.parse_args()._get_kwargs()

        self._process_arg_types()
        self._sep_args()


    def _process_arg_types(self):
        
        convert_args = {}

        for arg_name, arg_value in self.Args:

            arg_type = self.script_settings[arg_name][0]
            arg_defaultValue = self.script_settings[arg_name][1]

            # Traiter le type des argument
            if arg_value == None  and  arg_defaultValue == inspect.Parameter.empty:
                raise ValueError(f"The argument '{arg_name}' is mandatory")

            else:

                # Si la valeur na été donner par l'utilisateur métre la valeur par default
                if arg_value == None  and  arg_defaultValue != None:
                    new_value = arg_defaultValue
                
                else:
                    new_value = arg_value
                
                # Si c'est un Union, essayer chaque type de l'Union jusqu'à trouver celui qui convient
                if hasattr(arg_type, "__origin__") and arg_type.__origin__ is Union: 
                    union_types = arg_type.__args__

                    converted = False

                    for union_type in union_types:
                        try:
                            new_value = union_type(new_value)
                            converted = True
                            break
                        except:
                            pass
                    if not converted:
                        raise SyntaxError(f"The value '{type(new_value)}' of argument '{arg_name}' does not match any type in the Union")
                
                # Gérer les autees types
                else:

                    try:
                        new_value = arg_type(new_value)

                    except Exception as e:
                        pass # Utiliser l'erreur pour le débogage si nécessaire.

                convert_args[arg_name] = new_value
        
        self.Args = convert_args
                        

    def _sep_args(self) -> None:
        
        self.other_Args = {}
        self.funct_Args = {}

        # Trier les Arguments obtenue en focntion de leur proveunance
        for name, value in self.Args.items():

            if name in self.otherParams:
                self.other_Args[name] = value

            elif name in self.functParams:
                self.funct_Args[name] = value

            else: raise ValueError(f'Il y a eu une erreur de listage. {name} n\'est pas catégorisé.')


    def get_arguments(self):
        return self.Args
    
    def get_functArgs(self):
        return self.funct_Args

    def get_otherArgs(self):
        return self.other_Args