# Uso de mypy para validar los errores de tipo.
# Se utiliza instalando la librería y ejecutando lo siguiente en consola
# mypy palindrome.py --check-untyped-defs

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(is_palindrome(100))


if __name__ == '__main__':
    run()