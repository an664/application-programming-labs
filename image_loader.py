import cv2
import numpy as np

def load_image(path: str) -> np.ndarray:
    """
    Загрузка изображения из файла.
    """
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Не удалось загрузить изображение: {path}")
    return img 