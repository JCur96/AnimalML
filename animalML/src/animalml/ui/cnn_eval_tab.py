from PySide6.QtWidgets import (
QWidget,
QVBoxLayout,
QComboBox,
QPushButton,
QLabel,
QCheckBox
)
from PySide6.QtCore import Signal
from dir_file_browse_button import DirBrowseButton, FileBrowseButton
from console_widget import ConsoleWidget


class CnnEvalTab(QWidget):
    eval_requested = Signal(dict)
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Select Evaluation Dataset"))
        self.eval_dataset = DirBrowseButton()
        layout.addWidget(self.eval_dataset)

        layout.addWidget(QLabel("Select Trained Model"))
        self.model_to_eval = FileBrowseButton()
        layout.addWidget(self.model_to_eval)

        layout.addWidget(QLabel("Target Metric"))
        self.F1_checkbox = QCheckBox("F1 Score")
        layout.addWidget(self.F1_checkbox)
        self.accuracy_checkbox = QCheckBox("Accuracy")
        layout.addWidget(self.accuracy_checkbox)

        layout.addWidget(QLabel("Toggle Output Files"))
        self.confusion_matrix_checkbox = QCheckBox("Confusion Matrix")
        layout.addWidget(self.confusion_matrix_checkbox)
        self.tsne_plot_checkbox = QCheckBox("tSNE plot")
        layout.addWidget(self.tsne_plot_checkbox)

        self.start_eval_btn = QPushButton("Start Evaluation")
        self.start_eval_btn.clicked.connect(self.on_start_eval_clicked)
        layout.addWidget(self.start_eval_btn)
        # tab = QWidget()
        # tab.setLayout(layout)

        self.console = ConsoleWidget()
        self.console.hide()

        layout.addWidget(self.console)

        self.setLayout(layout)
    
    def on_start_eval_clicked(self):
        eval_dataset = self.eval_dataset.get_path()
        trained_model = self.model_to_eval.get_path()
        metrics = []
        if self.F1_checkbox.isChecked():
            metrics.append("F1")
        if self.accuracy_checkbox.isChecked():
            metrics.append("accuracy")
        output_files = []
        if self.confusion_matrix_checkbox.isChecked():
            output_files.append("cm")
        if self.tsne_plot_checkbox.isChecked():
            output_files.append("tsne")

        eval_request = {"evaluation dataset": eval_dataset, 
                        "model to evaluate": trained_model, 
                        "metrics to display": metrics, 
                        "output graphs": output_files}
        
        
        self.console.show()

        self.eval_requested.emit(eval_request)