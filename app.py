from flask import Flask, render_template, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
with open('./data/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('./data/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        user_review = request.form['review']
        review_vectorized = vectorizer.transform([user_review])  # Vectorize the review
        prediction = model.predict(review_vectorized)[0]  # Predict the sentiment
        prediction = 'positive' if prediction == 1 else 'negative'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
