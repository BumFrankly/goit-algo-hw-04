import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def list_files_and_directories(directory):

    print(Fore.BLUE + f"Директорія: {directory}")

    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.GREEN + f"  {item.name}/")
            list_files_and_directories(item)
        elif item.is_file():
            print(Fore.RED + f"  {item.name}")

def main():
    if len(sys.argv) != 2:
        print("Потрібно вказати шлях до директорії") #python test3.py C:\Users\Dimon\Documents\GitHub\goit-algo-hw-04
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists() or not directory_path.is_dir():
        print("Вказаний шлях не існує або не є директорією.")
        return

    list_files_and_directories(directory_path)

if __name__ == "__main__":
    main()
 