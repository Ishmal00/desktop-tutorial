import pickle
import pandas as pd

class ModelPredictor:
    """
    Loads trained model and scaler to make predictions on new input.
    """
    def __init__(self, model_path='svm_model.pkl', scaler_path='scaler.pkl'):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)
        print("✅ Model and scaler loaded.")

    def predict(self, input_df):
        input_scaled = self.scaler.transform(input_df)
        prediction = self.model.predict(input_scaled)
        return prediction
