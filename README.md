# 🛡️ FakeBuster AI - Fake News Detection Web App

Welcome to **FakeBuster AI**, an advanced **Fake News Detection System** powered by **Ensemble Machine Learning Models**. This project leverages multiple ML algorithms to accurately classify news articles as **Real or Fake**.

---

## 📸 Screenshots

---

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
│-- 📜 fake_and_real_news.csv     # Dataset after processing
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
- It was **preprocessed** (stopword removal, lemmatization, vectorization) and saved as `fake_and_real_news.csv`.

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

