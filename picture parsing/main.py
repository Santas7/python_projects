import os, shutil, requests
from bs4 import BeautifulSoup as BS

URL = "https://yandex.ru/images/" # ссылка на страничку html


def save_image(image_url, name, i):
    """save the saved picture to a specific folder"""
    request_on_download_image = requests.get(f"https:{image_url}")
    saver = open(f"dataset/{name}/{i:04d}.jpg", "wb")
    saver.write(request_on_download_image.content)
    saver.close()


def check_folder():
    """check for the existence of a folder"""
    try:
        os.mkdir("dataset")
    except:
        shutil.rmtree("dataset")
        os.mkdir("dataset")

def get_images_url(name):
    """
    VARIABLES: we create the variables we need to work with
    FOR: The for loop is needed to run through the finder (the sparsened html code).
    IMAGE_URL: Next we write the link in the image_url variable which is contained in the img tag, in the src="..." parameter.
    DATA: Then add the value of the image_url variable to the end of the data array using the append method.
    Then use conditional if statement to check if the string.... is empty If not empty, then save the picture to the
    the appropriate folder dataset/name/....jpg/. After the loop, we output a message to the console for the user.
    This completes the function.
    """
    i = 1
    page = 0
    request_go = requests.get(f"{URL}search?p={page}&text={name}&lr=51&rpt=image", headers={"User-Agent":"Mozilla/5.0"})
    html = BS(request_go.content, "html.parser")
    data = []
    finder = html.findAll("img")
    os.mkdir(f"dataset/{name}")
    while (True):
        for event in finder:
            image_url = event.get("src")
            data.append([image_url])
            if (i > 999):
                page = 0
                break
            if (image_url != ""):
                save_image(image_url, name, i)
                i += 1
        if (i > 999): break
        page += 1
    print("Nice save images)")
    print(data)

if __name__ == "__main__":
    check_folder()
    get_images_url("rose")
    get_images_url("tulip")
