"""
Download and unzip the data.
"""
from argparse import ArgumentParser
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

from config import fname

parser = ArgumentParser(__doc__)
parser.add_argument('subject', type=int, help='Subject to process [1-64]')
args = parser.parse_args()

request = urlopen(fname.url(subject=args.subject))
zip_data = BytesIO(request.read())
with ZipFile(zip_data) as zipfile:
    zipfile.extractall(fname.data_dir)
