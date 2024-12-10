import os
import csv
import shutil
from typing import Dict, List


class ImageIterator:
    """
    Итератор для последовательного обхода загруженных изображений.
    
    Attributes:
        annotation_path (str): путь к файлу аннотаций
        current (int): текущий индекс
        images (List[Dict[str, str]]): список изображений с их путями
    """
    
    def __init__(self, annotation_path: str) -> None:
        """
        Инициализация итератора.
        
        Args:
            annotation_path (str): путь к файлу аннотаций
        """
        self.annotation_path = annotation_path
        self.current = 0
        self.images = []
        
        with open(annotation_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.images = list(reader)
    
    def __iter__(self) -> 'ImageIterator':
        """
        Возвращает сам объект итератора.
        
        Returns:
            ImageIterator: текущий объект
        """
        return self
    
    def __next__(self) -> Dict[str, str]:
        """
        Возвращает следующее изображение из списка.
        
        Returns:
            Dict[str, str]: словарь с путями к изображению
            
        Raises:
            StopIteration: если достигнут конец списка
        """
        if self.current >= len(self.images):
            raise StopIteration
        
        image = self.images[self.current]
        self.current += 1
        return image


def clear_directory(directory: str) -> None:
    """
    Очищает указанную директорию.
    
    Args:
        directory (str): путь к директории для очистки
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


def create_annotation(save_dir: str, annotation_path: str) -> None:
    """
    Создает файл аннотаций для загруженных изображений.
    
    Args:
        save_dir (str): директория с изображениями
        annotation_path (str): путь для сохранения файла аннотаций
    """
    with open(annotation_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['relative_path', 'absolute_path'])
        
        files_count = 0
        files = sorted([f for f in os.listdir(save_dir) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        for filename in files:
            relative_path = os.path.join(save_dir, filename)
            absolute_path = os.path.abspath(relative_path)
            writer.writerow([relative_path, absolute_path])
            files_count += 1
        
        print(f"\nВсего загружено изображений: {files_count}")