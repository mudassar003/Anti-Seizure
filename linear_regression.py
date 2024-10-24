import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.api import add_constant

# Load data
df = pd.read_csv('Data2.csv')

# Define indices and properties for analysis
indices_values = ['RezG3(G)']
chemical_properties = ['Polarizability', 'Complexity', 'Boiling Point',
                       'Molecular Weight', 'Molecular Volume', 'Flash Point']

# Perform analysis
for index in indices_values:
    if index not in df.columns:
        print(f"Index '{index}' not found in the DataFrame.\n")
        continue

    for chemical_property in chemical_properties:
        if chemical_property not in df.columns:
            print(f"Chemical property '{chemical_property}' not found in the DataFrame.\n")
            continue

        # Prepare data for regression
        X = df[[index]]
        X = add_constant(X)
        y = df[chemical_property]

        # Setup k-fold cross-validation
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        model = LinearRegression()
        mse_list = []

        # Perform k-fold cross-validation
        for train_index, test_index in kf.split(X):
            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]

            # Fit the model
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            # Calculate MSE for the current fold
            mse = mean_squared_error(y_test, y_pred)
            mse_list.append(mse)

        # Average MSE across all folds
        avg_mse = np.mean(mse_list)

        # Fit model on the entire dataset for comparison / complete model stats
        full_model = model.fit(X, y)
        intercept = full_model.intercept_
        slope = full_model.coef_[1]

        # Print regression equation and average MSE
        equation = f"{chemical_property} = {intercept:.4f} + {slope:.4f} * {index}"
        print(f"Equation for {chemical_property}: {equation}")
        print(f"Average MSE from K-Fold Validation: {avg_mse:.4f}\n")
