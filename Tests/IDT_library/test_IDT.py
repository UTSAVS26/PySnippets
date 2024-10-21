import unittest
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import interactive_decision_tree as idt

class TestDecisionTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the Titanic dataset
        url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
        data = pd.read_csv(url)

        # Preprocess the data
        data = data[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]
        data = data.dropna()
        data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
        cls.X = data[['Pclass', 'Sex', 'Age', 'Fare']]
        cls.y = data['Survived']

        # Split the data into training and testing sets
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(cls.X, cls.y, test_size=0.2, random_state=42)
        cls.model = DecisionTreeClassifier()
        cls.model.fit(cls.X_train, cls.y_train)
        cls.y_pred = cls.model.predict(cls.X_test)

    def test_accuracy(self):
        accuracy = accuracy_score(self.y_test, self.y_pred)
        self.assertGreaterEqual(accuracy, 0.7, "Accuracy should be at least 0.7")

    def test_feature_importance(self):
        feature_importances = self.model.feature_importances_
        self.assertEqual(len(feature_importances), 4, "There should be 4 feature importances")
        self.assertTrue(all(0 <= importance <= 1 for importance in feature_importances), "Feature importances should be between 0 and 1")

    def test_prediction_shape(self):
        self.assertEqual(self.y_pred.shape, self.y_test.shape, "Predicted and test labels should have the same shape")
        
    def test_create_tee(self):
        idt.create_tree(tree_model = self.model, X=self.X_train, target_names=['Survived', 'Died'], target_colors=['red', 'green'],save_path='titanic_tree.html')
        
        
    def test_sankey_tree(self):
        idt.create_sankey(tree_model=self.model,X=self.X_train,target_names=['Not Survived', 'Survived'],target_colors=['red', 'green'],save_path='titanic_sankey.html')
        

if __name__ == '__main__':
    unittest.main()
