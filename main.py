import argparse

import cv2

from src.image_loader import load_image
from src.image_processor import overlay_images
from src.visualization import plot_histogram, show_results



def parse_args() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки.
    """
    parser = argparse.ArgumentParser(description='Наложение изображений')
    parser.add_argument('img1_path', type=str, help='Путь к первому изображению')
    parser.add_argument('img2_path', type=str, help='Путь ко второму изображению')
    parser.add_argument('output_path', type=str, help='Путь для сохранения результата')
    parser.add_argument('--alpha', type=float, default=0.5, 
                        help='Коэффициент прозрачности (0-1), по умолчанию 0.5')
    
    args = parser.parse_args()
    if not 0 <= args.alpha <= 1:
        raise ValueError("alpha должно быть в диапазоне [0, 1]")
    return args


def main() -> None:
    """
    Основная функция программы.
    """
    try:
        args = parse_args()
        
        img1 = load_image(args.img1_path)
        img2 = load_image(args.img2_path)
        
        print(f"Размер первого изображения: {img1.shape}")
        print(f"Размер второго изображения: {img2.shape}")
        
        plot_histogram(img1)
        result = overlay_images(img1, img2, args.alpha)
        show_results(img1, img2, result)
        
        cv2.imwrite(args.output_path, result)
        print(f"Результат сохранен в {args.output_path}")
        
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
