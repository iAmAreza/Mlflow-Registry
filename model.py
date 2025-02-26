import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set up MLflow experiment with a SQLite backend
# mlflow.set_tracking_uri("sqlite:///mlflow.db")  # Connects to mlflow.db
experiment_name = "IrisModelExperiment"

# Create the experiment if not already existing
mlflow.set_experiment(experiment_name)

# Load dataset and train model
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)

# Register the model with MLflow Model Registry
with mlflow.start_run() as run:
    model.fit(X_train, y_train)
    
    # Log the model to MLflow (Uncomment this line)
    mlflow.sklearn.log_model(model, "model", registered_model_name="IrisModel")
    
    # Log parameters and metrics
    mlflow.log_param("n_estimators", 100)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    mlflow.log_metric("accuracy", accuracy)
    
    print(f"Model registered as 'IrisModel' with accuracy: {accuracy:.4f}")

print(f"Experiment ID: {mlflow.get_experiment_by_name(experiment_name).experiment_id}")
