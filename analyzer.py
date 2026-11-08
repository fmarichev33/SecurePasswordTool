import math
import string


def get_alphabet_size(password):
    """Определяет размер алфавита N в зависимости от того, какие символы есть в пароле"""
    n = 0
    if any(c in string.ascii_lowercase for c in password):
        n += 26
    if any(c in string.ascii_uppercase for c in password):
        n += 26
    if any(c in string.digits for c in password):
        n += 10
    if any(c in string.punctuation for c in password):
        n += len(string.punctuation)
    return max(n, 1)


def calculate_entropy(password):
    L = len(password)
    if L == 0:
        return 0.0

    N = get_alphabet_size(password)
    E = L * math.log2(N)
    return E

def format_time(seconds):
    """Переводит секунды в человекочитаемый формат"""
    if seconds < 1:
        return "мгновенно"
    elif seconds < 60:
        return f"{int(seconds)} сек."
    elif seconds < 3600:
        return f"{int(seconds / 60)} мин."
    elif seconds < 86400:
        return f"{int(seconds / 3600)} ч."
    elif seconds < 31536000:
        return f"{int(seconds / 86400)} дн."
    elif seconds < 31536000 * 1000:
        years = seconds / 31536000
        return f"{int(years)} лет"
    else:
        return "триллионы лет (практически вечно)"


def analyze_password(password: str):
    """Анализирует пароль и возвращает структурированный результат"""
    entropy = calculate_entropy(password)
    speed = 10 ** 10  # 10 млрд попыток в секунду
    time_seconds = (2 ** entropy) / speed

    return {
        "entropy": entropy,
        "time_str": format_time(time_seconds)
    }