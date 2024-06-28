import os

from io import BytesIO
from mutagen.id3 import ID3
from PIL import Image


def get_cover_image(directory):
    dir_path = f"downloads/{directory}"
    mp3_files = [f for f in os.listdir(dir_path) if f.endswith(".mp3")]
    for mp3_file in mp3_files:
        song_path = os.path.join(dir_path, mp3_file)
        tags = ID3(song_path)
        apic_frames = tags.getall("APIC")
        if apic_frames:
            pic = apic_frames[0].data
            im = Image.open(BytesIO(pic))
            title = tags.get("TIT2").text[0] if tags.get("TIT2") else "unknown"
            title = title.replace("-", "/")
            cover_image_path = os.path.join(dir_path, f"{title}_cover.jpg")
            im.save(cover_image_path)
