import pandas as pd
import numpy as np

# Input arrays
P = np.array([1, 2, 2, 3])
Q = np.array([3, 2, 3, 3])
R = np.array([3, 6, 6, 6])

m = len(P)
G = np.zeros((m, 10))

# Calculating values and populating matrix G
for n in range(m):
    G[n, 0] = R[n] * (P[n] + Q[n])
    G[n, 1] = R[n] * (P[n] * Q[n])
    G[n, 2] = R[n] * (2 / (P[n] + Q[n]))
    G[n, 3] = R[n] * (P[n]**2 + Q[n]**2)
    G[n, 4] = R[n] * (np.sqrt((P[n] * Q[n]) / (P[n] + Q[n])))
    G[n, 5] = R[n] * (np.sqrt((P[n] + Q[n] - 2) / (P[n] * Q[n])))
    G[n, 6] = R[n] * (np.sqrt(1 / (P[n] * Q[n])))
    G[n, 7] = R[n] * (np.sqrt(1 / (P[n] + Q[n])))
    G[n, 8] = R[n] * (2 * (np.sqrt(P[n] * Q[n]) / (P[n] + Q[n])))
    G[n, 9] = R[n] * (P[n] + Q[n])**2

# Summing values along axis 0
results = G.sum(axis=0)

# Metrics labels
metrics = ["M1", "M2", "H", "F", "SS", "ABC", "RI", "SC", "GA", "HZ"]

# Creating DataFrame
indices_df = pd.DataFrame([results], columns=metrics)

# Formatting DataFrame values to 4 decimal places
for col in indices_df.columns:
    indices_df[col] = indices_df[col].apply(lambda x: f'{x:.4f}')

# Exporting DataFrame to Excel file
indices_df.to_excel('Topological_Indices.xlsx', index=False)
