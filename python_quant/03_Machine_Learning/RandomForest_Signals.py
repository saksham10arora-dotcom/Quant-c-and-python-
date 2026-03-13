"""
Topic: Random Forest Classifier for Signal Generation
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_rf_signal_model(features: pd.DataFrame, target: pd.Series):
    """Trains a Random Forest to predict price direction (+1 or -1)."""
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=False)
    
    clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    clf.fit(X_train, y_train)
    
    preds = clf.predict(X_test)
    print(classification_report(y_test, preds))
    
    feature_importance = pd.Series(clf.feature_importances_, index=features.columns)
    print("\nFeature Importances:")
    print(feature_importance.sort_values(ascending=False).head(3))
    
    return clf

if __name__ == "__main__":
    n = 1000
    X = pd.DataFrame({
        'RSI': np.random.uniform(20, 80, n),
        'MACD': np.random.uniform(-2, 2, n),
        'Vol': np.random.uniform(0.1, 0.5, n)
    })
    # Synthetic target logic
    y = pd.Series(np.where(X['RSI'] < 40, 1, np.where(X['RSI'] > 60, -1, 0)))
    
    train_rf_signal_model(X, y)





















