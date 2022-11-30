import csv
import random
import os
import shutil
import copy_elements as ce
import main
from main import Data


def create_copy_dataset_with_random_number(obj: type(Data), path: str, class_name: str) -> None:
    """
        this function copies the class files and renames them randomly. At the end of the loop we add an annotation to the file.
        :later_dir: - previous directory ( we need to save )
    """
    later_dir = obj.dir_name
    ce.make_dir(obj)

    for i in range(1000):
        n = random.randint(0, 10000)
        os.rename(os.path.join(later_dir, class_name, f'{(i+1):04d}.jpg'),
                  os.path.join(later_dir, class_name, f'{n:05d}.jpg'))
        shutil.copy(os.path.join(later_dir, class_name, f'{n:05d}.jpg'), obj.dir_name)
        os.rename(os.path.join(later_dir, class_name, f"{n:05d}.jpg"),
                  os.path.join(later_dir, class_name, f'{(i+1):04d}.jpg'))
        obj.add(os.path.join(path, obj.dir_name, class_name), class_name, f'{n:05d}.jpg')  # добавление строки в файл аннотация

if __name__ == "__main__":
    create_copy_dataset_with_random_number(Data("dataset"), "D:\Program Files\programmingLabs\Python\python-L-2-var-4\Lab2", main.CLASS_DEFAULT[0])
