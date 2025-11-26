# 02_ray_tune_hypersearch.py
from ray import tune
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=10000, n_features=20, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

def objective(config):
    model = RandomForestClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"]
    )
    model.fit(X_train, y_train)
    score = model.score(X_val, y_val)
    tune.report(score=score)

analysis = tune.run(
    objective,
    config={
        "n_estimators": tune.choice([100, 200, 400, 800]),
        "max_depth": tune.choice([10, 20, 30, None])
    },
    num_samples=24,
    resources_per_trial={"cpu": 2}
)

print("Best config :", analysis.best_config)
print("Best accuracy :", analysis.best_result["score"])