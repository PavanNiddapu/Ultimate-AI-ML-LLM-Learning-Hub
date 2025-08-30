"""
Linear Regression from Scratch
A simple, educational implementation of linear regression using only NumPy.

Author: Ultimate AI/ML/LLM Learning Hub
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional


class LinearRegressionScratch:
    """
    Simple linear regression implementation using gradient descent.
    
    This implementation is designed for educational purposes and includes
    detailed comments to help understand the underlying mathematics.
    """
    
    def __init__(self, learning_rate: float = 0.01, max_iterations: int = 1000):
        """
        Initialize the linear regression model.
        
        Args:
            learning_rate: Step size for gradient descent (default: 0.01)
            max_iterations: Maximum number of training iterations (default: 1000)
        """
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weight = 0.0  # Slope (m)
        self.bias = 0.0    # Y-intercept (b)
        self.cost_history = []  # Track cost over iterations
        
    def _compute_cost(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute the Mean Squared Error cost function.
        
        Cost = (1/2m) * Σ(y_predicted - y_actual)²
        
        Args:
            X: Input features (1D array)
            y: True target values (1D array)
            
        Returns:
            Mean squared error cost
        """
        m = len(X)  # Number of training examples
        y_predicted = self.predict(X)
        cost = (1 / (2 * m)) * np.sum((y_predicted - y) ** 2)
        return cost
    
    def _compute_gradients(self, X: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
        """
        Compute gradients for weight and bias.
        
        dw = (1/m) * Σ(y_predicted - y_actual) * x
        db = (1/m) * Σ(y_predicted - y_actual)
        
        Args:
            X: Input features (1D array)
            y: True target values (1D array)
            
        Returns:
            Tuple of (weight_gradient, bias_gradient)
        """
        m = len(X)
        y_predicted = self.predict(X)
        
        # Calculate error
        error = y_predicted - y
        
        # Compute gradients
        weight_gradient = (1 / m) * np.sum(error * X)
        bias_gradient = (1 / m) * np.sum(error)
        
        return weight_gradient, bias_gradient
    
    def fit(self, X: np.ndarray, y: np.ndarray, verbose: bool = True) -> None:
        """
        Train the linear regression model using gradient descent.
        
        Args:
            X: Input features (1D array)
            y: Target values (1D array)
            verbose: Whether to print training progress
        """
        # Convert to numpy arrays if needed
        X = np.array(X)
        y = np.array(y)
        
        # Training loop
        for i in range(self.max_iterations):
            # Compute cost and gradients
            cost = self._compute_cost(X, y)
            weight_grad, bias_grad = self._compute_gradients(X, y)
            
            # Update parameters using gradient descent
            self.weight -= self.learning_rate * weight_grad
            self.bias -= self.learning_rate * bias_grad
            
            # Store cost for plotting
            self.cost_history.append(cost)
            
            # Print progress every 100 iterations
            if verbose and (i + 1) % 100 == 0:
                print(f"Iteration {i + 1:4d}: Cost = {cost:.6f}, "
                      f"Weight = {self.weight:.4f}, Bias = {self.bias:.4f}")
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the linear regression equation: y = wx + b
        
        Args:
            X: Input features
            
        Returns:
            Predicted values
        """
        return self.weight * X + self.bias
    
    def plot_results(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Visualize the training results.
        
        Args:
            X: Input features used for training
            y: True target values
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot 1: Data points and fitted line
        ax1.scatter(X, y, color='blue', alpha=0.6, label='Data points')
        
        # Create line for plotting
        x_range = np.linspace(X.min(), X.max(), 100)
        y_pred_range = self.predict(x_range)
        ax1.plot(x_range, y_pred_range, color='red', linewidth=2, 
                label=f'Fitted line: y = {self.weight:.2f}x + {self.bias:.2f}')
        
        ax1.set_xlabel('X')
        ax1.set_ylabel('y')
        ax1.set_title('Linear Regression Results')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Cost function over iterations
        ax2.plot(self.cost_history, color='green', linewidth=2)
        ax2.set_xlabel('Iteration')
        ax2.set_ylabel('Cost')
        ax2.set_title('Cost Function During Training')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()


def generate_sample_data(n_samples: int = 100, noise: float = 0.1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate sample data for testing linear regression.
    
    Args:
        n_samples: Number of data points to generate
        noise: Amount of random noise to add
        
    Returns:
        Tuple of (X, y) arrays
    """
    np.random.seed(42)  # For reproducible results
    
    # Generate X values
    X = np.random.uniform(-2, 2, n_samples)
    
    # True relationship: y = 2x + 1 + noise
    y = 2 * X + 1 + np.random.normal(0, noise, n_samples)
    
    return X, y


def main():
    """
    Demonstration of linear regression from scratch.
    """
    print("🚀 Linear Regression from Scratch Demo")
    print("=" * 40)
    
    # Generate sample data
    print("📊 Generating sample data...")
    X, y = generate_sample_data(n_samples=100, noise=0.5)
    print(f"Generated {len(X)} data points")
    
    # Create and train model
    print("\n🧠 Training linear regression model...")
    model = LinearRegressionScratch(learning_rate=0.01, max_iterations=1000)
    model.fit(X, y, verbose=True)
    
    # Print final results
    print(f"\n✅ Training completed!")
    print(f"Final weight (slope): {model.weight:.4f}")
    print(f"Final bias (intercept): {model.bias:.4f}")
    print(f"True relationship: y = 2x + 1")
    
    # Make some predictions
    test_X = np.array([0, 1, -1, 2])
    predictions = model.predict(test_X)
    
    print(f"\n🔮 Sample predictions:")
    for x, pred in zip(test_X, predictions):
        print(f"X = {x:2.0f} -> Predicted y = {pred:.4f}")
    
    # Visualize results
    print("\n📈 Displaying results...")
    model.plot_results(X, y)


if __name__ == "__main__":
    main()