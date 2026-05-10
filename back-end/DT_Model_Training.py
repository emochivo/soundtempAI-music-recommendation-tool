import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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
dt_model = DecisionTreeClassifier(max_depth=7, random_state=42)

#building the pipeline (preprocessing and decision tree model)
pipeline = Pipeline([
    ("preprocessor", weather_encoded),
    ("classifer", dt_model)
])
#training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#training model
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
score = accuracy_score(y_test, y_pred)
#91% accuracy score
print("Model Accuracy:", score)

#saving the model
joblib.dump(pipeline, 'dt_pipeline.pkl')