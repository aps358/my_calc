""" CSV Read Class """

import os
import shutil
import pandas as pd


class CSVRead:
    """ Defining Class Constructor in here """

    # pylint: disable=too-few-public-methods

    @staticmethod
    def read_data(path):
        return pd.read_csv(path)

    @staticmethod
    def move_file(curr_path, move_path):
        os.rename(curr_path, move_path)
        os.replace(curr_path, move_path)
        shutil.move(curr_path, move_path)
