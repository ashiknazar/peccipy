
# peccipy

peccipy is a Python package designed for data preprocessing tasks, providing utilities to clean, transform, and prepare data for analysis.

## Installation

You can install peccipy using pip:

\`\`\`bash
pip install peccipy
\`\`\`

peccipy requires Python 3.6 or above.

## Functionality

### \`impute_and_onehot_encode\`

The \`impute_and_onehot_encode\` function in peccipy performs two main tasks on a pandas DataFrame:

1. **Imputation with Most Frequent Value**: It replaces missing values in specified columns with the most frequent value found in each column.

2. **One-Hot Encoding**: It applies one-hot encoding to categorical columns specified in the input list.

#### Parameters

- **dataframe**: \`pandas.DataFrame\`
  - The input DataFrame containing the data to be processed.
  
- **columns**: \`list\`
  - A list of column names from the DataFrame to apply imputation and one-hot encoding.

#### Returns

- **encoded_df**: \`pandas.DataFrame\`
  - The DataFrame with imputed values and one-hot encoded columns.

## License

This project is licensed under the MIT License. 
