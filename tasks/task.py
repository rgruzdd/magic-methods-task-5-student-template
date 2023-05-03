import os
import shutil
import uuid


class TempDir():

    def __init__(self, dir_path=None):
        self.dir_path = dir_path or os.getcwd()
        self.tmpdir = str(uuid.uuid4())
        self.save_dir = os.path.join(self.dir_path, self.tmpdir)

    def __enter__(self):
        os.mkdir(self.save_dir)
        os.chdir(self.save_dir)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.dir_path)
        shutil.rmtree(self.save_dir)

