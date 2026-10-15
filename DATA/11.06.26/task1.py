import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

credit_data = pd.read_csv('credit_data.csv')

le = LabelEncoder()
credit_data['Gender'] = le.fit_transform(credit_data['Gender'])

X = credit_data.drop(['ID', 'Credit_Score'], axis=1)
y = credit_data['Credit_Score']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Точність моделі:", accuracy_score(y_test, y_pred))