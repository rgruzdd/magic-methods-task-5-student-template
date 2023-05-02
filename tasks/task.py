import os
import shutil
import tempfile
from pathlib import Path


class TempDir(object):

    def __init__(self, suffix=None, prefix=None, dir=None):
        dir = os.getcwd()
        self.name = tempfile.mkdtemp(suffix, prefix, dir=dir)
        os.mkdir(self.name)

    def __enter__(self):
        return self.name

    def __exit__(self, exc, value, tb):
        shutil.rmtree(self.name)
