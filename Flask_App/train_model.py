# import pandas as pd
# from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
# import joblib
# import time

# try:
#     print("Starting the script...")

#     # Load dataset
#     print("Loading dataset...")
#     data = pd.read_csv(r'C:\Users\thrup\Desktop\Flask_App\Flask_App\network_data.csv')
#     print("Dataset loaded successfully.")

#     # Print column names to check for discrepancies
#     print("Column names:", data.columns)

#     # Convert 'Label' column to numeric (if needed)
#     print("Converting 'Label' column to numeric...")
#     data['Label'] = pd.to_numeric(data['Label'], errors='coerce')
#     print("Conversion complete.")

#     # Drop rows with NaN in 'Label' column
#     print("Dropping rows with NaN in 'Label' column...")
#     data.dropna(subset=['Label'], inplace=True)
#     print("Rows with NaN in 'Label' column dropped.")

#     # Ensure 'Label' column contains only 0 and 1
#     print("Checking unique values in 'Label' column...")
#     unique_labels = data['Label'].unique()
#     print("Unique values in 'Label' column:", unique_labels)
#     if len(unique_labels) != 2 or set(unique_labels) != {0.0, 1.0}:
#         raise ValueError("Invalid values found in 'Label' column. Expected only 0 and 1.")

#     # Print the number of rows in the dataset
#     num_rows = data.shape[0]
#     print(f"Number of rows in the dataset after preprocessing: {num_rows}")

#     # Sample dataset for training
#     sample_size = min(2000, num_rows)
#     print(f"Sampling {sample_size} rows from the dataset...")
#     data_sampled = data.sample(n=sample_size, random_state=42)
#     print("Dataset sampled.")

#     # Define features and target
#     print("Defining features and target...")
#     X = data_sampled[['ellis-cpu.system_perc', 'ellis-cpu.wait_perc', 'ellis-load.avg_1_min',
#                       'ellis-mem.free_mb', 'ellis-net.in_bytes_sec', 'ellis-net.out_packets_sec']]
#     y = data_sampled['Label']
#     print("Features and target defined.")

#     # Scale the features
#     print("Scaling features...")
#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)
#     print("Feature scaling complete.")

#     # Split dataset into training and testing sets
#     print("Splitting dataset into training and testing sets...")
#     X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
#     print("Dataset split complete.")

#     # Train SVM model
#     print("Training SVM model...")
#     start_time = time.time()
#     model = SVC(kernel='linear', C=1.0, random_state=42)
#     model.fit(X_train, y_train)
#     print(f"SVM model trained successfully in {time.time() - start_time:.2f} seconds.")

#     # Calculate accuracy on test set
#     print("Calculating accuracy...")
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f'Accuracy: {accuracy}')

#     # Save the model to disk
#     print("Saving the model to disk...")
#     joblib.dump(model, 'svm_model.pkl')
#     print("Model saved successfully.")

#     # Save the scaler to disk
#     print("Saving the scaler to disk...")
#     joblib.dump(scaler, 'scaler.pkl')
#     print("Scaler saved successfully.")

#     # Print success message
#     print("Support Vector Machine model trained successfully and saved!")

# except Exception as e:
#     print(f"Error occurred: {str(e)}")


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import time

try:
    print("Starting the script...")

    # Load dataset
    print("Loading dataset...")
    data = pd.read_csv(r'C:\Users\thrup\Desktop\Flask_App\Flask_App\network_data.csv')
    print("Dataset loaded successfully.")

    # Print column names to check for discrepancies
    print("Column names:", data.columns)

    # Convert 'Label' column to numeric (if needed)
    print("Converting 'Label' column to numeric...")
    data['Label'] = pd.to_numeric(data['Label'], errors='coerce')
    print("Conversion complete.")

    # Drop rows with NaN in 'Label' column
    print("Dropping rows with NaN in 'Label' column...")
    data.dropna(subset=['Label'], inplace=True)
    print("Rows with NaN in 'Label' column dropped.")

    # Ensure 'Label' column contains only 0 and 1
    print("Checking unique values in 'Label' column...")
    unique_labels = data['Label'].unique()
    print("Unique values in 'Label' column:", unique_labels)
    if len(unique_labels) != 2 or set(unique_labels) != {0.0, 1.0}:
        raise ValueError("Invalid values found in 'Label' column. Expected only 0 and 1.")

    # Print the number of rows in the dataset
    num_rows = data.shape[0]
    print(f"Number of rows in the dataset after preprocessing: {num_rows}")

    # Sample dataset for training
    sample_size = min(2000, num_rows)
    print(f"Sampling {sample_size} rows from the dataset...")
    data_sampled = data.sample(n=sample_size, random_state=42)
    print("Dataset sampled.")

    # Define features and target
    print("Defining features and target...")
    X = data_sampled[['ellis-cpu.system_perc', 'ellis-cpu.wait_perc', 'ellis-load.avg_1_min',
                      'ellis-mem.free_mb', 'ellis-net.in_bytes_sec', 'ellis-net.out_packets_sec']]
    y = data_sampled['Label']
    print("Features and target defined.")

    # Scale the features
    print("Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Feature scaling complete.")

    # Split dataset into training and testing sets
    print("Splitting dataset into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    print("Dataset split complete.")

    # Train Decision Tree model
    print("Training Decision Tree model...")
    start_time = time.time()
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    print(f"Decision Tree model trained successfully in {time.time() - start_time:.2f} seconds.")

    # Calculate accuracy on test set
    print("Calculating accuracy...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')

    # Save the model to disk
    print("Saving the model to disk...")
    joblib.dump(model, 'decision_tree_model.pkl')
    print("Model saved successfully.")

    # Save the scaler to disk
    print("Saving the scaler to disk...")
    joblib.dump(scaler, 'scaler.pkl')
    print("Scaler saved successfully.")

    # Print success message
    print("Decision Tree model trained successfully and saved!")

except Exception as e:
    print(f"Error occurred: {str(e)}")
