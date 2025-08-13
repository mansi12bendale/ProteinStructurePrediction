import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define mappings for amino acids and secondary structure labels
aa_to_int = {aa: i + 1 for i, aa in enumerate("ACDEFGHIKLMNPQRSTVWY")}
label_map = {'C': 0, 'E': 1, 'H': 2}

# Load the dataset
with open('Data_RS126.txt', 'r') as file:
    primary_structures = []
    secondary_structures = []

    for count, line in enumerate(file, start=1):
        if count % 2 == 0:
            secondary_structures.append(line.strip())
        else:
            primary_structures.append(line.strip())

# Preprocess the data
def preprocess_data(primary_structures, secondary_structures):
    X_data = []
    y_data = []
    for i in range(len(primary_structures)):
        primary_seq = primary_structures[i]
        secondary_seq = secondary_structures[i]

        # Handle mismatched lengths
        if len(primary_seq) != len(secondary_seq):
            print(f"Warning: Length mismatch at index {i}. Truncating to shortest length.")
            min_len = min(len(primary_seq), len(secondary_seq))
            primary_seq = primary_seq[:min_len]
            secondary_seq = secondary_seq[:min_len]

        # Convert primary sequence to integers
        X_seq = [aa_to_int.get(aa, 0) for aa in primary_seq]
        # Convert secondary sequence to labels
        y_seq = [label_map[char] for char in secondary_seq]

        X_data.append(X_seq)
        y_data.append(y_seq)

    # Padding or truncating sequences to a fixed length
    max_length = 300
    X_data = [seq[:max_length] + [0] * (max_length - len(seq)) for seq in X_data]
    y_data = [seq[:max_length] + [0] * (max_length - len(seq)) for seq in y_data]

    return np.array(X_data), np.array(y_data)

# Prepare the data
X, y = preprocess_data(primary_structures, secondary_structures)

# Flatten y to create a single target vector
y = y.flatten()

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the SVM model
svc = SVC()
svc.fit(X_train, y_train)

# Predict and evaluate
y_pred = svc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")



