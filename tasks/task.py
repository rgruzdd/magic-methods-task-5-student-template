import os
import shutil
import tempfile
from pathlib import Path


class TempDir(object):

    def __init__(self, suffix=None, prefix=None, dir=None):
        os.chdir("D:\\pythonProject63")
        dir = os.getcwd()
        self.name = tempfile.mkdtemp(suffix, prefix, dir=dir)
        name = self.name.split('\\')[-1]
        path = Path(self.name)
        os.mkdir(self.name)

    def __enter__(self):
        return self.name

    def __exit__(self, exc, value, tb):
        shutil.rmtree(self.name)

