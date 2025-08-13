# Protein Structure Prediction

This project predicts the **secondary structure** of proteins (Helix, Sheet, or Coil) from their amino acid sequences using a **Support Vector Machine (SVM)** model.

## 📌 Features
- Train a model on protein sequence datasets.
- Predict secondary structures for new protein sequences.
- Simple web interface built using Flask.
- Pre-trained model (`svm_model.pkl`) for quick predictions.

## 📂 Project Structure
<details>
<summary>Click to view</summary>

ProteinStruturePrediction/
│
├── app.py # Flask app for web interface
├── Data_RS126.txt # Dataset of protein sequences
├── protein (1).ipynb # Model training and analysis
├── svm_model.pkl # Trained SVM model
├── templates/
│ └── index.html # Front-end HTML template
└── ProteinStruturePrediction.code-workspace

bash
Copy
Edit

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mansi12bendale/ProteinStructurePrediction.git
cd ProteinStructurePrediction
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is missing, manually install:)

bash
Copy
Edit
pip install flask scikit-learn pandas numpy
3️⃣ Run the application
bash
Copy
Edit
python app.py
Then open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
🧠 Model Details
Algorithm: Support Vector Machine (SVM)

Dataset: RS126 dataset (Data_RS126.txt)

Output: Predicted secondary structure (Helix, Sheet, Coil)

📜 License
This project is open-source and available under the MIT License.

sql
Copy
Edit

Once saved, run:  
```bash
git add README.md
git commit -m "Add README"
git push
