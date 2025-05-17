1. Import Libraries
We begin by importing essential Python libraries:
pandas and numpy for data manipulation and numerical operations.
seaborn and matplotlib for data visualization.
2. Importing Data and Initial Inspection
Loaded the dataset into a DataFrame.
Checked the first few rows to get a glimpse of the data.
Inspected for missing values and data types to understand data quality.
Generated statistical summaries to learn about data distribution and scale.
3. Exploratory Data Analysis (EDA)
Performed EDA to explore relationships and distributions in the data:
Created pairplots to visualize relationships between variables.
Plotted the distribution of house prices to check for skewness or outliers.
Generated a heatmap showing correlations between features to identify strong predictors.
4. Feature Selection and Engineering
Created a new feature Bathrooms by subtracting the number of bedrooms from total rooms, assuming the remainder are bathrooms.
Selected features believed to impact house price:
Average area number of rooms
Average area number of bedrooms
Bathrooms (engineered)
Defined the target variable as the house Price.
5. Splitting the Data
Split the dataset into training and testing sets using a 60-40 split.
Training data is used to fit the model; testing data is used to evaluate it.
6. Creating and Training the Model
Initialized a Linear Regression model.
Trained the model using the training data.
7. Model Evaluation – Coefficients
Printed the model intercept and coefficients to understand the influence of each feature on price.
8. Making Predictions and Visualizing Results
Used the model to predict prices on the test set.
Created a scatter plot comparing actual vs predicted prices to assess accuracy visually.
Plotted the distribution of residuals (errors) to check for bias or skew.
9. Regression Evaluation Metrics
Calculated key metrics to quantify model performance:
Mean Absolute Error (MAE): Average magnitude of prediction errors.
Mean Squared Error (MSE): Average squared errors, penalizing larger errors.
Root Mean Squared Error (RMSE): Square root of MSE, in same units as target variable.

Summary
This structured approach—from data exploration to model evaluation—helps ensure that the house price prediction is both accurate and interpretable.
The insights gained from EDA and model coefficients guide improvements and feature engineering for future iterations.

Project Structure:

House Price Prediction Dataset.csv:
The dataset used to train and test the model. Contains columns like area, number of rooms, bedrooms, and price.

Linear_Regression_Model.ipynb:
A complete notebook containing:
Data loading and cleaning
Exploratory Data Analysis (EDA)
Feature engineering
Model training and evaluation
Visualizations

Linear_Regression_Model.pkl:
The trained Linear Regression model saved using pickle. It is used by app.py to make real-time predictions.

app.py:
The main Flask application file that:
Loads the pickled model
Renders the HTML form
Accepts user input
Predicts house price
Returns the result to the frontend

index.html:
A styled HTML form where users can input:
Area (in sq ft)
Number of Bedrooms
Number of Bathrooms
Submits the form to /predict route to get the predicted price.




