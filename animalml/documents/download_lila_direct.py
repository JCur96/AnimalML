import os
import random
from tqdm import tqdm


from multiprocessing.pool import ThreadPool
from collections import defaultdict
from data_management.lila.lila_common import read_lila_all_images_file, is_empty, lila_base_urls. azure_url_to_gcp_http_url
from md_utils.url_utils import download_url


import json
import urllib.request
import tempfile
import zipfile
import itertools
import shutil
import pandas as pd
from urllib.parse import urlparse


class DataDownloader:
    def __init__(self, url, destination_folder):
        self.url = url
        self.destination_folder = destination_folder

    def download(self):
        raise NotImplementedError("Download method must be implemented by subclass")

class AzureDownloader(DataDownloader):
    def __init__(self, url, destination_folder):
        super().__init__(url, destination_folder)
        # might want some azure account and credential details here at some point?
    def download(self):
        # setup
        
        


class GSDownloader(DataDownloader):
    def download(self):
        pass
class S3Downloader(DataDownloader):
    def download(self):
        pass
