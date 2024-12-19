import matplotlib.pyplot as plt
import pandas as pd


def setup_display_options():
    """Настраивает параметры отображения DataFrame"""
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)


def create_histogram(df: pd.DataFrame, output_path: str = 'histogram.png'):
    """
    Создает гистограмму распределения площадей.
    
    Args:
        df (pd.DataFrame): DataFrame с данными
        output_path (str): путь для сохранения гистограммы
    """
    # Создаем гистограмму
    plt.figure(figsize=(12, 8))
    plt.hist(df['Площадь'], bins=30, edgecolor='black', color='skyblue')
    
    # Настраиваем внешний вид
    plt.title('Распределение площадей изображений', fontsize=14)
    plt.xlabel('Площадь (пикселей)', fontsize=12)
    plt.ylabel('Количество изображений', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Делаем отступы, чтобы текст не обрезался
    plt.tight_layout()
    
    plt.show() 