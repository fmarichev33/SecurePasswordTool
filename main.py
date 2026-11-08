from generator import generate_password
from analyzer import analyze_password


def main():
    print("===Генератор и анализатор паролей===")
    print("===Password generator & analyzer===")
    print("1. Сгенерировать новый пароль / Generate a new password")
    print("2. Проверить существующий пароль / Check an existing password")
    choice = input('\nВыберите действие (1 или 2): ').strip()
    if choice == "1":
        try:
            length = int(input("Введите длину пароля: "))
            pwd = generate_password(length)
            print(f'Сгенерированный пароль: {pwd}')
            result = analyze_password(pwd)
            print(f'Энтропия: {result['entropy']:.2f} бит')
            print(f'Время взлома: {result['time_str']}')
        except ValueError:
            print('Ошибка: введите корректное число!')

    elif choice == "2":
        pwd = input("\nВведите пароль для проверки: ")
        print(f'Сгенерированный пароль: {pwd}')
        result = analyze_password(pwd)
        print(f'Энтропия: {result['entropy']:.2f} бит')
        print(f'Время взлома: {result['time_str']}')

    else:
        print("Неверный выбор!")


if __name__ == "__main__":
    main()