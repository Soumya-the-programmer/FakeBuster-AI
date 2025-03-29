# 🛡️ FakeBuster AI - Fake News Detection Web App

Welcome to **FakeBuster AI**, an advanced **Fake News Detection System** powered by **Ensemble Machine Learning Models**. This project leverages multiple ML algorithms to accurately classify news articles as **Real or Fake**.

---

## 🚀 Project Overview  
**FakeBuster AI** is an **NLP-powered web application** that detects **fake news** using an **ensemble machine learning model**.  
It leverages **SVM, Naïve Bayes, Random Forest, Logistic Regression, and Decision Trees** for accurate predictions.  

🔹 **Tech Stack:** Python, NLP, Machine Learning, Streamlit  
🔹 **Algorithms Used:** SVM, Naïve Bayes, Random Forest, Logistic Regression, Decision Trees  
🔹 **Deployment:** Streamlit 

---

## 📸 Screenshots

### 🔹 Home Page  
![Home Page](https://github.com/user-attachments/assets/66332319-632b-400d-bc4e-f387d57c233e)  

### 🔹 News Analysis Section  
![Analysis Page](https://github.com/user-attachments/assets/dfef5365-ac34-45fc-a3c7-248463572d7c)  

### 🔹 About Section  
![About Page](https://github.com/user-attachments/assets/0dc1707f-532e-42f8-ae32-f998eb295bd0)  

## ✅ Test Cases  
Here are two test cases demonstrating the FakeBuster AI in action.  

### **Test Case 1**  
- **Input:** A piece of real news  
- **Prediction:** ✅ **REAL NEWS**  
![Test Case 1](https://github.com/user-attachments/assets/e1ac64a8-97dd-4654-b62d-25fd9b072a78)  

### **Test Case 2**  
- **Input:** A piece of fake news  
- **Prediction:** ❌ **FAKE NEWS**  
![Test Case 2](https://github.com/user-attachments/assets/9d15b72c-a12c-4c89-b85d-46e9e75f26b7)  

---

## 🚀 Features
- **Multi-Model Approach:** Uses **SVM, Naïve Bayes, Random Forest, Logistic Regression, and Decision Trees** in an ensemble model.
- **Web-Based UI:** Built with **Streamlit** for an interactive experience.
- **Real-Time Prediction:** Paste any news article and get instant results.
- **Custom Vectorization:** Uses **TF-IDF Vectorization** for text processing.
- **User-Friendly Interface:** Professional UI with banner image.
- **Optimized & Deployed:** Fully trained and deployed as a working web application.

---

## 📂 Project Structure

```
📁 FakeBuster_AI/
│-- 📜 Model_Training.ipynb       # Jupyter Notebook for model training & evaluation
│-- 📜 Processed_news.csv         # Preprocessed dataset
│-- 📜 fake_and_real_news.csv     # Original dataset
│-- 📜 app.py                     # Main Streamlit UI application
│-- 📜 fake_news_detect.py        # Helper functions for prediction
│-- 📜 requirements.txt           # Dependencies list
│-- 📜 vector.pkl                 # TF-IDF Vectorization model
│-- 📜 all_ensemble_model         # Final trained ensemble model
│-- 🖼️ fake_news_banner.jpg       # Banner image for the website
```

---

## 📊 Dataset
We used the dataset from **Kaggle**:
[News Detection: Fake or Real](https://www.kaggle.com/datasets/nitishjolly/news-detection-fake-or-real-dataset)

- The dataset contains labeled news articles categorized as **Fake (0) or Real (1)**.
- It was **preprocessed** (stopword removal, lemmatization, vectorization) and saved as `Processed_news.csv`.

---

## ⚙️ Model Training
The **Model_Training.ipynb** notebook includes:
- **Data Preprocessing** (Cleaning, Tokenization, Stopword Removal, Lemmatization)
- **Vectorization** using **TF-IDF**
- Training **Multiple ML Models**:
  - 🏆 **Support Vector Machine (SVM)**
  - 📊 **Naïve Bayes**
  - 🌲 **Random Forest**
  - 📈 **Logistic Regression**
  - 🌿 **Decision Trees**
- **Ensemble Learning**: Combining all models to improve accuracy.
- **Model Evaluation**: Analyzing Accuracy, Precision, Recall, and Confusion Matrix.

Final model is stored as `all_ensemble_model` and vectorizer as `vector.pkl`.

---

## 🖥️ Web Application
The **Streamlit-based Web App** allows users to:
1️⃣ **Enter a news article**
2️⃣ **Process and analyze it**
3️⃣ **Get a prediction (Fake or Real)** instantly!

**Run the app locally:**
```bash
streamlit run app.py
```

---

## 🛠 Installation
To set up the project locally, follow these steps:

1️⃣ Clone this repository:
```bash
git clone https://github.com/Soumya-the-programmer/FakeBuster_AI.git
cd FakeBuster_AI
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Run the web app:
```bash
streamlit run app.py
```

---

## 🎯 Future Improvements
- **Integrate Deep Learning (LSTMs, BERT, or Transformers)** for better accuracy.
- **Expand the dataset** for a more generalized model.
- **Enhance UI/UX** for a better user experience.
- **Deploy on Cloud (AWS/GCP/Heroku)** for global accessibility.

---

## 📜 License
This project is **Open-Source** under the **MIT License**.

🌟 If you found this useful, **give it a ⭐ star!**

---

💡 Developed by **Soumyajeet Das** 🚀

