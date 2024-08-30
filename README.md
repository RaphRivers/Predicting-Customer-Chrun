# Customer Churn Prediction Using Customer Service Call Dataset
## Project Overview
The primary objective of this project is to use the customer service call dataset to predict customer churn and identify the key features influencing this behavior. This project follows a systematic approach, including data preprocessing, exploratory data analysis (EDA), feature engineering, model building, model performance evaluation, and cross-validation. By applying robust predictive models, I identified the most significant features influencing customer churn, ultimately helping businesses enhance their retention strategies. The dataset contains various data points that highlight customer characteristics and company interactions but does not include personally identifiable information.

## Dataset 
The <a href="https://www.rdocumentation.org/packages/modeldata/versions/1.3.0/topics/mlc_churn" target="_blank">Dataset</a> used in this project is sourced from the modeldata package in R, an MLC++ machine learning software challenge problem. It contains 19 input variables and 1 binary outcome. These 19 inputs represent customer characteristics, including location, account history, and purchase behavior. The variable names are detailed in the data dictionary EDA description. The critical outcome of interest is indicated by the "churn" column, which specifies whether a customer has churned ("yes") or not ("no"). Churn refers to a customer leaving and no longer purchasing products from the company.


## Key Findings
### Significant Predictors of Churn:

The analysis identified two main variables, total_day_minutes and total_eve_minutes, and a principal component feature, pca_cluster, as significant predictors of customer churn.

### Model Development:

The study developed and evaluated several models. The primary model, Model 8, which included interaction terms and polynomial features, demonstrated the highest performance.

### Model Performance:

Model 8 achieved a mean ROC_AUC score of 0.6798 with a 95% confidence interval of 0.0117.
These results emphasize the importance of advanced feature engineering and model selection techniques in accurately predicting customer churn.

### Business Impact

The findings from this project provide actionable insights that can be used to enhance customer retention strategies. By identifying the key factors contributing to churn, businesses can take proactive measures to improve customer satisfaction and loyalty, thereby contributing to their overall stability and growth.

## Methodology
1. [**Data Preprocessing**](https://github.com/RaphRivers/Predicting-Customer-Chrun/blob/main/notebooks/1.%20Data%20Preprocessing%20EDA.ipynb)
Data cleaning and preparation.
Handling missing values and outliers.
Encoding categorical variables and normalizing numerical features.
2. [**Exploratory Data Analysis**](https://github.com/RaphRivers/Predicting-Customer-Chrun/blob/main/notebooks/1.%20Data%20Preprocessing%20EDA.ipynb)
Understanding the distribution and relationships between variables.
Visualizing key patterns and trends in the dataset.
3. [**Feature Engineering**](https://github.com/RaphRivers/Predicting-Customer-Chrun/blob/main/notebooks/2.%20Feature%20Engineering.ipynb)
Creation of new features to capture complex patterns.
Principal Component Analysis (PCA) and clustering to identify significant feature groups.
4. [**Model Building**](https://github.com/RaphRivers/Predicting-Customer-Chrun/blob/main/notebooks/3.%20Models%20Building.ipynb)
Development of logistic regression models, including both linear terms and interaction terms.
Incorporation of polynomial features to capture non-linear relationships.
5. [**Model Performance Evaluation**](https://github.com/RaphRivers/Predicting-Customer-Chrun/blob/main/notebooks/4.%20Confusion%20Matrix.ipynb)
Evaluation of models using metrics such as ROC-AUC score, precision, recall, and F1-score.
Cross-validation to ensure model generalization.
6. [**Prediction and Cross-Validation**](https://github.com/RaphRivers/Predicting-Customer-Chrun/blob/main/notebooks/5.%20Model%20Prediction%20and%20Perfomance.ipynb)
Validation of model performance using input grid cross-validation to assess stability and avoid overfitting.

## Models and Results
Model 8: Primary Model
Features: Includes linear terms, interaction terms, and polynomial features.
Performance: Achieved a mean ROC_AUC score of 0.6798 with a 95% confidence interval of 0.0117.
This model demonstrated the best performance and can be used to predict churn on new datasets.

## Conclusion
This project highlights the critical importance of advanced feature engineering and model selection techniques in accurately predicting customer churn. The insights gained from this analysis offer valuable guidance for businesses aiming to enhance their customer retention strategies. By focusing on significant predictors such as total_day_minutes, total_eve_minutes, and pca_cluster, companies can develop targeted interventions to reduce churn and promote long-term customer loyalty.

## How to Use
Dataset: Ensure you have the customer service call dataset you can get it following this link https://www.rdocumentation.org/packages/modeldata/versions/1.3.0/topics/mlc_churn.

Preprocessing: Apply the data preprocessing steps as outlined in the methodology section.

Model Training: Use the provided models or train new ones using the same features and techniques.

Prediction: Apply the trained model to new data to predict customer churn.

Evaluation: Assess model performance on new datasets and refine as necessary.

## Future Work
Further Feature Exploration: Explore additional feature engineering techniques to uncover other potential predictors.

Advanced Modeling Techniques: To improve prediction accuracy, experiment with other machine learning algorithms, such as Random Forest, Gradient Boosting, or Neural Networks.

## Contribution
Contribution to this project is highly encouraged. Thank you!


