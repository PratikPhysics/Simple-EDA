import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# Load the dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
data = pd.read_csv(url)

# Display basic info
print("Dataset shape:", data.shape)
print("\nFirst few rows:")
print(data.head())
print("\nMissing values:")
print(data.isnull().sum())

## Data Preprocessing

# 1. Feature selection - drop irrelevant columns
data = data.drop(['Name'], axis=1)

# 2. Feature engineering
data['FamilySize'] = data['Siblings/Spouses Aboard'] + data['Parents/Children Aboard']
data['IsAlone'] = (data['FamilySize'] == 0).astype(int)

# 3. Convert categorical variables
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 4. Separate features and target
X = data.drop('Survived', axis=1)
y = data['Survived']

# 5. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

## Handle missing values

# For numerical features
num_features = ['Age', 'Fare', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'FamilySize', 'IsAlone']
cat_features = ['Pclass', 'Sex']

# Impute missing values for numerical features
num_imputer = SimpleImputer(strategy='median')
X_train[num_features] = num_imputer.fit_transform(X_train[num_features])
X_test[num_features] = num_imputer.transform(X_test[num_features])

# No missing values in categorical features in this dataset, but here's how you would handle them:
# cat_imputer = SimpleImputer(strategy='most_frequent')
# X_train[cat_features] = cat_imputer.fit_transform(X_train[cat_features])
# X_test[cat_features] = cat_imputer.transform(X_test[cat_features])

## Feature Scaling

# Scale numerical features
scaler = StandardScaler()
X_train[num_features] = scaler.fit_transform(X_train[num_features])
X_test[num_features] = scaler.transform(X_test[num_features])

## One-Hot Encoding for categorical variables

# Since we've already converted Sex to numerical, we only need to one-hot encode Pclass
encoder = OneHotEncoder(sparse=False, drop='first')
encoded_cols = encoder.fit_transform(X_train[['Pclass']])
encoded_cols_test = encoder.transform(X_test[['Pclass']])

# Create column names for the encoded features
class_names = [f'Pclass_{i}' for i in encoder.categories_[0][1:]]

# Add encoded columns to dataframe
X_train[class_names] = encoded_cols
X_test[class_names] = encoded_cols_test

# Drop original Pclass column
X_train = X_train.drop('Pclass', axis=1)
X_test = X_test.drop('Pclass', axis=1)

## Train Random Forest Model

# Initialize the model
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)

## Evaluate the model

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

## Feature Importance

# Get feature importances
importances = rf.feature_importances_
feature_names = X_train.columns

# Create a DataFrame for visualization
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values('Importance', ascending=False)

print("\nFeature Importances:")
print(feature_importance_df)
