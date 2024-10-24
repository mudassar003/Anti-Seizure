<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - On QSPR Analysis of Anti-Seizure Drugs Via Statistical Models</title>
</head>
<body>

<h1>On QSPR Analysis of Anti-Seizure Drugs Via Statistical Models</h1>

<p>This repository contains code used for the quantitative structure-property relationship (QSPR) analysis of anti-seizure drugs. The analysis was performed using statistical models such as multiple linear regression and cross-validation techniques. The primary goal of this study is to investigate the relationships between molecular properties and topological indices of anti-seizure drugs.</p>

<h2>Code Overview</h2>

<p>The project consists of two main Python scripts:</p>

<ol>
    <li><strong>Topological Indices Calculation</strong>: This code calculates various topological indices based on molecular properties of the drugs.</li>
    <li><strong>Regression and Cross-Validation</strong>: This code performs regression analysis using k-fold cross-validation to model the relationship between molecular properties and a topological index.</li>
</ol>

<h3>Files Included:</h3>

<ul>
    <li><code>Topological_Indices.py</code>: Calculates the topological indices for each drug and saves the results in an Excel file.</li>
    <li><code>QSPR_Regression.py</code>: Performs regression analysis using 5-fold cross-validation, calculating the mean squared error (MSE) for each property.</li>
</ul>

<h3>Dependencies</h3>

<p>To run the provided code, you will need to install the following Python libraries:</p>

<ul>
    <li><code>pandas</code></li>
    <li><code>numpy</code></li>
    <li><code>scikit-learn</code></li>
    <li><code>statsmodels</code></li>
    <li><code>openpyxl</code> (for exporting Excel files)</li>
</ul>

<p>You can install all the dependencies using the following command:</p>

<pre><code>pip install pandas numpy scikit-learn statsmodels openpyxl</code></pre>

<h2>How to Use</h2>

<h3>Topological Indices Calculation</h3>

<p>The first script calculates various topological indices based on input arrays of molecular properties. The results are stored in an Excel file.</p>

<ol>
    <li>Modify the input arrays for molecular properties (<code>P</code>, <code>Q</code>, <code>R</code>) in the script.</li>
    <li>Run the script:</li>
</ol>

<pre><code>python Topological_Indices.py</code></pre>

<p>The output will be saved as <code>Topological_Indices.xlsx</code>.</p>

<h3>QSPR Regression Analysis</h3>

<p>This script performs linear regression and k-fold cross-validation for the quantitative structure-property relationship (QSPR) analysis.</p>

<ol>
    <li>Ensure the input CSV file (<code>Data2.csv</code>) is placed in the same directory.</li>
    <li>Modify the script to include the topological index and molecular properties you are analyzing.</li>
    <li>Run the script:</li>
</ol>

<pre><code>python QSPR_Regression.py</code></pre>

<p>The script will output the regression equation and the average mean squared error (MSE) from the cross-validation for each molecular property.</p>

<h2>Code Explanation</h2>

<h3>Topological Indices Calculation (<code>Topological_Indices.py</code>)</h3>

<ul>
    <li><strong>Input</strong>: Arrays <code>P</code>, <code>Q</code>, and <code>R</code> representing molecular properties.</li>
    <li><strong>Process</strong>: The script calculates ten different topological indices based on combinations of the properties in <code>P</code>, <code>Q</code>, and <code>R</code>. These include formulas involving square roots, sums, products, and powers.</li>
    <li><strong>Output</strong>: The resulting matrix of indices is summed, formatted, and saved as an Excel file.</li>
</ul>

<h3>QSPR Regression and Cross-Validation (<code>QSPR_Regression.py</code>)</h3>

<ul>
    <li><strong>Input</strong>: A CSV file containing molecular properties and topological indices.</li>
    <li><strong>Process</strong>:
        <ol>
            <li>For each index and molecular property pair, the code prepares the data by adding a constant to the index.</li>
            <li>It uses 5-fold cross-validation to split the data into training and test sets, fitting a linear regression model for each fold.</li>
            <li>After training, it calculates the mean squared error (MSE) for each fold and averages the MSE across all folds.</li>
            <li>Finally, the code fits a regression model on the entire dataset to calculate the intercept and slope for the regression equation.</li>
        </ol>
    </li>
    <li><strong>Output</strong>: The regression equation for each molecular property and the average MSE from cross-validation.</li>
</ul>

<h2>Example Output</h2>

<p>Example of a regression equation for the property 'Boiling Point':</p>

<pre><code>Boiling Point = 128.4567 + 0.6789 * RezG3(G)
Average MSE from K-Fold Validation: 0.0123</code></pre>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>

<h2>Contact</h2>

<p>For any questions or further information, please contact <strong> Mudassar Rehman</strong> at <strong>mudassar.rehman687@gmail.com</strong>.</p>

</body>
</html>
