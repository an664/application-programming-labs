import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lab2.image_processor import ImageIterator # type: ignore
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                           QPushButton, QLabel, QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageViewer(QMainWindow):
    """Главное окно приложения для просмотра датасета изображений."""
    def __init__(self):
        super().__init__()
        self.iterator = None
        self.initUI()
        
    def initUI(self):
        """Инициализация интерфейса"""
        self.setWindowTitle('Просмотр датасета')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.select_btn = QPushButton('Выбрать файл аннотации', self)
        self.select_btn.clicked.connect(self.select_annotation)
        layout.addWidget(self.select_btn)

        self.next_btn = QPushButton('Следующее изображение', self)
        self.next_btn.clicked.connect(self.show_next_image)
        self.next_btn.setEnabled(False)
        layout.addWidget(self.next_btn)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

    def select_annotation(self):
        """Открывает диалог выбора файла аннотации"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл аннотации", "", "CSV Files (*.csv)"
        )
        if filename:
            self.iterator = ImageIterator(filename)
            self.next_btn.setEnabled(True)
            self.show_next_image()

    def show_next_image(self):
        """Отображает следующее изображение из датасета"""
        try:
            if self.iterator:
                image_data = next(self.iterator)
                pixmap = QPixmap(image_data['absolute_path'])
                scaled_pixmap = pixmap.scaled(
                    self.image_label.size(), 
                    Qt.KeepAspectRatio, 
                    Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
        except StopIteration:
            self.next_btn.setEnabled(False)
            self.image_label.setText("Изображения закончились") 