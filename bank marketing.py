import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import export_text
url = r"C:\Users\karan\Documents\Python Scripts\bank.csv"  
df = pd.read_csv(url, sep=';')
df = df.dropna()
selected_features = ['age', 'job', 'education', 'marital', 'default', 'housing', 'loan', 'campaign', 'pdays', 'previous', 'poutcome', 'y']
df = df[selected_features]
df = pd.get_dummies(df, drop_first=True)
X = df.drop('y_yes', axis=1)
y = df['y_yes']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
tree_rules = export_text(clf, feature_names=list(X.columns))
print("Decision Tree Rules:")
print(tree_rules)


