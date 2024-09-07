import sys
from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import PIL
from PIL import Image
import os

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        self.left = 800
        self.top = 200
        self.width = 500
        self.height = 700
        self.image_width = 0
        self.compress_width = 0
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
        self.browse_button.clicked.connect(self.select_file)
        self.browse_button.move(210,93)
        
        self.single_image_quality = QLabel(self.single_bubble_expanded)
        self.single_image_quality.setObjectName("bubble_para")
        self.single_image_quality.setText("Choose Quality")
        self.single_image_quality.move(30,185)
        
        self.quality_path = QLineEdit(self.single_bubble_expanded)
        self.quality_path.setObjectName("text_path_quality")
        self.quality_path.move(60,215)
        
        self.quality_combo = QComboBox(self.single_bubble_expanded)
        self.quality_combo.setObjectName("quality_combo")
        self.quality_combo.addItem("High")
        self.quality_combo.addItem("Medium")
        self.quality_combo.addItem("Low")
        self.quality_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quality_combo.move(170,214)
        self.quality_combo.resize(70,26)
        
        self.compress_button = QPushButton(self.single_bubble_expanded)
        self.compress_button.setText("Compress")
        self.compress_button.setObjectName("compress_button")
        self.compress_button.clicked.connect(self.resize_image)
        self.compress_button.move(100,280)
         
        #Multiple Bubble Expanded
        
        self.multiple_bubble_expanded = QFrame(self)
        self.multiple_bubble_expanded.setObjectName("bubble_expanded")
        self.multiple_bubble_expanded.move(100,150)
        self.multiple_bubble_expanded.setVisible(False)
        
        self.back_arrow_m = QLabel(self.multiple_bubble_expanded)
        self.back_arrow_m.move(10, 0)
        self.back_arrow_m.setObjectName("back_arrow")
        self.back_arrow_m.setTextFormat(Qt.RichText)
        self.back_arrow_m.setText("&#8592;")
        self.back_arrow_m.mousePressEvent = self.back_arrow_clicked
        
        self.multiple_bubble_heading = QLabel(self.multiple_bubble_expanded)
        self.multiple_bubble_heading.setObjectName("bubble_heading")
        self.multiple_bubble_heading.setText("Compress Multiple Images")
        self.multiple_bubble_heading.move(55,12)
        
        self.multiple_image_label = QLabel(self.multiple_bubble_expanded)
        self.multiple_image_label.setObjectName("bubble_para")
        self.multiple_image_label.setText("Choose Image")
        self.multiple_image_label.move(30,65)
        
        self.source_path = QLineEdit(self.multiple_bubble_expanded)
        self.source_path.setObjectName("text_path")
        self.source_path.move(60,95)
        
        self.browse_src_button = QPushButton(self.multiple_bubble_expanded)
        self.browse_src_button.setText("...")
        self.browse_src_button.setObjectName("browse_button")
        self.browse_src_button.clicked.connect(self.select_folder_src)
        self.browse_src_button.move(210,93)
        
        self.multiple_dest_label = QLabel(self.multiple_bubble_expanded)
        self.multiple_dest_label.setObjectName("bubble_para")
        self.multiple_dest_label.setText("Choose Destination Directory")
        self.multiple_dest_label.move(30,134)
        
        self.destination_path = QLineEdit(self.multiple_bubble_expanded)
        self.destination_path.setObjectName("text_path")
        self.destination_path.move(60,165)
        
        self.browse_dest_button = QPushButton(self.multiple_bubble_expanded)
        self.browse_dest_button.setText("...")
        self.browse_dest_button.setObjectName("browse_button")
        self.browse_dest_button.clicked.connect(self.select_folder_dest)
        self.browse_dest_button.move(210,163)
        
        self.multiple_image_quality = QLabel(self.multiple_bubble_expanded)
        self.multiple_image_quality.setObjectName("bubble_para")
        self.multiple_image_quality.setText("Choose Quality")
        self.multiple_image_quality.move(30,205)
        
        self.dir_quality_path = QLineEdit(self.multiple_bubble_expanded)
        self.dir_quality_path.setObjectName("text_path_quality")
        self.dir_quality_path.move(60,235)
        
        self.dir_quality_combo = QComboBox(self.multiple_bubble_expanded)
        self.dir_quality_combo.setObjectName("quality_combo")
        self.dir_quality_combo.addItem("High")
        self.dir_quality_combo.addItem("Medium")
        self.dir_quality_combo.addItem("Low")
        self.dir_quality_combo.currentIndexChanged.connect(self.quality_current_value)
        self.dir_quality_combo.move(170,234)
        self.dir_quality_combo.resize(70,26) 
        
        self.multiple_compress_button = QPushButton(self.multiple_bubble_expanded)
        self.multiple_compress_button.setText("Compress")
        self.multiple_compress_button.setObjectName("compress_button")
        self.multiple_compress_button.move(100,280)
        
        #----------------End----------------------
        
        self.show()
        
    #----------------Functions----------------
            
    def select_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;JPEG (*.jpeg);;JPG (*.jpg);;PNG (*.png)")
        if fileName:
            print(fileName)
            self.image_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width
            self.compress_width = self.image_width
            self.quality_path.setText(str(self.image_width))
    
    def select_folder_src(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "Select Deirectory")
        self.source_path.setText(selected_directory)
        files = os.listdir(selected_directory)
        first_pic = selected_directory + "/" + files[0]
        
        img = Image.open(first_pic)
        self.image_width = img.width
        self.compress_width = self.image_width
        self.dir_quality_path.setText(str(self.image_width))
        
    def select_folder_dest(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "Select Deirectory")
        self.destination_path.setText(selected_directory)
        
    def quality_current_value(self):
        if self.quality_combo.currentText() == "High":
            self.quality_path.setText(str(self.image_width))
            self.compress_width = self.image_width
            
        if self.quality_combo.currentText() == "Medium":
            self.quality_path.setText(str(int(self.image_width/2)))
            self.compress_width = int(self.image_width/2)
            
        if self.quality_combo.currentText() == "Low":
            self.quality_path.setText(str(int(self.image_width/4)))
            self.compress_width = int(self.image_width/4)

        if self.quality_combo.currentText() == "High":
            self.dir_quality_path.setText(str(self.image_width))
            self.compress_width = self.image_width
            
        if self.quality_combo.currentText() == "Medium":
            self.dir_quality_path.setText(str(int(self.image_width/2)))
            self.compress_width = int(self.image_width/2)
            
        if self.quality_combo.currentText() == "Low":
            self.dir_quality_path.setText(str(int(self.image_width/4)))
            self.compress_width = int(self.image_width/4)
    
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
        
    def resize_image(self):
        old_pic = self.image_path.text()
        directories = self.image_path.text().split("/")
        new_pic_name, okPressed = QInputDialog.getText(self, "Save Image as", "Image Name:", QLineEdit.Normal, "")
        
        if okPressed and new_pic_name != '':
            print(new_pic_name)
            ext = old_pic.split('.')[-1].lower()  # Extract the extension from the old file
            new_pic = "/".join(directories[:-1]) + "/" + new_pic_name + "." + ext
            print(new_pic)
            
            self.compression_code(old_pic, new_pic)
            print("Compressed")
                
    def compression_code(self, old_pic, new_pic):
        img = Image.open(old_pic)
        mywidth = self.compress_width
        wpercent = (mywidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((mywidth,hsize), PIL.Image.LANCZOS)
        img.save(new_pic)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())