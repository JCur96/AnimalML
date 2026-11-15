from PySide6.QtWidgets import (
QWidget,
QVBoxLayout,
QComboBox,
QPushButton,
QLabel,
QCheckBox,
QLineEdit,
QPlainTextEdit
) 
from PySide6.QtCore import Signal
from dir_file_browse_button import DirBrowseButton
from PySide6.QtGui import QFont
from console_widget import ConsoleWidget


class CnnTrainTab(QWidget):
    train_requested = Signal(str, bool, str)
    """
    Signal emits dataset_path (training dataset, str), 
    use_imagenet_weights(defaulted to True, bool), 
    and backbone name (string model name , str).

    Add more types to the above as widgets get added. 
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Select Training Dataset"))
        self.dataset_selection = DirBrowseButton()
        layout.addWidget(self.dataset_selection)

        self.imagenet_checkbox = QCheckBox("Use ImageNet weights?")
        self.imagenet_checkbox.setChecked(True)
        layout.addWidget(self.imagenet_checkbox)

        layout.addWidget(QLabel("Select Backbone Model"))
        self.backbone_model_combo = QComboBox()
        self.backbone_model_combo.addItems([
                        "ResNet-152V2", 
                        "Inception-V3", 
                        "Inception-ResNet-V2", 
                        "ResNet-50V2", 
                        "ResNet-101V2", 
                        "VGG19", 
                        "EfficientNetV2S", 
                        "EfficientNetV2M", 
                        "ConvNeXtTiny"
                        ])
        layout.addWidget(self.backbone_model_combo)
        
        self.start_train_button = QPushButton("Start Training")
        self.start_train_button.clicked.connect(self.on_start_training_clicked)
        layout.addWidget(self.start_train_button)

        # tab = QWidget()
        # tab.setLayout(layout)

        # Console log, need to make sure it stay a sensible number of lines,
        # auto scrolls and is read only
        # log = QPlainTextEdit()
        # log.setReadOnly(True)
        # log.setFont(QFont("Courier"))

        # default start message, should only be displayed on click of start train btn
        # log.appendPlainText("Training started...")
        self.console = ConsoleWidget()
        self.console.hide()

        layout.addWidget(self.console)

        self.setLayout(layout)
    def on_start_training_clicked(self):
        dataset_path = self.dataset_selection.get_path()
        use_imagenet_weights = self.imagenet_checkbox.isChecked()
        backbone_name = self.backbone_model_combo.currentText()
        self.console.show()

        self.train_requested.emit(
            dataset_path,
            use_imagenet_weights,
            backbone_name
        )