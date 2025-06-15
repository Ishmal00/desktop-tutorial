import pandas as pd

class DataLoader:
    """
    A class for dynamic dataset exploration:
    - Automatically loads given CSV file
    - Shows head, tail, info, stats, nulls, and drop nulls
    """
    
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        print(f"✅ File loaded: {file_path}")

    
