# 💻 Laptop Price Prediction

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen?style=for-the-badge&logo=streamlit)](https://laptop-price-prediction-m0tw.onrender.com/)  
A Machine Learning powered web app that predicts the price of laptops based on their specifications.  

---

## 🚀 Overview
The **Laptop Price Prediction App** uses real-world laptop specifications (CPU, GPU, RAM, storage, display, etc.) to predict the approximate market price.  
It is built with **Python, Scikit-Learn, and Streamlit** and deployed on **Render**.  

The project demonstrates:
- End-to-end **ML pipeline** (data preprocessing → feature engineering → model training → hyperparameter tuning → evaluation).
- Use of different ML algorithms (**Linear Regression, Ridge, Lasso, KNN, Decision Tree, Random Forest**) with **GridSearchCV** for hyperparameter tuning.
- Deployment of a trained model as an **interactive web app**.

---

## 📊 Dataset
The dataset was collected from **Kaggle** and contains laptop details such as:
- Brand
- CPU (extracted into generation & clock speed)
- GPU
- RAM
- Storage (HDD, SSD)
- Display size & resolution (PPI calculated)
- Weight
- Operating System
- Target variable → **Price (in INR)**

---

## ⚙️ Features
✔️ Data preprocessing with **pandas & scikit-learn**  
✔️ Feature engineering (e.g., extracting CPU generation, calculating PPI)  
✔️ Handling missing values with imputation  
✔️ Encoding categorical variables using **ColumnTransformer & OneHotEncoder**  
✔️ Hyperparameter tuning with **GridSearchCV**  
✔️ Comparison of multiple ML models  
✔️ Deployment with **Streamlit**  

---

## 🛠️ Tech Stack
- **Python** 🐍
- **pandas**, **numpy**, **scikit-learn** → Data preprocessing & ML
- **matplotlib**, **seaborn** → Data visualization
- **Streamlit** → Web app interface
- **Render** → Cloud deployment

---

## 📂 Project Structure
```

├── app.py                 # Streamlit web app
├── Laptop\_price.csv       # Dataset
├── requirements.txt       # Dependencies
├── model.pkl              # Trained ML model
├── .streamlit/config.toml # Streamlit configuration (for deployment)
├── README.md              # Project documentation
└── notebooks/             # Jupyter notebooks (EDA, model training)

````

---

## 🌐 Live Demo
🔗 **Try the app here** → [Laptop Price Predictor](https://laptop-price-prediction-m0tw.onrender.com/)  

Steps to use:
1. Select laptop specifications (brand, CPU, RAM, storage, etc.)
2. Click **Predict Price**
3. Get an estimated price instantly 🎯

---

## 📈 Model Training & Results
The following models were tested:
- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **K-Nearest Neighbors**
- **Decision Tree Regressor**
- **Random Forest Regressor**

📌 **Random Forest performed the best** after hyperparameter tuning.

Evaluation metrics:
- **R² Score**
- **Mean Absolute Error (MAE)**

---

## ⚡ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/arif124713/Laptop-Price-Prediction.git
cd Laptop-Price-Prediction
````

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app locally

```bash
streamlit run app.py
```



## 🔮 Future Improvements

* Add support for **deep learning regression models**
* Integrate **real-time price scraping** from e-commerce sites
* Optimize model using **XGBoost/LightGBM**
* Improve UI with more interactive elements

---

## 👨‍💻 Author

**Arif Hussain**

* 🌐 [LinkedIn](https://www.linkedin.com/in/arif124713)
* 💻 [GitHub](https://github.com/arif124713)
* 🚀 Aspiring ML Engineer | Founder of *Zero Sense*

---

## ⭐ Contribute

Contributions are welcome!
Fork this repo → Create a new branch → Make changes → Submit a PR.

If you found this project helpful, **please star ⭐ the repo**.

```
