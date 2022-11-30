import os
import csv

CLASS_DEFAULT = ["rose", "tulip"]  # базовые названия


class Data:
    def __init__(self, dir_name: str) -> None:
        """
            :number_lines: - number of lines in the annotation
            :viewed_files: - number of files viewed
            :dir_name: - directory name ("dataset")
        """
        self.number_lines = 0
        self.viewed_files = 1
        self.dir_name = dir_name

    def add(self, path: str, class_name: str, name_image: str) -> None:
        """
            The function adds a line to the annotation file
            :path: - a variable containing the path ( for example: "D:\Program Files\programmingLabs\Python\python-L-2-var-4\Lab2")
            :class_name: - class name ( subdirectory ) for example: CLASS_DEFAULT[0]
            :name_image: - the variable which contains the name of the image
        """
        with open("annotation.csv", "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            if self.number_lines == 0: # если кол-во строк = 0, то это заголовки файла аннотация
                writer.writerow([
                    "the absolute way",
                    "relative path",
                    "class."
                ])
                self.number_lines += 1
            writer.writerow([os.path.join(path, self.dir_name, class_name, name_image), os.path.join(self.dir_name, class_name, name_image), class_name])
            self.number_lines += 1
