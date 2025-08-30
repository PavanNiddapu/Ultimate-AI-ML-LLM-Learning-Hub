# Linear Regression from Scratch

## 🎯 Learning Objectives

By the end of this example, you will:
- Understand the mathematical foundation of linear regression
- Implement linear regression using only NumPy
- Learn gradient descent optimization
- Compare your implementation with scikit-learn
- Visualize the learning process

## 📚 Prerequisites

- Basic Python programming
- Understanding of functions and loops
- Basic mathematical concepts (slope, intercept)
- Familiarity with NumPy arrays (helpful but not required)

## ⏱️ Time Estimate

**30-45 minutes** for complete understanding and implementation

## 🧮 Mathematical Foundation

Linear regression finds the best line through data points using the equation:
```
y = mx + b
```
Where:
- `y` = predicted value
- `m` = slope (weight)
- `x` = input feature
- `b` = y-intercept (bias)

### Cost Function
We use Mean Squared Error (MSE) to measure how wrong our predictions are:
```
MSE = (1/n) * Σ(y_actual - y_predicted)²
```

### Gradient Descent
We minimize the cost by updating weights and bias:
```
m = m - α * dm
b = b - α * db
```
Where `α` is the learning rate and `dm`, `db` are gradients.

## 💻 Implementation

See the complete implementation in:
- `linear_regression_scratch.py` - Educational version with comments
- `tutorial.ipynb` - Interactive Jupyter notebook
- `comparison.py` - Compare with scikit-learn

## 🚀 Quick Start

```bash
# Install dependencies
pip install numpy matplotlib scikit-learn

# Run the basic implementation
python linear_regression_scratch.py

# Open interactive notebook
jupyter notebook tutorial.ipynb
```

## 🎯 Key Takeaways

1. **Linear regression is simple but powerful** for understanding relationships
2. **Gradient descent** is a fundamental optimization technique
3. **Cost functions** help us measure and improve model performance
4. **Visualization** helps understand how the algorithm learns
5. **NumPy** provides efficient tools for mathematical operations

## 🔗 Next Steps

- Try with multiple features (multiple linear regression)
- Experiment with different learning rates
- Add regularization to prevent overfitting
- Explore other optimization algorithms
- Move on to logistic regression for classification

## 📖 Additional Resources

- [Khan Academy: Intro to Linear Regression](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data)
- [3Blue1Brown: Neural Networks](https://www.3blue1brown.com/topics/neural-networks)
- [Coursera: Machine Learning Course](https://www.coursera.org/learn/machine-learning)