# 🏁 Motocross Engine Class Prediction

## 📌 Project Overview

Motocross Engine Class Prediction is a Machine Learning project that predicts the engine capacity category of a motocross bike based on its model name.

The project uses Natural Language Processing (NLP) techniques and a Random Forest Classifier to classify bike models into three engine capacity categories: **125cc, 250cc, and 450cc**.

A simple and interactive web application is developed using Streamlit, allowing users to enter a bike model and view the predicted engine class.

## 🎯 Project Objectives

- Predict the engine capacity category of motocross bikes.
- Apply Machine Learning techniques to bike model data.
- Explore text processing using TF-IDF.
- Build an interactive prediction application.
- Demonstrate the use of Python and Scikit-learn in a real-world project.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Development Platform:** Google Colab, VS Code
- **Libraries:** Pandas, NumPy, Scikit-learn, Joblib
- **Machine Learning Algorithm:** Random Forest Classifier
- **Text Processing:** TF-IDF Vectorizer
- **Web Framework:** Streamlit
- **Version Control:** Git and GitHub

## 📊 Dataset

**Dataset Name:** American Motocross Race Results

**Source:** [Hugging Face – American Motocross Results](https://huggingface.co/datasets/mickey45/americanmotocrossresults)

The dataset contains motocross race information, including:

- Bike model
- Rider name
- Race year
- Race location
- Competition class
- Race position

The bike model information is used in the current prototype to derive engine capacity labels.

## 🤖 Machine Learning Workflow

1. Load the motocross dataset.
2. Explore and understand the data.
3. Clean missing and unnecessary values.
4. Extract engine capacity categories from bike model names.
5. Convert text into numerical features using TF-IDF.
6. Train a Random Forest Classifier.
7. Evaluate the model using classification metrics.
8. Save the trained model using Joblib.
9. Integrate the model with Streamlit.

## 🏍️ Supported Engine Classes

| Engine Class | Capacity |
|---|---|
| 125cc | 125 cubic centimetres |
| 250cc | 250 cubic centimetres |
| 450cc | 450 cubic centimetres |

**Note:** The current prototype supports three classes. The planned 50cc, 65cc and 85cc categories are future enhancements.

## 📂 Project Structure

```text
Motocross_Race_Class_Prediction/
│
├── app.py
├── motocross_model.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Motocross_Race_Class_Prediction
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### Step 5: Make a Prediction

1. Open the application in your browser.
2. Enter a motocross bike model name.
3. Click **Predict Engine Class**.
4. View the predicted engine capacity category.

## 🧪 Example Prediction

**Input:**
```text
Honda CRF250R
```

**Output:**
```text
Predicted Engine Class: 250cc
```

## 📈 Model Evaluation

The initial experiment reported 100% test accuracy.

**Important limitation:** The target labels were extracted directly from the bike model names, and those same names were used as model inputs. Therefore, this result involves target leakage and does not demonstrate independent real-world prediction accuracy. A more reliable evaluation requires verified manufacturer specifications and testing on bike models not seen during training.

## 🔮 Future Enhancements

- Add 50cc, 65cc and 85cc engine categories.
- Include more motocross bike models and manufacturers.
- Use verified engine specifications.
- Improve model generalization and evaluation.
- Add more bike information such as manufacturer and model year.
- Deploy the application online.

## 👩‍💻 Project Information

**Project Title:** Motocross Engine Class Prediction  
**Domain:** Machine Learning and Artificial Intelligence  
**Application:** Streamlit Web Application

---

⭐ If you find this project interesting, consider giving this repository a star!

**Thank you for visiting this project!** 🏁
