#  House Classification Project

##  Overview
An end-to-end ML pipeline built in Python using `SVC` to classify house categories based on features.

##   Features
- Object-Oriented code structure
- SVC (Support Vector Classifier)
- Visualizations (Histograms, Heatmaps)
- Light-mode Streamlit UI
- Scaler + Model saved using `pickle`

##   Folder Structure
- `src/` - All modular class files
- `app.py` - Streamlit frontend
- `README.md` - Project documentation

##   Running the App

pip install -r requirements.txt
streamlit run app.py
```


#  DETAIL:

This project is focused on predicting housing prices in California using **Machine Learning (Support Vector Regression)**. The dataset includes a wide range of real estate and demographic features. The aim is to create a clean ML pipeline and a deployable **Streamlit web app** that allows users to input values and get instant predictions.

---

##  Project Structure

├── main.ipynb           # Jupyter Notebook (EDA, preprocessing, training)
├── app.py               # Streamlit web app for predictions
├── housing.csv          # Dataset
├── model.pkl            # Trained SVR model
├── scaler.pkl           # Saved StandardScaler
├── requirements.txt     # Python dependencies
├── images/              # Graphs and visualizations used in notebook
└── README.md            # Project documentation (this file)

---

##  Objective

- Clean and preprocess the California Housing Dataset
- Engineer new features to improve model performance
- Train an accurate **Support Vector Machine (SVR)** model
- Evaluate using error metrics and graphs
- Deploy a working **Streamlit app** for predictions

---

## Machine Learning Workflow

### 1. Data Preprocessing

- Removed missing values using `dropna()`
- Applied log transformation to skewed columns
- Performed **one-hot encoding** on the `ocean_proximity` column
- Engineered new features:
  - `bedroom_ratio` = total_bedrooms / total_rooms
  - `household_rooms` = total_rooms / households
  - `bedroom_households` = total_bedrooms / households

### 2. Feature Scaling

- Used `StandardScaler` to normalize features before feeding into SVR model

### 3. Model Training

- Applied **Support Vector Regression (SVR)** with default kernel
- Trained on processed data and stored using `pickle`

### 4. Model Evaluation

- Used **R² Score**, **MAE**, and **MSE** for evaluation
- Compared actual vs predicted values using graphs

---

##  Visualizations Included

- **Heatmap** to show feature correlations
- **Distribution plots** for continuous variables
- **Scatter plot** of median income vs house price
- **Actual vs Predicted** plot to evaluate model visually

All graphs are available inside the `images/` folder and shown within the notebook.

---

##  Streamlit Web App

A fully functional Streamlit web app (`app.py`) is included.
 It:

- Takes user input via sidebar
- Preprocesses the input exactly like the training pipeline
- Loads the trained model and scaler
- Displays predicted price instantly on-screen

---

## How to Run the Project Locally

1. Clone the repository:
   git clone https://github.com/Ishmal00/desktop-tutorial.git
   cd Cal-House-Predict

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

---

##  Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Pickle
- Jupyter Notebook



---

##  Author

**Ishmal Nadeem**  
[GitHub Profile](https://github.com/Ishmal00)

---

## Feedback

Suggestions and improvements are welcome! Feel free to open issues or submit pull requests.
