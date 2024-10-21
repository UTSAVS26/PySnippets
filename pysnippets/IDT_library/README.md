📚🔍🎨 **Decision Tree Visualizer**

**Introduction**
The Decision Tree Visualizer is a powerful library that allows you to visualize sklearn Decision Tree Classifiers with ease. It provides functions for extracting useful information about the tree structure and rules, and generates HTML files for visualizing the decision tree.

📊 **Features**
- 🌳 Visualize sklearn Decision Tree Classifiers using HTML templates
- 🔍 Extract useful information about the tree structure and rules
- 📊 Generate output HTML files for visualization
- 🎨 Customize target names and colors for better visualization

🔧 **Installation**
To use the Decision Tree Visualizer, you can simply install it using pip:

```
pip install decision-tree-visualizer
```

📖 **Usage**
To get started, import the library and create an instance of the DecisionTreeVisualizer class:

```python
from decision_tree_visualizer import DecisionTreeVisualizer

# Create an instance of the DecisionTreeVisualizer
visualizer = DecisionTreeVisualizer()
```

Next, fit a sklearn Decision Tree Classifier on your dataset and pass it to the `visualize` method:

```python
# Fit a Decision Tree Classifier on your dataset
tree_model = DecisionTreeClassifier()
tree_model.fit(X, y)

# Visualize the decision tree
visualizer.visualize(tree_model)
```

You can also customize the target names and colors for better visualization:

```python
# Define target names and colors
target_names = ['apple', 'banana', 'orange']
target_colors = ['red', 'yellow', 'orange']

# Visualize the decision tree with custom target names and colors
visualizer.visualize(tree_model, target_names=target_names, target_colors=target_colors)
```

📚 **Documentation**
For detailed documentation and examples, please refer to the [Decision Tree Visualizer Documentation](https://example.com/documentation).

📄 **License**
This library is licensed under the [MIT License](https://example.com/license).

🙌 **Contributing**
Contributions are welcome! Please read the [Contribution Guidelines](https://example.com/contributing) before submitting a pull request.

📧 **Contact**
If you have any questions or suggestions, feel free to reach out to us at [support@example.com](mailto:support@example.com).

🔖 **References**
- [sklearn Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
