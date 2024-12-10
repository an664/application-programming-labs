import cv2
import numpy as np


def overlay_images(img1: np.ndarray, img2: np.ndarray, alpha: float) -> np.ndarray:
    """
    Наложение одного изображения на другое с заданной прозрачностью.
    """
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    return cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0) 