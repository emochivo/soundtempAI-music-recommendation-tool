import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, classification_report
from sklearn.model_selection import GridSearchCV
import joblib


#defining dataset - synthetic 
#features - weather, weather_desc, temperature
#target - mood

syn_data = pd.read_csv("back-end/weather_mood_us_500.csv")

#features 
X = syn_data[["weather", "weather_desc", "temperature"]]

#target variable - mood
y = syn_data["mood"]

#Data Preprocessing - One hot Encoding
weather_encoded = ColumnTransformer([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ["weather", "weather_desc"])], remainder="passthrough", verbose_feature_names_out=False)
weather_encoded.set_output(transform="pandas")
encoded_data = weather_encoded.fit_transform(X)
# print(encoded_data)


#Decision Tree Model
# dt_model = DecisionTreeClassifier(max_depth=7, random_state=42)
dt_model = DecisionTreeClassifier(random_state=42)

#building the pipeline (preprocessing and decision tree model)
pipeline = Pipeline([
    ("preprocessor", weather_encoded),
    ("classifier", dt_model)
])


#training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#TUNING Hyperparameters
param = {
    "classifier__criterion": ["gini", "entropy"],
    "classifier__max_depth": [3, 5, 7, 10],
    "classifier__min_samples_leaf": [1, 5, 10]
}

scoring = {
    "accuracy": "accuracy",
    "precision_weighted": "precision_weighted",
    "recall_weighted": "recall_weighted",
    "f1_weighted": "f1_weighted"
}

grid = GridSearchCV(
    pipeline,
    param,
    cv=5,
    scoring=scoring,
    refit="f1_weighted"
)

grid.fit(X_train, y_train)

print(f"Best Parameters: {grid.best_params_}")
print(f"Best Score: {grid.best_score_}")
#best model
best_model = grid.best_estimator_

#training model
best_model.fit(X_train, y_train)

y_pred = best_model.predict(X_test)
score = accuracy_score(y_test, y_pred)

print("Model Accuracy:", score)

matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:", matrix)

prec_score = precision_score(y_test, y_pred, average="weighted")
print("Precision Score:", prec_score)
re_score = recall_score(y_test, y_pred, average="weighted")
print("Recall Score:", re_score)

class_report = classification_report(y_test, y_pred)
print("Classification Report:", class_report)

#saving the model
joblib.dump(best_model, 'dt_pipeline.pkl')

#training model
# pipeline.fit(X_train, y_train)

# y_pred = pipeline.predict(X_test)
# score = accuracy_score(y_test, y_pred)
# #91% accuracy score
# print("Model Accuracy:", score)

# matrix = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:", matrix)

# prec_score = precision_score(y_test, y_pred)
# print("Precision Score:", prec_score)
# re_score = recall_score(y_test, y_pred)
# print("Recall Score:", re_score)

# class_report = classification_report(y_test, y_pred)
# print("Classification Report:", class_report)

# #saving the model
# joblib.dump(pipeline, 'dt_pipeline.pkl')