import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, 
    QPushButton, 
    QLineEdit, 
    QFileDialog,
    QHBoxLayout
)

class DirBrowseButton(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        dir_select_btn = QPushButton("Browse")
        dir_select_btn.clicked.connect(self.open_dir_dialog)
        self.dir_name_edit = QLineEdit()

        layout.addWidget(self.dir_name_edit)
        layout.addWidget(dir_select_btn)

        self.setLayout(layout)


    def open_dir_dialog(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path = Path(dir_name)
            self.dir_name_edit.setText(str(path))
    
    def get_path(self):
        return self.dir_name_edit.text()
class FileBrowseButton(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        file_select_btn = QPushButton("Browse")
        file_select_btn.clicked.connect(self.open_file_dialog)
        self.file_name_edit = QLineEdit()

        layout.addWidget(self.file_name_edit)
        layout.addWidget(file_select_btn)

        self.setLayout(layout)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select a File")
        if file_name:
            path = Path(file_name)
            self.file_name_edit.setText(str(path))
    def get_path(self):
        return self.file_name_edit.text()