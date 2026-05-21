# 📘 Study Hours vs Marks Prediction using Linear Regression

A beginner-friendly Machine Learning project that predicts student marks based on study hours using **Linear Regression**.

This repository focuses on understanding:
- Machine Learning basics
- Supervised Learning
- Linear Regression
- Mathematical foundation behind predictions
- Model training and saving

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
- ✅ Beginner-friendly mathematical explanation
- ✅ Handwritten learning notes included

---

# 🧠 Machine Learning Concept

Machine Learning is mainly divided into:

- Supervised Learning
- Unsupervised Learning

This project uses:

## Supervised Learning

Where:
- Input data contains labels
- Model learns from known outputs

Example:
- Study Hours → Input
- Marks → Output

---

# 📈 Linear Regression

Linear Regression is a supervised learning algorithm used to model the relationship between:

- One dependent variable
- One or more independent variables

In this project:

- Independent Variable → Study Hours
- Dependent Variable → Marks Scored

It predicts continuous values by fitting a straight line that best represents the data.

---

# 📐 Linear Regression Formula

The model uses:

\[
y = wx + b
\]

Where:

- `x` → input feature
- `y` → predicted output
- `w` → weight/slope
- `b` → bias/intercept

Learned equation from the dataset:

\[
y = 6.58x + 28.11
\]

---

# 📚 Mathematical Foundation & Notes

The `images/` folder contains handwritten notes and visual explanations covering:

- Supervised Learning basics
- Linear Regression intuition
- Dependent vs Independent variables
- Regression line understanding
- Formula derivation
- Weight calculation
- Bias calculation
- Dataset tabulation
- Step-by-step mathematical substitution

These notes are included for beginners who want to understand the mathematics behind Linear Regression instead of only using libraries.

---

# 📂 Additional Learning Dataset

An additional synthetic dataset:

```text
house_price_sqft_dataset.csv
```

is also included for learners who want to further experiment with Linear Regression concepts using house price prediction.

This dataset is provided for educational exploration purposes.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Pickle / Joblib

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

# 🧪 Train the Model

Run:

```bash
python main.py
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
python Predict.py
```

Example prediction:

```text
Predicted Marks: 107.07
```

---

# 📊 Visualization

The regression line visually represents the relationship between:

- Study Hours
- Marks Scored

showing how predictions are made using a best-fit straight line.

---

# 💾 Model Saving

The trained model is saved as:

```text
marks_prediction.pkl
```

This allows predictions without retraining the model every time.

---

# 📁 Project Structure

```text
Linear_Regression/
│
├── images/
│   ├── handwritten_notes
│   ├── mathematical_explanations
│   └── regression_visuals
│
├── Predict.py
├── main.py
├── marks dataset.csv
├── house_price_sqft_dataset.csv
├── marks_prediction.pkl
├── requirements.txt
└── README.md
```

---

# 👨‍💻 Author

Vishwa

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.