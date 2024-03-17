def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            num_developers = 0
            for line in file:
                data = line.strip().split(',')
                if len(data) == 2:
                    try:
                        salary = int(data[1])
                        total_salary += salary
                        num_developers += 1
                    except ValueError:
                        print(f"Помилка: Некоректне значення заробітної плати у рядку, введіть ціле число: {line.strip()}")
                else:
                    print(f"Помилка: Некоректний формат рядка у вашому файлі із данними працівників: {line.strip()}")

        if num_developers > 0:
            average_salary = total_salary / num_developers
            return total_salary, average_salary
        else:
            return 0, 0 

    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print("Помилка: Файл не знайдено, створіть файл із данними працівників")
        else:
            print(f"Помилка: {e}")
        return None, None

total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

