from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="soundbook",
    description="search, download, and merge audiobooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erfan Samandarian",
    author_email="mail@erfansamandarian.com",
    url="https://erfansamandarian.com/soundbook",
    license="MIT",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["setuptools", "ffmpeg", "mutagen", "eyed3", "pillow", "requests", "sox", "yt_dlp"],
    py_modules=["soundbook"],
    entry_points={"console_scripts": ["soundbook=soundbook:main"]},
)
