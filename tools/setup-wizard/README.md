# 🚀 Setup Wizard

Interactive environment setup tool for the Ultimate AI/ML/LLM Learning Hub.

## 🎯 Purpose

This wizard helps you:
- Check system compatibility
- Create an isolated virtual environment
- Install appropriate ML/AI libraries
- Configure Jupyter notebooks
- Verify your installation

## 🏃‍♂️ Quick Start

```bash
cd Ultimate-AI-ML-LLM-Learning-Hub
python tools/setup-wizard/setup_wizard.py
```

## ✨ Features

### 🔍 Automatic Detection
- Python version compatibility
- Operating system optimization
- Existing environment checking

### 📦 Smart Package Installation
- **Core packages**: numpy, pandas, matplotlib, scikit-learn
- **Optional packages**: PyTorch, TensorFlow, Jupyter
- **Advanced tools**: seaborn, plotly, xgboost

### 🧪 Verification
- Import testing for all packages
- Basic operation validation
- Environment activation scripts

### 🛠️ Helper Scripts
- Platform-specific activation scripts
- Installation verification test
- Jupyter kernel configuration

## 📋 Requirements

- Python 3.7 or higher
- pip package manager
- Internet connection for downloads

## 🎮 Interactive Flow

The wizard will ask you:

1. **Core packages** (required): numpy, pandas, matplotlib, scikit-learn
2. **Jupyter Notebook**: For interactive learning (recommended)
3. **PyTorch**: For deep learning tutorials
4. **TensorFlow**: Alternative deep learning framework
5. **Advanced packages**: Additional visualization and ML tools

## 📁 What Gets Created

### Virtual Environment
```
mlhub-env/          # Isolated Python environment
├── bin/            # Python executables (Unix)
├── Scripts/        # Python executables (Windows)
├── lib/            # Installed packages
└── include/        # Header files
```

### Helper Files
```
activate.sh         # Unix activation script
activate.bat        # Windows activation script
test_setup.py       # Installation verification
```

## 🎯 Usage Examples

### Basic Setup (Beginners)
Accept defaults for most questions:
- ✅ Jupyter Notebook
- ⚠️ Skip PyTorch/TensorFlow initially
- ✅ Advanced packages

### Deep Learning Setup
Select deep learning frameworks:
- ✅ Jupyter Notebook
- ✅ PyTorch OR TensorFlow
- ✅ Advanced packages

### Minimal Setup
For limited resources:
- ⚠️ Skip Jupyter (use Colab instead)
- ⚠️ Skip deep learning frameworks
- ⚠️ Skip advanced packages

## 🔧 Manual Setup Alternative

If the wizard fails, you can set up manually:

```bash
# Create virtual environment
python -m venv mlhub-env

# Activate (Unix/macOS)
source mlhub-env/bin/activate

# Activate (Windows)
mlhub-env\Scripts\activate

# Install core packages
pip install numpy pandas matplotlib scikit-learn jupyter

# Install deep learning (optional)
pip install torch tensorflow

# Install advanced packages (optional)
pip install seaborn plotly xgboost tqdm
```

## 🚨 Troubleshooting

### Common Issues

#### Python Version Error
```
❌ Python 3.7+ is required.
```
**Solution**: Upgrade Python from [python.org](https://python.org)

#### pip Not Available
```
❌ pip is not available.
```
**Solutions**:
- Reinstall Python with pip included
- Install pip manually: `python -m ensurepip`

#### Permission Errors (Unix/macOS)
```
❌ Permission denied
```
**Solutions**:
- Use `--user` flag: `pip install --user package`
- Fix permissions: `sudo chown -R $(whoami) ~/.local`

#### Virtual Environment Creation Failed
```
❌ Failed to create virtual environment
```
**Solutions**:
- Check disk space
- Try different location: `python -m venv ~/mlhub-env`
- Use conda instead: `conda create -n mlhub python=3.9`

#### Package Installation Failed
```
❌ Failed to install package
```
**Solutions**:
- Check internet connection
- Update pip: `pip install --upgrade pip`
- Try different package version
- Use conda: `conda install package-name`

### Getting Help

1. **Run verification**: `python test_setup.py`
2. **Check environment**: `which python` and `pip list`
3. **Search issues**: Many solutions on Stack Overflow
4. **Ask community**: Use GitHub Discussions
5. **Alternative setup**: Try Google Colab or Kaggle

## 🎯 Next Steps After Setup

### 1. Verify Installation
```bash
# Activate environment
source activate.sh  # Unix/macOS
# OR
activate.bat        # Windows

# Test setup
python test_setup.py
```

### 2. Start Learning
```bash
# Open learning materials
jupyter notebook

# Try first example
cd examples/algorithms/linear-regression/
python linear_regression_scratch.py
```

### 3. Follow Learning Path
- Read the main [README.md](../../README.md)
- Choose a [learning path](../../docs/learning-paths/)
- Start with [beginner tutorials](../../tutorials/)

## 📊 Package Details

### Core Packages (~200MB)
- **numpy**: Numerical computing
- **pandas**: Data manipulation
- **matplotlib**: Basic plotting
- **scikit-learn**: Machine learning
- **ipython**: Interactive Python

### Deep Learning (~1-2GB)
- **PyTorch**: Dynamic neural networks
- **TensorFlow**: Production ML framework
- **torchvision**: Computer vision utilities

### Advanced Tools (~100MB)
- **seaborn**: Statistical visualization
- **plotly**: Interactive plots
- **xgboost**: Gradient boosting
- **tqdm**: Progress bars

## 🌟 Tips for Success

### Performance Tips
- Use SSD storage for faster package installation
- Ensure good internet connection
- Close other applications during setup

### Learning Tips
- Start with core packages only
- Add deep learning frameworks when needed
- Use virtual environments for different projects
- Keep packages updated regularly

### Best Practices
- Always activate environment before working
- Use `pip list` to see installed packages
- Keep requirements.txt files for reproducibility
- Document your environment setup

---

**Ready to set up your ML learning environment? Run the wizard! 🚀**