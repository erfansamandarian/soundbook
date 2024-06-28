import subprocess


def extract_audio(url, directory):
    subprocess.run(
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
