import argparse

from image_crawler import download_images
from image_processor import create_annotation, ImageIterator, clear_directory


def parse_arguments() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки.
    
    Returns:
        argparse.Namespace: объект с параметрами:
            - keyword (str): поисковый запрос
            - save_dir (str): директория для сохранения изображений
            - annotation (str): путь к файлу аннотаций
            - num_images (int): количество изображений для загрузки
    """
    parser = argparse.ArgumentParser(description='Загрузка изображений по ключевому слову')
    parser.add_argument('--keyword', default='snake', help='Поисковый запрос')
    parser.add_argument('--save_dir', default='images', help='Директория для сохранения')
    parser.add_argument('--annotation', default='annotation.csv', help='Путь к файлу аннотаций')
    parser.add_argument('--num_images', type=int, default=100, help='Количество изображений')
    
    return parser.parse_args()


def main() -> None:
    """
    Основная функция программы.
    Координирует процесс загрузки изображений и создания аннотаций.
    """
    args = parse_arguments()
    
    clear_directory(args.save_dir)
    
    print(f"\nНачинаю загрузку {args.num_images} изображений для запроса '{args.keyword}'...")
    
    download_images(args.keyword, args.save_dir, args.num_images)
    create_annotation(args.save_dir, args.annotation)

    print("\nДемонстрация работы итератора:")
    iterator = ImageIterator(args.annotation)
    for i, image in enumerate(iterator):
        print(f"Изображение {i + 1}:")
        print(f"Относительный путь: {image['relative_path']}")
        print(f"Абсолютный путь: {image['absolute_path']}\n")


if __name__ == '__main__':
    main()