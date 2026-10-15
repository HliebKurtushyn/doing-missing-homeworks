import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV,
)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from skopt import BayesSearchCV
from skopt.space import Integer, Categorical


# Завантаження даних
df = pd.read_csv("housing-prices-dataset.csv")

X = df.drop("price", axis=1)
y = (df["price"] > df["price"].median()).astype(int)

numeric_features = X.select_dtypes(include="number").columns
categorical_features = X.select_dtypes(exclude="number").columns

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)


# ==========================================
# Завдання 1: SVM + Grid Search
# ==========================================

svm_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", SVC(kernel="rbf")),
])

svm_params = {
    "model__C": [0.1, 1, 10, 100],
    "model__gamma": [1, 0.1, 0.01, 0.001],
}

svm_search = GridSearchCV(
    svm_pipeline, svm_params, cv=5, scoring="accuracy", n_jobs=-1
)

svm_search.fit(X_train, y_train)
svm_pred = svm_search.predict(X_test)

print("=== SVM ===")
print("Найкращі параметри:", svm_search.best_params_)
print("Точність:", accuracy_score(y_test, svm_pred))
print(classification_report(y_test, svm_pred))

sns.heatmap(
    confusion_matrix(y_test, svm_pred),
    annot=True,
    fmt="d",
    cmap="Blues",
)
plt.title("SVM Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()


# ==========================================
# Завдання 2: Random Forest optimization
# ==========================================

rf_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(random_state=42)),
])

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 10, 20],
    "model__min_samples_split": [2, 5],
    "model__min_samples_leaf": [1, 2],
}

param_distributions = {
    "model__n_estimators": [100, 200, 300, 400],
    "model__max_depth": [None, 10, 20, 30],
    "model__min_samples_split": [2, 5, 10],
    "model__min_samples_leaf": [1, 2, 4],
}

bayes_space = {
    "model__n_estimators": Integer(100, 400),
    "model__max_depth": Categorical([None, 10, 20, 30]),
    "model__min_samples_split": Integer(2, 10),
    "model__min_samples_leaf": Integer(1, 4),
}

searches = {
    "Grid Search": GridSearchCV(
        rf_pipeline,
        param_grid,
        cv=5,
        scoring="accuracy",
        n_jobs=-1,
    ),
    "Random Search": RandomizedSearchCV(
        rf_pipeline,
        param_distributions,
        n_iter=20,
        cv=5,
        scoring="accuracy",
        random_state=42,
        n_jobs=-1,
    ),
    "Bayesian Optimization": BayesSearchCV(
        rf_pipeline,
        bayes_space,
        n_iter=20,
        cv=5,
        scoring="accuracy",
        random_state=42,
        n_jobs=-1,
    ),
}

results = []

for name, search in searches.items():
    start = time.perf_counter()
    search.fit(X_train, y_train)
    elapsed = time.perf_counter() - start

    predictions = search.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    results.append({
        "Method": name,
        "Best Parameters": search.best_params_,
        "Accuracy": accuracy,
        "Time (seconds)": round(elapsed, 2),
    })

    print(f"\n=== {name} ===")
    print("Найкращі параметри:", search.best_params_)
    print(f"Точність: {accuracy:.4f}")
    print(f"Час виконання: {elapsed:.2f} секунд")

results_df = pd.DataFrame(results)

print("\n=== Порівняння методів ===")
print(results_df[["Method", "Accuracy", "Time (seconds)"]].to_string(index=False))

print("\nНайвища точність:")
print(results_df.loc[results_df["Accuracy"].idxmax(), ["Method", "Accuracy"]])

print("\nНайшвидший метод:")
print(results_df.loc[results_df["Time (seconds)"].idxmin(), ["Method", "Time (seconds)"]])
