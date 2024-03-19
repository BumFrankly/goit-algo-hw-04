def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_data = line.strip().split(',')
                    if len(cat_data) == 3:
                        cat_info = {
                            "id": cat_data[0],
                            "name": cat_data[1],
                            "age": cat_data[2]
                        }

                        cats_info.append(cat_info)
                    else:
                        raise ValueError("Формат введення даних не вірний, потрібно: ID, Name, Age")
                except ValueError as ve:
                    print(ve)

    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Виникла помилка:", e)
    
    return cats_info

cats_info = get_cats_info("task2\cats_file.txt")
for cat in cats_info:
    print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")
