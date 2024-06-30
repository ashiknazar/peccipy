import os
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

def hello():
    print("hello peccipy")

def impute_and_onehot_encode(df, columns_to_process):
    # Make a copy of the original dataframe
    df_processed = df.copy()
    
    # Iterate through each column in columns_to_process
    for col in columns_to_process:
        # Impute missing values with most frequent value
        imputer = SimpleImputer(strategy='most_frequent')
        df_processed[col] = pd.Series(imputer.fit_transform(df[[col]]).flatten())
        
        # Perform one-hot encoding on the column
        encoder = OneHotEncoder(drop='first', sparse_output=False)
        encoded_col = encoder.fit_transform(df_processed[[col]])
        
        # Create column names for encoded columns
        encoded_cols_names = encoder.get_feature_names_out([col])
        
        encoded_cols_df = pd.DataFrame(encoded_col, columns=encoded_cols_names)
        
        # Concatenate the encoded columns back to the dataframe
        df_processed = pd.concat([df_processed, encoded_cols_df], axis=1)
        
        # Drop the original column after encoding
        df_processed.drop(col, axis=1, inplace=True)
    
    return df_processed

