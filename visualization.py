import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(img: np.ndarray) -> None:
    """
    Построение и отображение гистограммы изображения.
    """
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=f'канал {color}')
    
    plt.title('Гистограмма изображения')
    plt.xlabel('Значения пикселей')
    plt.ylabel('Количество пикселей')
    plt.legend()
    plt.grid(True)
    plt.show()


def show_results(img1: np.ndarray, img2: np.ndarray, result: np.ndarray) -> None:
    """
    Отображение исходных изображений и результата.
    """
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title('Исходное изображение 1')
    
    plt.subplot(132)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.title('Исходное изображение 2')
    
    plt.subplot(133)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title('Результат наложения')
    
    plt.show() 