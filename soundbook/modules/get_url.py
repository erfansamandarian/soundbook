import os
import subprocess


def make_folder(directory):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    dir_path = os.path.join("downloads", directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def extractAudio(url, directory):
    subprocess.run(
        [
            "yt-dlp",
            "-f",
            "bestaudio",
            "-x",
            "--audio-format",
            "wav",
            "-P",
            f"downloads/{directory}",
            url,
        ],
        check=True,
    )


def mergeAudio(directory):
    os.chdir(f"downloads/{directory}")
    subprocess.run(["sox", "*.wav", f"{directory}.wav"], check=True)
    for file in os.listdir():
        if file.endswith(".wav") and file != f"{directory}.wav":
            os.remove(file)
    os.chdir("../..")


def getTitle(url):
    return url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]


def get_url(url):
    directory = getTitle(url)
    make_folder(directory)
    extractAudio(url, directory)
    mergeAudio(directory)
