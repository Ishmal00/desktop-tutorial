
class DataCleaner:
    """
    Cleans the dataset by removing null values and duplicate rows.
    Shows row count and data preview after each step.
    """
    def __init__(self, dataframe):
        self.df = dataframe
        self.original_rows = dataframe.shape[0]
        print(f"Original rows: {self.original_rows}")

    def check_nulls(self):
        """Prints null count per column and previews rows with nulls."""
        nulls = self.df.isnull().sum()
        print("\nNull values per column:\n", nulls)
        print("\nPreview of rows with nulls:")
        print(self.df[self.df.isnull().any(axis=1)].head())

    def remove_nulls(self):
        """Removes rows with any null values."""
        rows_before = self.df.shape[0]
        self.df = self.df.dropna()
        rows_after = self.df.shape[0]
        print(f"Removed {rows_before - rows_after} rows with null values.")
        return self.df

    def remove_duplicates(self):
        """Removes duplicate rows from the dataset."""
        before = self.df.shape[0]
        self.df = self.df.drop_duplicates()
        after = self.df.shape[0]
        print(f"Removed {before - after} duplicate rows.")
        return self.df
