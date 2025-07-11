# Step 1: Import required libraries
import pandas as pd
import seaborn as sns
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 2: Load the 'tips' dataset
df = sns.load_dataset('tips')

# Step 3: Preprocessing
# Identify categorical features
categorical_features = ['sex', 'smoker', 'day', 'time']

# Split features and target
X = df.drop('tip', axis=1)
y = df['tip']

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Initialize CatBoost Regressor
model = CatBoostRegressor(
    iterations=100,
    learning_rate=0.1,
    depth=6,
    cat_features=categorical_features,
    verbose=0
)

# Step 6: Fit the model
model.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.3f}")
