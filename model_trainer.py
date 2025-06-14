import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pickle

class ModelTrainer:
    """
    Handles training of SVM model, scaling, and model saving.
    """
    def __init__(self, dataframe):
        self.df = dataframe
        self.model = None
        self.scaler = None

    def preprocess(self):
        X = self.df.drop(['target'], axis=1)
        y = self.df['target']

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    def train(self, X_train, y_train):
        self.model = SVC()
        self.model.fit(X_train, y_train)
        print("✅ Model training complete.")

    def save_model(self, model_path='svm_model.pkl', scaler_path='scaler.pkl'):
        with open(model_path, 'wb') as f:
            pickle.dump(self.model, f)
        with open(scaler_path, 'wb') as f:
            pickle.dump(self.scaler, f)
        print("✅ Model and scaler saved.")
