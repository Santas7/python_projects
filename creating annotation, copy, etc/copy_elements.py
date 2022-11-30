import os
import shutil
import main
from main import Data
from typing import Type


def make_dir(obj: type(Data)) -> None:
    """
        check for an existing directory + create a new directory "new_dataset"
    """
    try:
        os.mkdir("new_dataset")
        obj.dir_name = "new_dataset"
    except OSError:
        shutil.rmtree("new_dataset")
        os.mkdir("new_dataset")
        obj.dir_name = "new_dataset"


def teleport_dir(obj: type(Data), path: str, class_name: str) -> None:
    """
        this function creates a new folder new_dataset and moves directory class_name with all its subdirectories there
        so that the names of the new subdirectories start with class_name. At the end of the loop we add an annotation to the file.
        :later_dir: - previous directory ( you need to save )
    """
    later_dir = obj.dir_name
    make_dir(obj)
    for i in range(1000):
        os.rename(os.path.join(later_dir, class_name, f'{(i+1):04d}.jpg'),
                  os.path.join(later_dir, class_name, f'{class_name}_{(i+1):04d}.jpg'))
        shutil.copy(os.path.join(later_dir, class_name, f'{class_name}_{(i+1):04d}.jpg'), obj.dir_name)
        os.rename(os.path.join(later_dir, class_name, f"{class_name}_{(i+1):04d}.jpg"),
                  os.path.join(later_dir, class_name, f'{(i+1):04d}.jpg'))
        obj.add(os.path.join(path, obj.dir_name, class_name), class_name, f'{class_name}_{(i+1):04d}.jpg')  # добавление строки в файл аннотация

if __name__ == "__main__":
    teleport_dir(Data("dataset"), "D:\Program Files\programmingLabs\Python\python-L-2-var-4\Lab2", main.CLASS_DEFAULT[0])
