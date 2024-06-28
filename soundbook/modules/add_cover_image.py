import glob
import os

from mutagen.mp4 import MP4, MP4Cover


def add_cover_image(directory, title, book_title, book_author):
    title = title + ".m4b"
    dir_path = f"downloads/{directory}"
    full_path_to_file = os.path.join(dir_path, title)
    image_files = glob.glob(os.path.join(dir_path, "*.jpg"))
    if image_files:
        cover_img = image_files[0]
        if os.path.isfile(cover_img):
            audio = MP4(full_path_to_file)
            cover_image = open(cover_img, "rb").read()
            audio["covr"] = [MP4Cover(cover_image)]
            if book_title is not None:
                audio["\xa9nam"] = [book_title]
            if book_author is not None:
                audio["\xa9ART"] = [book_author]
            audio.save()
            os.remove(cover_img)
        else:
            print(f"Cover image {cover_img} not found")
