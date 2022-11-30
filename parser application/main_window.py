import annotation
import copy_elements as ce
import random_of_copy as rc
from annotation import Data
from iterator_class import IteratorOfExemplar
import os
import sys
from enum import Enum
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QGridLayout
from PyQt6 import QtGui, QtWidgets


class Type(Enum):
    ROSE = 0
    TULIP = 1


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # options window
        self.setWindowTitle("Main window")
        # self.setFixedSize(QSize(800, 600))
        self.dataset_path = QFileDialog.getExistingDirectory(self, 'Путь к папке базового датасет')
        src = QLabel(f'Basic dataset:\n{self.dataset_path}', self)
        src.setFixedSize(QSize(800, 50))
        #layout = QGridLayout()
        #layout.addWidget(src, 0, 0)

        # starts values
        self.count_r = 1  # position counter
        self.count_t = 1
        self.s_p_rose = os.path.join("dataset", annotation.CLASS_DEFAULT[Type.ROSE.value], "0001.jpg")  # начальный для rose
        self.s_p_tulip = os.path.join("dataset", annotation.CLASS_DEFAULT[Type.TULIP.value], "0001.jpg")  # начальный для tulip

        # buttons
        self.btn_create_of_annotation = self.add_button("Create an abstract", 150, 50, 630, 50)
        self.btn_copy_of_dataset = self.add_button("Copy dataset", 150, 50, 630, 100)
        self.btn_random_of_dataset = self.add_button("Random dataset", 150, 50, 630, 150)
        self.btn_next_rose = self.add_button("Next rose-->", 150, 50, 630, 250)
        self.btn_back_rose = self.add_button("<--Prev rose", 150, 50, 630, 300)
        self.btn_next_tulip = self.add_button("Next tulip-->", 150, 50, 630, 350)
        self.btn_back_tulip = self.add_button("<--Prev tulip", 150, 50, 630, 400)
        self.go_to_exit = self.add_button("Exit", 150, 50, 630, 500)

        # picture
        self.pic = QtWidgets.QLabel(self)
        self.pic.setPixmap(QtGui.QPixmap(self.s_p_rose))
        self.pic.resize(600, 500)  # <--
        self.pic.move(10, 50)

        if not os.path.exists(self.s_p_rose) or os.path.exists(self.s_p_tulip):
            self.pic.setText('Error!\n' + 'There are no initial pictures in the base dataset: "rose" или "tulip"')

    # button click events
        # transitions "next element" and "previous element"
        self.btn_next_rose.clicked.connect(lambda image_path=self.s_p_rose, index=Type.ROSE.value, count=self.count_r: self.next(self.s_p_rose, Type.ROSE.value, self.count_r)) # self.next(self.s_p_rose, Type.ROSE.value)
        self.btn_back_rose.clicked.connect(lambda image_path=self.s_p_rose, index=Type.ROSE.value, count=self.count_r: self.back(self.s_p_rose, Type.ROSE.value, self.count_r))
        self.btn_next_tulip.clicked.connect(lambda image_path=self.s_p_tulip, index=Type.TULIP.value, count=self.count_t: self.next(self.s_p_tulip, Type.TULIP.value, self.count_t))
        self.btn_back_tulip.clicked.connect(lambda image_path=self.s_p_tulip, index=Type.TULIP.value, count=self.count_t: self.back(self.s_p_tulip, Type.TULIP.value, self.count_t))

        # annotation creation, copy + random
        self.btn_create_of_annotation.clicked.connect(self.create_annotation)
        self.btn_copy_of_dataset.clicked.connect(self.copy_of_dataset)
        self.btn_random_of_dataset.clicked.connect(self.random_of_dataset)

        # exit the program
        self.go_to_exit.clicked.connect(self.exit)

        self.show()

    def add_button(self, name: str, size_x: int, size_y: int, pos_x: int, pos_y: int):
        """
            method of adding ( creating ) a button
            :name: - button name
            :size_x: - size by x
            :size_y: - size by y
            :pos_x: - position by x
            :pos_y: - y position
        """
        button = QPushButton(name, self)
        button.setFixedSize(QSize(size_x, size_y))
        button.move(pos_x, pos_y)
        return button

    def next(self, image_path: str, index: int, count: int):
        """
            the method of switching to a non-ext picture
        """
        try:
            if count >= 1000 or count < 1:
                image_path = os.path.join("dataset", annotation.CLASS_DEFAULT[index], "0001.jpg")
            else:
                next = IteratorOfExemplar(Data("dataset"), image_path).__next__()
                next.replace("", '"')
                image_path = next.replace("/", "\\")
                count += 1
            self.pic.setPixmap(QtGui.QPixmap(image_path.replace('"', "")))
            if index == 0 and count != 0:
                self.s_p_rose = image_path
                self.count_r = count
            elif index == 1 and count != 0:
                self.s_p_tulip = image_path
                self.count_t = count
            else:
                self.pic.setText('Ошибка!\n' + 'В базовом датасете нету начальных картинок: "rose" или "tulip"')
        except OSError:
            print("error")

    def back(self, image_path: str, index: int, count: int):
        """
            method of going to the previous picture
        """
        try:
            if count >= 1000 or count < 1:
                image_path = os.path.join("dataset", annotation.CLASS_DEFAULT[index], "0001.jpg")
            else:
                next = IteratorOfExemplar(Data("dataset"), image_path).__back__()
                next.replace("", '"')
                image_path = next.replace("/", "\\")
                count -= 1
            self.pic.setPixmap(QtGui.QPixmap(image_path.replace('"', "")))
            if index == 0 and count != 0:
                self.s_p_rose = image_path
                self.count_r = count
            elif index == 1 and count != 0:
                self.s_p_tulip = image_path
                self.count_t = count
            else:
                self.pic.setText('Ошибка!\n' + 'В базовом датасете нету начальных картинок: "rose" или "tulip"')
        except OSError:
            print("error")

    def create_annotation(self):
        """
            method of creating an annotation file
        """
        try:
            ann = Data("dataset")
            for i in range(1, 1000):
                ann.add(self.dataset_path, f"{annotation.CLASS_DEFAULT[0]}", f"{i:04d}.jpg")
            for i in range(1, 1000):
                ann.add(self.dataset_path, f"{annotation.CLASS_DEFAULT[1]}", f"{i:04d}.jpg")
        except OSError:
            print("error")

    def copy_of_dataset(self):
        """
            method to create a copy of dataset
        """
        try:
            ce.teleport_dir(Data("dataset"), self.dataset_path, annotation.CLASS_DEFAULT[0])
        except OSError:
            print("error")

    def random_of_dataset(self):
        """
            method of creating a randomized dataset
        """
        try:
            rc.create_copy_dataset_with_random_number(Data("dataset"), self.dataset_path, annotation.CLASS_DEFAULT[0])
        except OSError:
            print("error")

    def exit(self):
        """
            exit method
        """
        print("Bye... I hope to see you soon!)")
        self.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
