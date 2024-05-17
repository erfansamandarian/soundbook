from PIL import Image
from io import BytesIO
from mutagen.id3 import ID3
from mutagen.mp4 import MP4, MP4Cover
import glob
import os
import subprocess


def make_folder(directory):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    dir_path = os.path.join("downloads", directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def extract_audio(url, directory):
    result = subprocess.run(
        [
            "yt-dlp",
            "-f",
            "bestaudio",
            "-x",
            "--audio-format",
            "mp3",
            "-P",
            f"downloads/{directory}",
            url,
        ],
        check=True,
    )
    return directory


def merge_audio(directory):
    os.chdir(f"downloads/{directory}")
    output_file = f"{directory}.mp3"
    output_file_m4b = f"{directory}.m4b"
    subprocess.run(["sox", "*.mp3", output_file], check=True)
    subprocess.run(
        ["ffmpeg", "-i", output_file, "-c:v", "h264_videotoolbox", output_file_m4b],
        check=True,
    )  # todo: detect hardware and change accordingly
    mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]
    for mp3_file in mp3_files:
        os.remove(mp3_file)
    os.chdir("../..")


def get_title(url):
    return url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]


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


def add_cover_image(directory, title):
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
            audio.save()
            os.remove(cover_img)
        else:
            print(f"Cover image {cover_img} not found")


def get_url(url):
    directory = get_title(url)
    make_folder(directory)
    title = extract_audio(url, directory)
    get_cover_image(directory)
    merge_audio(directory)
    add_cover_image(directory, title)
