from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


app = Flask(__name__)

df = pd.read_csv('heart.csv')


selected_features = ['age', 'cp', 'trestbps', 'chol','thalach']
X = df[selected_features]

y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)


y_pred = rf_clf.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy on Test Data: ", accuracy*100)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", classification_rep)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    age = float(request.form['age'])
    chest_pain_type = float(request.form['cp'])
    resting_Blood_pressure = float(request.form['trestbps'])
    cholesterol_level= float(request.form['chol'])
    maximum_heart_rate_achieved= float(request.form['thalach'])
    


    input_data = [[age,chest_pain_type , resting_Blood_pressure,cholesterol_level,maximum_heart_rate_achieved]]

    
    prediction = rf_clf.predict(input_data)
    prediction_proba = rf_clf.predict_proba(input_data)

    
    predicted_class = prediction[0]
    predicted_prob = prediction_proba[0]

    
    result = {
        'predicted_class': predicted_class,
        'predicted_probability': dict(zip(rf_clf.classes_, predicted_prob))
    }
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)




