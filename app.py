from flask import Flask, render_template, request,send_file
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load model
model_path = os.path.join('model', 'fraud_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load dataset
df = pd.read_csv('ecommercehub_dataset.csv')

# Routes
@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/project')
def project():
    return render_template('index.html', prediction=None)

@app.route('/project_report')
def project_report():
    return render_template('project_report.html')

@app.route('/data')
def data():
    df = pd.read_csv("dataset/ecommercehub_dataset.csv")
    dataset_html = df.head(10).to_html(classes='dataset-table', index=False)
    return render_template('dataset.html', dataset_html=dataset_html)

@app.route('/report')
def report():
    return send_file("static/resume.pdf")

@app.route('/back')
def back():
    return render_template("backend.html")

@app.route('/intro')
def intro():
    return render_template("intro.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        amt = float(request.form['transaction_amount'])
        category = request.form['product_category']
        method = request.form['payment_method']
        customer_id = int(request.form['customer_id'])
        hour = int(request.form['hour'])

        input_df = pd.DataFrame([{
            'Transaction Amount': amt,
            'Product Category': category,
            'Payment Method': method,
            'Customer ID': customer_id,
            'Hour': hour
        }])

        prediction = model.predict(input_df)[0]
        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return render_template('index.html', prediction_error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
