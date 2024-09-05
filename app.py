import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        self.left = 800
        self.top = 200
        self.width = 500
        self.height = 700
        self.setFixedSize(self.width, self.height)
        self.setObjectName("main_window")
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #--------------Main Window----------------
        
        #------------single-------
        self.single_bubble = QFrame(self)
        self.single_bubble.setObjectName("single_bubble")
        self.single_bubble.move(100,150)
        self.single_bubble.mousePressEvent = self.single_bubble_clicked
        
        self.single_bubble_heading = QLabel(self.single_bubble)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(75,8)
        
        self.single_bubble_para = QLabel(self.single_bubble)
        self.single_bubble_para.setObjectName("bubble_para")
        self.single_bubble_para.setText("Click here to compress single image")
        self.single_bubble_para.move(25,55)
        
        #----------------------multiple------
        
        self.multiple_bubble = QFrame(self)
        self.multiple_bubble.setObjectName("multiple_bubble")
        self.multiple_bubble.move(100,350)
        self.multiple_bubble.mousePressEvent = self.multiple_bubble_clicked
        
        self.multiple_bubble_heading = QLabel(self.multiple_bubble)
        self.multiple_bubble_heading.setObjectName("bubble_heading")
        self.multiple_bubble_heading.setText("Compress Multiple Images")
        self.multiple_bubble_heading.move(30,12)
        
        self.multiple_bubble_para = QLabel(self.multiple_bubble)
        self.multiple_bubble_para.setObjectName("bubble_para")
        self.multiple_bubble_para.setWordWrap(True)
        self.multiple_bubble_para.setText("Click here to compress multiple images using select folder")
        self.multiple_bubble_para.move(21,55)
        
        
        #Single Bubble Expanded
        
        self.single_bubble_expanded = QFrame(self)
        self.single_bubble_expanded.setObjectName("bubble_expanded")
        self.single_bubble_expanded.move(100,150)
        self.single_bubble_expanded.setVisible(False)
        
        self.back_arrow_s = QLabel(self.single_bubble_expanded)
        self.back_arrow_s.move(30, 0)
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked
        
        self.single_bubble_heading = QLabel(self.single_bubble_expanded)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(75,12)
        
        self.single_image_label = QLabel(self.single_bubble_expanded)
        self.single_image_label.setObjectName("bubble_para")
        self.single_image_label.setText("Choose Image")
        self.single_image_label.move(30,65)
        
        self.image_path = QLineEdit(self.single_bubble_expanded)
        self.image_path.setObjectName("text_path")
        self.image_path.move(60,95)
        
        self.browse_button = QPushButton(self.single_bubble_expanded)
        self.browse_button.setText("...")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.move(210,93)
        
        self.single_image_quality = QLabel(self.single_bubble_expanded)
        self.single_image_quality.setObjectName("bubble_para")
        self.single_image_quality.setText("Choose Quality")
        self.single_image_quality.move(30,185)
        
        self.quality_path = QLineEdit(self.single_bubble_expanded)
        self.quality_path.setObjectName("text_path_quality")
        self.quality_path.move(60,215)
        
        self.compress_button = QPushButton(self.single_bubble_expanded)
        self.compress_button.setText("Compress")
        self.compress_button.setObjectName("compress_button")
        self.compress_button.move(100,280)
         
        #Multiple Bubble Expanded
        
        self.multiple_bubble_expanded = QFrame(self)
        self.multiple_bubble_expanded.setObjectName("bubble_expanded")
        self.multiple_bubble_expanded.move(100,150)
        self.multiple_bubble_expanded.setVisible(False)
        
        self.back_arrow_m = QLabel(self.multiple_bubble_expanded)
        self.back_arrow_m.move(30, 0)
        self.back_arrow_m.setObjectName("back_arrow")
        self.back_arrow_m.setTextFormat(Qt.RichText)
        self.back_arrow_m.setText("&#8592;")
        self.back_arrow_m.mousePressEvent = self.back_arrow_clicked
        
        #----------------End----------------------
        
        self.show()
        
    #----------------Functions----------------
    
    def back_arrow_clicked(self, event):
        self.single_bubble.setVisible(True)
        self.multiple_bubble.setVisible(True)
        self.single_bubble_expanded.setVisible(False)
        self.multiple_bubble_expanded.setVisible(False)
    
    def single_bubble_clicked(self, event):
        print("single button")
        self.single_bubble.setVisible(False)
        self.multiple_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(True)
        self.multiple_bubble_expanded.setVisible(False)
        
    def multiple_bubble_clicked(self, event):
        print("multiple button")
        self.single_bubble.setVisible(False)
        self.multiple_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(False)
        self.multiple_bubble_expanded.setVisible(True)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())