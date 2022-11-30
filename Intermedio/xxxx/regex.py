import re


class Regex:
    def __init__(
        self,
    ):
        pass

    def regex_nom(nombre):
        cadena = nombre
        patron = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
        if re.match(patron, cadena):
            print(nombre)
            return True 
        else:
            print("Nombre Invalido")
            return False


#ob_re = Regex.regex_nom("nombre")
