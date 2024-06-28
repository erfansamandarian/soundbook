import os


def make_folder(directory):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    dir_path = os.path.join("downloads", directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
