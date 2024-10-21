# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = pd.read_csv(url)

# Preprocess the data
data = data[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]
data = data.dropna()
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
X = data[['Pclass', 'Sex', 'Age', 'Fare']]
y = data['Survived']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X.columns, class_names=['Not Survived', 'Survived'], filled=True)
plt.show()


import interactive_decision_tree as idt  # noqa: E402
idt.create_tree(tree_model=model,
                X=X_train,
                target_names=['Not Survived', 'Survived'],
                target_colors=['red', 'green'],
                save_path='titanic-tree.html')

idt.create_sankey(tree_model=model,
                X=X_train,
                target_names=['Not Survived', 'Survived'],
                target_colors=['red', 'green'],
                save_path='titanic-sankey.html')


