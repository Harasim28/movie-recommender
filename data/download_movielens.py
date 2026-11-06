"""Скачивает MovieLens в data/. По умолчанию ml-latest-small (~1 МБ, для разработки).

Использование:
    python data/download_movielens.py            # ml-latest-small
    python data/download_movielens.py --full     # ml-25m (~260 МБ, для финальных рунов)
"""
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

URLS = {
    "ml-latest-small": "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip",
    "ml-25m": "https://files.grouplens.org/datasets/movielens/ml-25m.zip",
}

def main() -> None:
    key = "ml-25m" if "--full" in sys.argv else "ml-latest-small"
    data_dir = Path(__file__).parent
    zip_path = data_dir / f"{key}.zip"
    if not zip_path.exists():
        print(f"Скачиваю {key}…")
        urllib.request.urlretrieve(URLS[key], zip_path)
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(data_dir)
    Path(zip_path).unlink()
    print(f"Готово: {data_dir / key}/")

if __name__ == "__main__":
    main()
