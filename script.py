import argparse
import re
from collections import Counter
from typing import List


def parse_arguments() -> argparse.Namespace:
    """
    Парсит аргументы командной строки.

    :return: Namespace с аргументами.
    """
    parser = argparse.ArgumentParser(description="Анализ популярных кодов операторов в номерах телефонов.")
    parser.add_argument('file', type=str, help='Путь к файлу с данными анкет.')
    return parser.parse_args().file


def read_file(file_path: str) -> List[str]:
    """
    Читает строки из указанного файла.

    :param file_path: Путь к файлу.
    :return: Список строк из файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except Exception as e:
         raise Exception(f"Ошибка при чтении файла: {e}")
        


def extract_operator_codes(lines: List[str]) -> List[str]:
    """
    Извлекает коды операторов из номеров телефонов.

    :param lines: Список строк из файла.
    :return: Список кодов операторов.
    """
    operator_codes = []
    # Обновлённое регулярное выражение для соответствия форматам номеров в data.txt
    phone_pattern = re.compile(r'\+7\s*(\d{3})[-\s]*\d{3}[-\s]*\d{2}[-\s]*\d{2}')

    for line in lines:
        match = phone_pattern.search(line)
        if match:
            operator_code = match.group(1)
            operator_codes.append(operator_code)
            print(f"Найден номер: {match.group(0)} -> Код оператора: {operator_code}")  # Отладочный вывод
        else:
            if "Номер телефона" in line:
                print(f"Не удалось найти номер в строке: {line.strip()}")  # Отладочный вывод
    return operator_codes


def find_most_common_code(codes: List[str]) -> str:
    """
    Находит наиболее частый код оператора.

    :param codes: Список кодов операторов.
    :return: Наиболее частый код.
    """

    counter = Counter(codes)
    most_common = counter.most_common(1)[0]
    return most_common[0]


def main():
    """
    Основная функция программы.
    """
    file = parse_arguments()
    try:
        lines = read_file(file)
        print(f"Прочитано строк: {len(lines)}")  # Отладочный вывод
        codes = extract_operator_codes(lines)
        print(f"Извлечено кодов операторов: {len(codes)}")  # Отладочный вывод

        if codes:
            print(f"Коды операторов: {codes}")  # Отладочный вывод
        else:
            return print(f"Коды телефонов не найдены.")
        
        most_common_code = find_most_common_code(codes)
        print(f"Наиболее распространенный код оператора: {most_common_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
