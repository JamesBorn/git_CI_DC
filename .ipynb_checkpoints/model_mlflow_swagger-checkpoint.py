import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Log the model to MLflow
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model", registered_model_name="IrisClassifier")
    mlflow.log_metric("accuracy", model.score(X_test, y_test))