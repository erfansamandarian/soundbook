def get_title(url):
    return url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
