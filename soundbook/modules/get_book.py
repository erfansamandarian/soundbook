import re
import requests
import json

# https://bookaudiobooks.com/?s=test
# https://bigaudiobooks.com/?s=test


def get_book(book):
    small = requests.get(f"https://bookaudiobooks.com/?s={book}")

    big = requests.get(f"https://bigaudiobooks.com/?s={book}")

    print("SMALL :: %s" % (small))
    print("BIG :: %s" % (big))
