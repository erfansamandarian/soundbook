# soundbook

like soundcloud but

download, merge and add cover images to audiobooks

## about

downloading audiobooks online is a pain, this tool takes away that pain

less pain is good...

## installation 

### venv

```
git clone https://github.com/erfansamandarian/soundbook

cd soundbook 

python -m venv venv

source venv/bin/activate

pip install .
```

### baller mode 

```
pip install soundbook
```

### even more baller 

```
pip install soundbook --break-system-packages
```

## usage

### by url 

```
soundbook --url "https://<website>.com/<book>/"
```

### example

```
soundbook --url "https://appaudiobooks.com/the-fountainhead-audiobook/"
```

do not pirate, pirating is bad, paying money for dead people's ip is good, believe in the system, the system is always right

### by search

<b>coming soon</b>

requests.json() not working for these shitty websites

i get 403 when i try to connect, even with the correct headers

anyone know how to do it? if so, submit a pull request

## contemplation / todo

what is fountainhead about? is it worth reading / listening to

is making a gui worth it?

need to make ffmpeg work on systems other than m-series mac

what happens if the book doesn't have a cover image?