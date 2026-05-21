# Study Hours vs Marks Prediction using Linear Regression

A beginner-friendly Machine Learning project that predicts student marks based on study hours using Linear Regression.

---

# 📌 Project Overview

This project demonstrates how Linear Regression works using a synthetic dataset of:

| Study Hours | Marks Scored |
|-------------|--------------|
| 1 | 35 |
| 2 | 40 |
| 3 | 50 |
| 4 | 55 |
| 5 | 60 |
| 6 | 68 |
| 7 | 72 |
| 8 | 80 |
| 9 | 88 |
| 10 | 95 |

The model learns the relationship between:

> More study hours → Higher marks

and predicts marks for new study hours.

---

# ✨ Features

- ✅ Synthetic dataset generation
- ✅ CSV dataset loading using Pandas
- ✅ Linear Regression model training
- ✅ Weight and Bias calculation
- ✅ Regression graph visualization
- ✅ Model saving using Pickle (`.pkl`)
- ✅ Prediction using saved model

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Joblib

---

# 📈 Linear Regression Equation

The model uses:

\[
y = wx + b
\]

Where:

- `x` = study hours
- `y` = predicted marks
- `w` = weight/slope
- `b` = bias/intercept

Learned equation:

\[
y = 6.58x + 28.11
\]

---

# 🚀 Installation

Clone the repository:

```bash
git clone git@github-personal:vishwa-vv11/Linear_Regression.git
```

Move into project directory:

```bash
cd Linear_Regression
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧠 Train the Model

Run:

```bash
python train.py
```

This will:

- Load dataset
- Train model
- Display regression graph
- Save trained model

---

# 🔮 Predict Using Saved Model

Run:

```bash
python predict.py
```

Example prediction:

```text
Predicted Marks: 107.07
```

---

# 📊 Visualization

The regression line shows the relationship between:

- Study hours
- Marks scored

---

# 💾 Model Saving

The trained model is saved as:

```text
linear_regression_model.pkl
```

This allows prediction without retraining.

---

# 📁 Project Structure

```text
Linear_Regression/
│
├── dataset.csv
├── train.py
├── predict.py
├── linear_regression_model.pkl
├── requirements.txt
└── README.md
```

---

# 👨‍💻 Author

Vishwa