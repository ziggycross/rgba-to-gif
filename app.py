import os
import sys
from pathlib import Path

from PIL import Image
from PyQt6.QtWidgets import (QApplication, QFileDialog, QGridLayout, QLabel,
                             QLineEdit, QMainWindow, QPushButton, QWidget)

import rgba_to_gif


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Session variables
        self.frame_folder = None
        self.output_path = None
    
        # Window setup
        self.setWindowTitle('RGBA to GIF')
        self.setGeometry(100, 100, 500, 100)

        # Grid Layout
        layout = QGridLayout()
        self.setLayout(layout)

        # Input Path
        layout.addWidget(QLabel('Frames:'), 0, 0)
        
        self.frame_folder_display = QLineEdit()
        layout.addWidget(self.frame_folder_display, 0, 1)
        
        frame_folder_button = QPushButton('Select')
        frame_folder_button.clicked.connect(self.get_frame_folder)
        layout.addWidget(frame_folder_button, 0, 2)
        
        # Output Path
        layout.addWidget(QLabel('Output:'), 1, 0)

        self.output_path_display = QLineEdit()
        layout.addWidget(self.output_path_display, 1, 1)
        
        output_path_button = QPushButton('Select')
        output_path_button.clicked.connect(self.get_output_path)
        layout.addWidget(output_path_button, 1, 2)
        
        # Convert Button
        convert_files = QPushButton("Convert")
        convert_files.clicked.connect(self.convert_frames)
        layout.addWidget(convert_files, 2, 0, 1, 3)

        self.show()


    def _get_directory(self, suffix=""):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec() == QFileDialog.DialogCode.Accepted:
            return dialog.selectedFiles()[0]+suffix

    def get_frame_folder(self):
        self.frame_folder = self._get_directory()
        if self.frame_folder:
            self.frame_folder_display.setText(self.frame_folder)

    def get_output_path(self):
        self.output_path = self._get_directory(suffix="/output.gif")
        if self.output_path:
            self.output_path_display.setText(self.output_path)

    def convert_frames(self):
        try: 
            rgba_to_gif.convert(
                input_folder=self.frame_folder,
                output_path=self.output_path
                )
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
