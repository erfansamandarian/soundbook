import os
import subprocess


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
