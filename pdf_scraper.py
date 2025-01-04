from pypdf import PdfReader
from argparse import ArgumentParser
from pathlib import Path

from lib.pdf.scrape_models import BaseScraper
# TODO: import and use SQLAlchemy


def write_to_db():
    raise NotImplementedError

def xml_to_sql():
    raise NotImplementedError

def scrape(filename: Path):
    if filename.suffix != ".pdf":
        raise TypeError(f"{filename} does not have pdf extension")
    reader = PdfReader(filename)
    pages = []
    for reader in reader.pages:
        pages.append(reader.extract_text())
    scraper = BaseScraper(filename, pages)
    scraper.structure()

def parse_args():
    parser = ArgumentParser(
        prog="PdfScraper",
        description="Scrapes home data from pdf files and collates them into a database"
    )
    parser.add_argument("filename")
    parser.add_argument("-d", "--directory", action="store_true")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    path = Path(args.filename)
    if args.directory:
        if not path.is_dir():
            raise ValueError(f"path: {path} is not a directory, remove --directory")

        for file in path.iterdir():
            try:
                scrape(file)
            except TypeError:
                pass
    else:
        if path.is_dir():
            raise ValueError(f"path: {path} is directory, add --directory.")
        scrape(path)

if __name__ == "__main__":
    main()
