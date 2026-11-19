from generator import generate_password
from analyzer import analyze_password
from pattern_generator import generate_pattern, draw_pattern


def main():
    print("===Генератор и анализатор паролей. Генератор графических ключей===")
    print("===Password generator & analyzer. Pattern generator===")
    print("1. Сгенерировать новый пароль / Generate a new password")
    print("2. Проверить существующий пароль / Check an existing password")
    print("3. Сгенерировать графический ключ (Android) / Generate a pattern (Android)")
    print("Нажмите 0, чтобы выйти из программы / Press 0 to exit")
    while True:
        choice = input('\nВыберите действие (1, 2 или 3): ').strip()
        if choice == "1":
            try:
                length = int(input("Введите длину пароля: "))
                pwd = generate_password(length)
                print(f'Сгенерированный пароль: {pwd}')
                result = analyze_password(pwd)
                print(f'Энтропия: {result['entropy']:.2f} бит')
                print(f'Время взлома: {result['time_str']}')
                print("Нажмите 0, чтобы выйти из программы / Press 0 to exit")
            except ValueError:
                print('Ошибка: введите корректное число!')

        elif choice == "2":
            pwd = input("\nВведите пароль для проверки: ")
            print(f'Сгенерированный пароль: {pwd}')
            result = analyze_password(pwd)
            print(f'Энтропия: {result['entropy']:.2f} бит')
            print(f'Время взлома: {result['time_str']}')
            print("Нажмите 0, чтобы выйти из программы / Press 0 to exit")

        elif choice == '3':
            min_len = int(input("Минимальная длина ключа (4-9, по умолчанию 5): ") or 5)
            max_len = int(input("Максимальная длина ключа (4-9, по умолчанию 8): ") or 8)

            # Защита от некорректных границ
            min_len = max(4, min(9, min_len))
            max_len = max(min_len, min(9, max_len))

            pattern = generate_pattern(min_len=min_len, max_len=max_len)
            print(f"\nПоследовательность точек: {' -> '.join(map(str, pattern))}")

            draw_pattern(pattern, filename="pattern.png", show=True)
            print("Схема сохранена в pattern.png и открыта на экране.")
            print("Нажмите 0, чтобы выйти из программы / Press 0 to exit")

        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
