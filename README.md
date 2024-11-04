# cs506-final-project

# 1. Description of the Project
This project aims to build a sentiment analysis model that classifies movie reviews as positive or negative based on their textual content.
# 2. Clear Goal
Successfully predict the sentiment (positive/negative) of movie reviews using natural language processing (NLP) techniques.
# 3. Data Collection
Use a publicly available dataset, such as the IMDb movie review dataset, which contains labeled reviews.
The dataset can be sourced from websites like Kaggle or directly from IMDb.
# 4. Modeling Plan
Use basic natural language processing techniques, such as tokenization, removing stop words, and feature extraction.
Implement a simple logistic regression or decision tree classifier for sentiment prediction.
# 5. Data Visualization
Word clouds to show common words in positive versus negative reviews.
Bar charts to visualize the distribution of review lengths or sentiment categories in the dataset.
Confusion matrix to visualize model performance.
# 6. Test Plan
Split the data into training (80%) and testing (20%) sets.
Train the model on the training set and evaluate its performance on the testing set using accuracy and F1-score as metrics.

---

1. The data will be sourced from a publicly available dataset such as the IMDb movie review dataset on Kaggle. The dataset consists of textual movie reviews along with labels indicating whether the review is positive or negative. The primary feature is the review text, which is categorical data in the form of strings.

2. The data will require preprocessing steps including tokenization, filtering out common words, and handling negations. Then we will need to convert the text into numerical features so that we can then train on those data.

3. The model's performance will be measured using accuracy, precision, recall, and F1-score. We will use a simple logistic regression model as a baseline and aim to surpass an F1-score of 80% on the test set.

---

## **Midterm Report**
https://youtu.be/m4rvpP1I6Lk

### 1. Preliminary Visualizations
- **Distribution of Review Lengths**: Analyzed to understand the spread and variance in review lengths.
- **Word Clouds**: Created for positive and negative reviews to visualize commonly used words.
- **Confusion Matrix**: Used to show the classification results of the model.

### 2. Detailed Description of Data Processing
- **Cleaning**: Removed HTML tags, special characters, and numbers, and converted text to lowercase.
- **Tokenization**: Split the text into individual words for further processing.
- **Stop Words Removal**: Filtered out common words that do not contribute significantly to sentiment analysis.
- **Lemmatization**: Reduced words to their base forms to standardize them.
- **Feature Extraction**: Applied TF-IDF vectorization to transform text data into numerical features.

### 3. Data Modeling Methods
- **Model Used**: Logistic regression was chosen for the baseline model.
- **Data Split**: The dataset was split into an 80% training set and a 20% testing set.
- **Training and Evaluation**: The logistic regression model was trained on the TF-IDF matrix and evaluated using accuracy, precision, recall, and F1-score.

### 4. Preliminary Results
- **Metrics**:
  - **Accuracy**: 0.88
  - **Precision**: 0.88
  - **Recall**: 0.90
  - **F1-score**: 0.89
- **Confusion Matrix**:

### 5. Code and Notebooks
- **data_preprocessing.ipynb**: Steps for cleaning and processing the data.
- **model_training.ipynb**: Code for training and evaluating the logistic regression model.
- **visualizations.ipynb**: Contains visualizations and analyses of the data.

