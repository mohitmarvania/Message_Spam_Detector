"""
This is the main and only file which should be executed.
"""
from flask import Flask, render_template, request
import random
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from PIL import Image
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article

# ------------------------ EMAIL SPAM (Start) ------------------------
ps = PorterStemmer()
nltk.download('punkt')
non_spam_email_text = [
    'Great news! This message is NOT SPAM.',
    'Phew! You can relax, this message is LEGITIMATE. ✅',
    'Looks good! This message is SAFE to open.',
    'All clear! NO SPAM detected in this message. 🟢',
    'This message is NOT SPAM',
    'We got your back! This email is SAFE.',
]
spam_email_text = [
    'Alert! This message is a SPAM.',
    'Heads up! ⚠️ This message might be SPAM. Suspicious activity detected.',
    'Uh oh! This message looks like SPAM. Be careful!',
    "❌ This message is SPAM. Don't click on any links if any!",
    'Phishing alert! This message is trying to STEAL your information.',
    'High SPAM risk! Delete this email immediately.'
]
tfidf = pickle.load(open('models/email_spam/vectorizer.pkl', 'rb'))
model = pickle.load(open('models/email_spam/model.pkl', 'rb'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Removing special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    # Removing stop words and punctuations
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    # stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# ------------------------ EMAIL SPAM (End) ------------------------

# Creating flask application named "app".
app = Flask(__name__)


# Creating routes for the application.
@app.route("/")
@app.route("/email", methods=["GET", "POST"])
def email():
    if request.method == "POST":
        email_content = request.form.get("message-content")

        if email_content == "":
            prediction_result = "Please enter the message!"
            return render_template("email.html", prediction=prediction_result)
        # For demonstration purposes, let's just print the message_content
        # print("Message entered:", email_content)

        # 1. preprocess
        transformed_text = transform_text(email_content)

        # 2. vectorize
        vector_input = tfidf.transform([transformed_text])

        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Display

        if result == 1:
            random_number = random.randint(0, 5)
            prediction_result = spam_email_text[random_number]
        elif result == 0:
            random_number = random.randint(0, 5)
            prediction_result = non_spam_email_text[random_number]
        else:
            prediction_result = "Cannot understand the message, Please try again!"

        # Render the updated HTML with the prediction result
        return render_template("email.html", prediction=prediction_result)

    # If it's a GET request or after processing the POST request (to render the form)
    return render_template("email.html")


@app.route('/info')
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)
