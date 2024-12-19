import cv2
import pandas as pd

from typing import Tuple


def get_image_dimensions(image_path: str) -> Tuple[int, int, int]:
    """
    Получает размеры изображения.
    
    Args:
        image_path (str): путь к изображению
    
    Returns:
        Tuple[int, int, int]: высота, ширина и количество каналов
    """
    img = cv2.imread(image_path)
    if img is None:
        return 0, 0, 0
    height, width, channels = img.shape
    return height, width, channels


def add_image_info(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет информацию о размерах изображений в DataFrame.
    
    Args:
        df (pd.DataFrame): исходный DataFrame
    
    Returns:
        pd.DataFrame: обновленный DataFrame
    """
    dimensions = df['Абсолютный путь'].apply(get_image_dimensions)
    df['Высота'] = [d[0] for d in dimensions]
    df['Ширина'] = [d[1] for d in dimensions]
    df['Глубина'] = [d[2] for d in dimensions]
    return df


def filter_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальным размерам.
    
    Args:
        df (pd.DataFrame): исходный DataFrame
        max_width (int): максимальная ширина
        max_height (int): максимальная высота
    
    Returns:
        pd.DataFrame: отфильтрованный DataFrame
    """
    return df[(df['Высота'] <= max_height) & (df['Ширина'] <= max_width)] 