# Customer Churn Prediction Pipeline

## Project Summary

This project demonstrates an end-to-end machine learning pipeline for customer churn prediction using the Telco dataset. It includes data cleaning, feature engineering, model training, evaluation, and a Streamlit web app for live predictions. The app allows users to input customer details and instantly see churn predictions.

## Project Files

- **churn_notebook.ipynb**: This Jupyter Notebook contains the complete workflow for the customer churn prediction model. It includes data loading, exploration, cleaning, feature engineering, model training using a Random Forest classifier, evaluation, and saving the model and scaler for later use.

- **app.py**: This file is a Streamlit application that serves as a user interface for the customer churn prediction model. It loads the trained model and scaler, provides input fields for user data, and displays the prediction result based on the input.

- **requirements.txt**: This file lists the necessary Python packages required for the project, including pandas, numpy, scikit-learn, matplotlib, seaborn, and streamlit.

- **.gitignore**: This file specifies files and directories that should be ignored by version control, including Python cache files and model files with the .pkl extension.

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the notebook to train and save the model:
   ```
   jupyter notebook churn_notebook.ipynb
   ```
3. Start the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

After starting the Streamlit app, you can enter customer details in the provided input fields and click on "Predict Churn" to see the prediction result based on the input.

## Example Inputs

| Field             | Example Value         |
|-------------------|----------------------|
| Gender            | Female               |
| Senior Citizen    | No                   |
| Partner           | Yes                  |
| Dependents        | No                   |
| Tenure (months)   | 24                   |
| Phone Service     | Yes                  |
| Multiple Lines    | No                   |
| Internet Service  | Fiber optic          |
| Online Security   | No                   |
| Online Backup     | Yes                  |
| Device Protection | No                   |
| Tech Support      | Yes                  |
| Streaming TV      | Yes                  |
| Streaming Movies  | No                   |
| Contract          | One year             |
| Paperless Billing | Yes                  |
| Payment Method    | Credit card (automatic) |
| Monthly Charges   | 85.5                 |
| Total Charges     | 2050.0               |

## Data

The dataset is not included in this repository due to size and licensing.  
You can download the Telco Customer Churn dataset from [this link](https://www.openml.org/d/42178) or use the code in the notebook to load it directly.

Place the downloaded file in a `data/` folder if you want to use a local copy.