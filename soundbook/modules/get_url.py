from soundbook.modules.add_cover_image import add_cover_image
from soundbook.modules.extract_audio import extract_audio
from soundbook.modules.get_cover_image import get_cover_image
from soundbook.modules.get_title import get_title
from soundbook.modules.make_folder import make_folder
from soundbook.modules.merge_audio import merge_audio


def get_url(url, book_title, book_author):
    directory = get_title(url)
    make_folder(directory)
    title = extract_audio(url, directory)
    get_cover_image(directory)
    merge_audio(directory)
    add_cover_image(directory, title, book_title, book_author)
