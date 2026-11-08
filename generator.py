import secrets
import string


def generate_password(length: int, use_symbols: bool = True) -> str:
    """Генерирует криптографически стойкий пароль заданной длины"""
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if use_symbols:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password