# Customer Loyalty Prediction Model
## Project Overview
This project contains a machine learning model used to predict customer loyalty based on various customer features such as age, annual income, purchase amount, region, and purchase frequency. The model has been trained using a **Random Forest Regressor** and achieved **99% accuracy**.
## Repository Structure

```bash
├── model/
│   ├── model.pkl
│   ├── label_encoder.pkl
│
├── notebook/
│   ├── Customer-Loyalty-Prediction-Model.ipynb
│
├── script/
│   ├──customer_loyalty_prediction.py
├── requirements.txt
└── README.md
└── LICENSE.md 

```

## Model Details
- **Algorithm**: Random Forest Regressor
- **Input Features**:
  - `Age`: Integer representing the age of the customer.
  - `Annual Income`: Float representing the customer's annual income.
  - `Purchase Amount`: Float representing the amount the customer spent.
  - `Region`: The region where the customer is located (`North`, `South`, `West`, `East`).
  - `Purchase Frequency`: Integer representing how frequently the customer makes purchases.
  
- **Target**: Customer loyalty score, which is a numeric value representing the loyalty level of the customer.
- ## Requirements

- Python 3.x
- Required Python Libraries:
  - `pandas`
  - `scikit-learn`
  - `pickle`

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/MinaIbrahim10/customer-loyalty-prediction.git
    cd Customer-Loyalty-Prediction-Model


    ```

2. Make sure you have Python installed. You can check this by running:

    ```bash
    python --version
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python customer_loyalty_prediction.py
    ```

5. Follow the on-screen prompts to enter the customer details:
    - Age (integer)
    - Annual Income (numeric)
    - Purchase Amount (numeric)
    - Purchase Frequency (integer)
    - Region (choose from North, South, West, East)

6. The script will output a predicted customer loyalty score.

## Performance Metrics

The model was evaluated using the following regression-specific metrics:

- **R-squared (R²)**: 0.99906 - Explains the proportion of the variance in the dependent variable that is predictable from the independent variables.
- **Mean Squared Error (MSE)**: 0.00371 - Measures the average squared difference between the predicted and actual values.
- **Root Mean Squared Error (RMSE)**: 0.06091 - The square root of MSE, providing a more interpretable error measure.
- **Mean Absolute Error (MAE)**: 0.02145 - Measures the average magnitude of errors in predictions without considering their direction.
- **Mean Absolute Percentage Error (MAPE)**: 0.00515 - Measures the percentage error between predicted and actual values.
- **Explained Variance Score (EVS)**: 0.99908 - Explains how well the model accounts for the variance in the data.

These performance metrics indicate that the model is highly accurate and performs well on the dataset, with minimal error.

## Contributors

- **Mina Ibrahim**: Developer, model training, and deployment.
- **Karam Ghazy** ([karam-ghazy](https://github.com/karam-ghazy)): Developer, model training, and deployment, with support in data preprocessing and feature engineering.


## Future Work

- Fine-tuning the model with more data.
- Adding cross-validation and further performance metrics.
- Incorporating more customer features (e.g., past purchases, demographics, etc.).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
    

