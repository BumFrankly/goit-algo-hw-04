def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        raise ValueError("Не введено жодних даних")
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Будь ласка, введіть ім'я та номер телефону")
    name, phone = args
    if name in contacts:
        raise ValueError("Контакт вже існує")
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Будь ласка, введіть ім'я та новий номер телефону")
    name, phone = args
    if name not in contacts:
        raise ValueError("Контакт не існує")
    contacts[name] = phone
    return "Контакт успішно оновлено"

def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Будь ласка, введіть ім'я контакту")
    name = args[0]
    if name not in contacts:
        raise ValueError("Контакт не знайдено")
    return contacts[name]

def show_all(contacts):
    if not contacts:
        raise ValueError("Список контактів порожній")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Ласкаво просимо до асистента!")
    while True:
        try:
            user_input = input("Введіть команду: ")
            command, args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("До побачення!")
                break
            elif command == "hello":
                print("Як я можу вам допомогти?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_contact(args, contacts))
            elif command == "all":
                show_all(contacts)
            else:
                print("Неправильна команда.")
        except ValueError as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
