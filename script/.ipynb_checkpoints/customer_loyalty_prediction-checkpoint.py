import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the model
with open('model.pkl', 'rb') as file:
    try:
        rareg = pickle.load(file)
    except (FileNotFoundError, pickle.UnpicklingError):
        print("Error loading the model. Please check if 'model.pkl' exists and is not corrupted.")
        exit(1)

# Load the LabelEncoder for 'region' encoding
with open('label_encoder.pkl', 'rb') as le_file:
    try:
        Le = pickle.load(le_file)
    except (FileNotFoundError, pickle.UnpicklingError):
        print("Error loading the LabelEncoder. Please check if 'label_encoder.pkl' exists.")
        exit(1)

# Input collection with validation and type casting
try:
    age = int(input('Enter the customer age (integer): '))
    annual_income = float(input('Enter the customer annual income (numeric): '))
    purchase_amount = float(input('Enter the customer purchase amount (numeric): '))
    purchase_frequency = int(input('Enter the customer purchase frequency (integer): '))
except ValueError:
    print("Invalid input. Please enter the correct data types for each field.")
    exit(1)

# Predefined regions and case-insensitive input
regions = ['North', 'South', 'West', 'East']

region = input('Enter the customer region (North, South, West, East): ').strip().capitalize()

if region not in regions:
    print(f"Invalid region. Please choose from {regions}.")
    exit(1)

# Encoding the 'region' field
try:
    encoded_region = Le.transform([region])[0]
except ValueError:
    print(f"Error: The region '{region}' is not recognized. Please check the input.")
    exit(1)

# Create a DataFrame for the input
df1 = pd.DataFrame(columns=['age', 'annual_income', 'purchase_amount', 'region', 'purchase_frequency'])
df1.loc[0] = [age, annual_income, purchase_amount, encoded_region, purchase_frequency]

# Make the prediction
try:
    prediction = rareg.predict(df1)
    print(f"Customer loyalty score is {prediction[0]:.1f}")
except Exception as e:
    print(f"Error during prediction: {e}")
    exit(1)
