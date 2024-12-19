import matplotlib.pyplot as plt
import pandas as pd


def setup_display_options():
    """Настраивает параметры отображения DataFrame"""
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)


def create_histogram(column: pd.Series, title: str, xlabel: str, ylabel: str):
    """
    Создает гистограмму распределения площадей.
    
    Args:
        df (pd.DataFrame): DataFrame с данными
        output_path (str): путь для сохранения гистограммы
    """
    # Создаем гистограмму
    plt.figure(figsize=(12, 8))
    plt.hist(column, bins=30, edgecolor='black', color='skyblue')
    
    # Настраиваем внешний вид
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Делаем отступы
    plt.tight_layout()
    
    plt.show() 
