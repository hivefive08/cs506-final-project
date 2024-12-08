# cs506-final-project

## **FinaL Report**

### 1. How to Build and Run the Code
- **Clone Repository**
- **Install the required dependencies**: enter "make install" in terminal
- **Accessing Jupyter Notebook**: enter "make notebook" in terminal
- **Run the flask app**: enter "make run" in terminal

### 2. Visualizations
- **Distribution of Review Lengths**: Analyzed to understand the spread and variance in review lengths.
- **Word Clouds**: Created for positive and negative reviews to visualize commonly used words.
- **Bar Charts**: Generated interactive bar charts for the top 20 words in positive and negative reviews, allowing users to view word frequencies.
- **Confusion Matrix**: Used to show the classification results of the model.

### 3. Detailed Description of Data Processing
- **Cleaning**: Removed HTML tags, special characters, and numbers, and converted text to lowercase.
- **Tokenization**: Split the text into individual words for further processing.
- **Stop Words Removal**: Filtered out common words that do not contribute significantly to sentiment analysis.
- **Lemmatization**: Reduced words to their base forms to standardize them.
- **Feature Extraction**: Applied TF-IDF vectorization to transform text data into numerical features.

### 4. Data Modeling Methods
- **Model Used**: Logistic regression was chosen as the primary model.
- **Data Split**: The dataset was split into an 80% training set and a 20% testing set.
- **Training and Evaluation**: The logistic regression model was trained on the TF-IDF matrix and evaluated using accuracy, precision, recall, and F1-score.
- **Deployment**:  The trained model was saved and deployed in a Flask web app for real-time sentiment predictions.

### 4. Preliminary Results
- **Metrics**:
  - **Accuracy**: 0.88
  - **Precision**: 0.88
  - **Recall**: 0.90
  - **F1-score**: 0.89

### 5. Code and Notebooks
- **data_exploration.ipynb**: Contains visualizations and analyses of the data.
- **data_preprocessing.ipynb**: Steps for cleaning and processing the data.
- **model_training.ipynb**: Code for training and evaluating the logistic regression model.
- **app.py**: Code to run website where user can enter their own custom reviews and get result from model
