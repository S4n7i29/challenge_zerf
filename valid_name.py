import re

VALID_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,254}$")

def is_valid_name(name: str) -> bool:
    """
    Devuelve True si 'name' cumple con el patrón:
      - No es '.' ni '..'
      - No contiene '/'
      - Sólo letras, números, '_' o '-'
      - Longitud 1–255
    """
    return bool(VALID_NAME.fullmatch(name))