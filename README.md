# Customer Churn Prediction Using Customer Service Call Dataset
## Project Overview
This project is part of my Masters in Data Science preliminary project at the University of Pittsburgh. The primary objective of this project is to predict customer churn and identify the key features influencing this behavior using the customer service call dataset. The dataset contains various data points that highlight customer characteristics and company interactions but does not include any personally identifiable information.

This project follows a systematic approach, including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, model performance evaluation, and cross-validation. By applying robust predictive models, we identified the most significant features influencing customer churn, ultimately helping businesses enhance their retention strategies.

## Key Findings
Significant Predictors of Churn:

The analysis identified two main variables: total_day_minutes and total_eve_minutes, along with a principal component feature, pca_cluster, as significant predictors of customer churn.
Model Development:

The study developed and evaluated several models. The primary model, Model 8, which included interaction terms and polynomial features, demonstrated the highest performance.
Model Performance:

Model 8 achieved a mean ROC_AUC score of 0.6798 with a 95% confidence interval of 0.0117.
These results emphasize the importance of advanced feature engineering and model selection techniques in accurately predicting customer churn.
Business Impact
The findings from this project provide actionable insights that can be used to enhance customer retention strategies. By identifying the key factors contributing to churn, businesses can take proactive measures to improve customer satisfaction and loyalty, thereby contributing to their overall stability and growth.

## Methodology
1. (Data Preprocessing)[notebooks/1. Data Preprocessing EDA.ipynb]
Data cleaning and preparation.
Handling missing values and outliers.
Encoding categorical variables and normalizing numerical features.
2. (Exploratory Data Analysis)[notebooks/1. Data Preprocessing EDA.ipynb]
Understanding the distribution and relationships between variables.
Visualizing key patterns and trends in the dataset.
3. (Feature Engineering)[notebooks/2. Feature Engineering.ipynb]
Creation of new features to capture complex patterns.
Principal Component Analysis (PCA) and clustering to identify significant feature groups.
4. (Model Building)[3. Models Building.ipynb]
Development of logistic regression models, including both linear terms and interaction terms.
Incorporation of polynomial features to capture non-linear relationships.
5. (Model Performance Evaluation)[4. Confusion Matrix.ipynb]
Evaluation of models using metrics such as ROC-AUC score, precision, recall, and F1-score.
Cross-validation to ensure model generalization.
6. (Prediction and Cross-Validation)[5. Model Prediction and Perfomance.ipynb]
Validation of model performance using k-fold cross-validation to assess stability and avoid overfitting.

## Models and Results
Model 8: Primary Model
Features: Includes linear terms, interaction terms, and polynomial features.
Performance: Achieved a mean ROC_AUC score of 0.6798 with a 95% confidence interval of 0.0117.
This model demonstrated the best performance and can be used for predicting churn on new datasets.

## Conclusion
This project highlights the critical importance of advanced feature engineering and model selection techniques in accurately predicting customer churn. The insights gained from this analysis offer valuable guidance for businesses aiming to enhance their customer retention strategies. By focusing on significant predictors such as total_day_minutes, total_eve_minutes, and pca_cluster, companies can develop targeted interventions to reduce churn and promote long-term customer loyalty.

## How to Use
Dataset: Ensure you have the customer service call dataset.
Preprocessing: Apply the data preprocessing steps as outlined in the methodology section.
Model Training: Use the provided models or train new ones using the same features and techniques.
Prediction: Apply the trained model to new data to predict customer churn.
Evaluation: Assess model performance on new datasets and refine as necessary.
Future Work
Further Feature Exploration: Explore additional feature engineering techniques to uncover other potential predictors.
Advanced Modeling Techniques: Experiment with other machine learning algorithms such as Random Forest, Gradient Boosting, or Neural Networks to potentially improve prediction accuracy.


