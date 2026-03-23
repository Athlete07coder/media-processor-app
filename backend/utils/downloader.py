import requests

def download_file(url, path):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code != 200:
            raise Exception("Invalid URL or download failed")

        with open(path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

    except Exception as e:
        raise Exception(f"Download error: {str(e)}")