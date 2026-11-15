import sys
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QGridLayout, 
    QStackedLayout,
    QTabWidget,
    QLabel,
    QPushButton,
    QStackedWidget,
    QComboBox,
    QTextBrowser
    )
from PySide6.QtGui import QPalette, QColor
from layout_colorwidget import Color
from cnn_train_tab import CnnTrainTab
from cnn_eval_tab import CnnEvalTab

class SplashPage(QWidget):
    def __init__(self, switch_callback):
        super().__init__()

        layout = QVBoxLayout()
        
        layout.addWidget(QLabel(
        "Welcome to AnimalML!\n" \
        "Here you can train neural networks to recognise animal species from camera trap images, with various enhancements and analysis techniques\n" \
        "This is an application that ties together (and improves on) the PhD work done by J. Curry between 2021 and 2026.\n" \
        ))
        self.license_text_browser = QTextBrowser(self)
        self.license_text_browser.setOpenExternalLinks(True)
        self.license_text_browser.append("Unless required by applicable law or agreed to in writing, " \
        "software distributed under the License is distributed on an 'AS IS' BASIS, " \
        "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, " \
        "either express or implied. " \
        "See the License for the specific language governing permissions and limitations under the License. ")
        self.license_text_browser.append("Please see the associated <a href=https://github.com/JCur96/AnimalML>GitHub</a> for full licesne details.")
        layout.addWidget(self.license_text_browser)

        button = QPushButton("Continue")
        button.clicked.connect(switch_callback)

        layout.addWidget(button)
        self.setLayout(layout)

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(False)

        cnn_train_tab = CnnTrainTab()
        cnn_train_tab.train_requested.connect(self.handle_train_request)

        tabs.addTab(cnn_train_tab, "CNN Training")

        cnn_eval_tab = CnnEvalTab()
        tabs.addTab(cnn_eval_tab, "CNN Evaluation")

        # layout.addWidget(QLabel("This is a test"))
        # tab = QWidget()
        # tab.setLayout(layout)

        # for color in ["red", "green", "blue", "yellow"]:
        #     tabs.addTab(Color(color), color)

        layout.addWidget(tabs)
        self.setLayout(layout)

    def handle_train_request(self, dataset_path, use_imagenet_weights, backbone_name):
        print(f"DEBUG: TRAIN SIGNAL RECIEVED: {dataset_path, use_imagenet_weights, backbone_name}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AnimalML")

        self.stack = QStackedWidget()

        # create pages
        self.main_page = MainPage()
        self.splash_page = SplashPage(self.show_main_page)

        self.stack.addWidget(self.splash_page)
        self.stack.addWidget(self.main_page)
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def show_main_page(self):
        self.stack.setCurrentIndex(1)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()