from data_loader import create_dataframe
from image_processor import add_image_info
from visualizer import setup_display_options, create_histogram

import os


def main():
    # Настраиваем отображение
    setup_display_options()
    
    # Создаем и обрабатываем DataFrame
    df = create_dataframe('annotation.csv')
    df = add_image_info(df)
    
    # Выводим все строки DataFrame
    print("\nВсе строки DataFrame:")
    print(df)
    
    # Выводим статистику
    print("\nСтатистика по размерам изображений:")
    print(df[['Высота', 'Ширина', 'Глубина']].describe())
    
    # Добавляем столбец с площадью
    df['Площадь'] = df['Высота'] * df['Ширина']
    
    # Сортируем по площади и выводим результат
    df = df.sort_values('Площадь')
    print("\nОтсортированный DataFrame по площади:")
    print(df)
    
    # Создаем и показываем визуализацию
    create_histogram(df)


if __name__ == "__main__":
    main()
