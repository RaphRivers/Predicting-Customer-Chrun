# Import required modules for the project 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import roc_curve, auc
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, roc_auc_score
import statsmodels.formula.api as smf

# Read in the dataset 
churn_df = pd.read_csv('churn_data.csv')