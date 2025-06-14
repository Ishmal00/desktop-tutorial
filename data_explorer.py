
import pandas as pd

class DataExplorer:
    """
    A class for dynamic dataset exploration:
    - Automatically loads given CSV file
    - Shows head, tail, info, stats, nulls, and drop nulls
    """

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        print(f"✅ File loaded: {file_path}")

    def show_head(self):
        return self.df.head()

    def show_tail(self):
        return self.df.tail()

    def show_info(self):
        self.df.info()

    def describe_data(self):
        return self.df.describe()
