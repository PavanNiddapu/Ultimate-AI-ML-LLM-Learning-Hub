#!/usr/bin/env python3
"""
Ultimate AI/ML/LLM Learning Hub - Environment Setup Wizard

This interactive script helps users set up their learning environment
with appropriate dependencies and configurations.

Author: Ultimate AI/ML/LLM Learning Hub
License: MIT
"""

import os
import sys
import subprocess
import platform
from pathlib import Path
from typing import List, Dict, Optional


class SetupWizard:
    """Interactive setup wizard for the Ultimate AI/ML/LLM Learning Hub."""
    
    def __init__(self):
        self.python_version = sys.version_info
        self.platform = platform.system().lower()
        self.cwd = Path.cwd()
        self.venv_name = "mlhub-env"
        
    def print_banner(self):
        """Print the welcome banner."""
        print("🚀" + "=" * 60 + "🚀")
        print("   Ultimate AI/ML/LLM Learning Hub - Setup Wizard")
        print("🚀" + "=" * 60 + "🚀")
        print()
        print("This wizard will help you set up your learning environment.")
        print(f"Detected: Python {self.python_version.major}.{self.python_version.minor} on {self.platform.title()}")
        print()
    
    def check_python_version(self) -> bool:
        """Check if Python version is compatible."""
        min_version = (3, 7)
        if self.python_version[:2] < min_version:
            print(f"❌ Python {min_version[0]}.{min_version[1]}+ is required.")
            print(f"   Current version: {self.python_version.major}.{self.python_version.minor}")
            print("   Please upgrade Python and try again.")
            return False
        
        print(f"✅ Python version {self.python_version.major}.{self.python_version.minor} is compatible.")
        return True
    
    def check_pip(self) -> bool:
        """Check if pip is available."""
        try:
            subprocess.run([sys.executable, "-m", "pip", "--version"], 
                         check=True, capture_output=True)
            print("✅ pip is available.")
            return True
        except subprocess.CalledProcessError:
            print("❌ pip is not available.")
            print("   Please install pip and try again.")
            return False
    
    def get_user_preferences(self) -> Dict[str, bool]:
        """Get user preferences for installation."""
        print("\n📋 Please select what you'd like to install:")
        print()
        
        preferences = {}
        
        # Core packages (always install)
        print("✅ Core packages (numpy, pandas, matplotlib, scikit-learn) - Required")
        
        # Optional packages
        questions = [
            ("jupyter", "🔬 Jupyter Notebook (recommended for interactive learning)"),
            ("torch", "🔥 PyTorch (for deep learning tutorials)"),
            ("tensorflow", "🧠 TensorFlow (alternative deep learning framework)"),
            ("advanced", "⚡ Advanced packages (seaborn, plotly, xgboost)")
        ]
        
        for key, description in questions:
            while True:
                response = input(f"{description} [Y/n]: ").strip().lower()
                if response in ['', 'y', 'yes']:
                    preferences[key] = True
                    break
                elif response in ['n', 'no']:
                    preferences[key] = False
                    break
                else:
                    print("Please enter 'y' or 'n'")
        
        return preferences
    
    def create_virtual_environment(self) -> bool:
        """Create a virtual environment."""
        print(f"\n🏗️  Creating virtual environment '{self.venv_name}'...")
        
        venv_path = self.cwd / self.venv_name
        
        if venv_path.exists():
            response = input(f"Virtual environment '{self.venv_name}' already exists. Recreate? [y/N]: ")
            if response.lower() in ['y', 'yes']:
                import shutil
                shutil.rmtree(venv_path)
            else:
                print("Using existing virtual environment.")
                return True
        
        try:
            subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
            print(f"✅ Virtual environment created at: {venv_path}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create virtual environment: {e}")
            return False
    
    def get_venv_python(self) -> str:
        """Get the path to Python in the virtual environment."""
        venv_path = self.cwd / self.venv_name
        
        if self.platform == "windows":
            return str(venv_path / "Scripts" / "python.exe")
        else:
            return str(venv_path / "bin" / "python")
    
    def install_packages(self, preferences: Dict[str, bool]) -> bool:
        """Install packages based on user preferences."""
        print("\n📦 Installing packages...")
        
        # Core packages
        core_packages = [
            "numpy>=1.21.0",
            "pandas>=1.3.0", 
            "matplotlib>=3.5.0",
            "scikit-learn>=1.0.0",
            "ipython>=7.0.0"
        ]
        
        # Optional packages
        optional_packages = {
            "jupyter": ["jupyter>=1.0.0", "ipykernel>=6.0.0"],
            "torch": ["torch>=1.10.0", "torchvision>=0.11.0"],
            "tensorflow": ["tensorflow>=2.7.0"],
            "advanced": [
                "seaborn>=0.11.0",
                "plotly>=5.0.0",
                "xgboost>=1.5.0",
                "tqdm>=4.62.0"
            ]
        }
        
        # Combine packages to install
        packages_to_install = core_packages.copy()
        
        for pref, enabled in preferences.items():
            if enabled and pref in optional_packages:
                packages_to_install.extend(optional_packages[pref])
        
        # Install packages
        python_path = self.get_venv_python()
        
        print(f"Installing {len(packages_to_install)} packages...")
        
        for i, package in enumerate(packages_to_install, 1):
            print(f"  [{i}/{len(packages_to_install)}] Installing {package}...")
            try:
                subprocess.run([
                    python_path, "-m", "pip", "install", package
                ], check=True, capture_output=True, text=True)
                print(f"    ✅ {package}")
            except subprocess.CalledProcessError as e:
                print(f"    ❌ Failed to install {package}: {e}")
                return False
        
        print("✅ All packages installed successfully!")
        return True
    
    def setup_jupyter_kernel(self, preferences: Dict[str, bool]) -> bool:
        """Set up Jupyter kernel for the virtual environment."""
        if not preferences.get("jupyter", False):
            return True
        
        print("\n🔬 Setting up Jupyter kernel...")
        
        python_path = self.get_venv_python()
        
        try:
            subprocess.run([
                python_path, "-m", "ipykernel", "install", 
                "--user", "--name", self.venv_name,
                "--display-name", f"Python (ML Hub - {self.venv_name})"
            ], check=True, capture_output=True)
            print(f"✅ Jupyter kernel '{self.venv_name}' installed.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install Jupyter kernel: {e}")
            return False
    
    def create_activation_script(self):
        """Create a convenient activation script."""
        print("\n📝 Creating activation script...")
        
        if self.platform == "windows":
            script_name = "activate.bat"
            script_content = f"""@echo off
echo Activating Ultimate AI/ML/LLM Learning Hub environment...
call {self.venv_name}\\Scripts\\activate.bat
echo ✅ Environment activated! 
echo.
echo 💡 Quick commands:
echo   jupyter notebook  - Start Jupyter Notebook
echo   python test_setup.py - Test your installation
echo   deactivate - Exit this environment
echo.
"""
        else:
            script_name = "activate.sh"
            script_content = f"""#!/bin/bash
echo "Activating Ultimate AI/ML/LLM Learning Hub environment..."
source {self.venv_name}/bin/activate
echo "✅ Environment activated!"
echo ""
echo "💡 Quick commands:"
echo "  jupyter notebook  - Start Jupyter Notebook" 
echo "  python test_setup.py - Test your installation"
echo "  deactivate - Exit this environment"
echo ""
"""
        
        script_path = self.cwd / script_name
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        if self.platform != "windows":
            os.chmod(script_path, 0o755)
        
        print(f"✅ Activation script created: {script_name}")
        return script_path
    
    def create_test_script(self):
        """Create a test script to verify the installation."""
        test_content = '''"""
Installation verification script for Ultimate AI/ML/LLM Learning Hub
"""

def test_imports():
    """Test that required libraries can be imported."""
    success = True
    
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"), 
        ("matplotlib", "Matplotlib"),
        ("sklearn", "Scikit-learn"),
        ("IPython", "IPython")
    ]
    
    print("🧪 Testing package imports...")
    
    for package, name in packages:
        try:
            __import__(package)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - Failed to import")
            success = False
    
    # Test optional packages
    optional_packages = [
        ("torch", "PyTorch"),
        ("tensorflow", "TensorFlow"),
        ("jupyter", "Jupyter"),
        ("seaborn", "Seaborn")
    ]
    
    print("\\n🔍 Testing optional packages...")
    
    for package, name in optional_packages:
        try:
            __import__(package)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ⚠️  {name} - Not installed (optional)")
    
    return success

def test_basic_operations():
    """Test basic operations."""
    print("\\n🧮 Testing basic operations...")
    
    try:
        import numpy as np
        import pandas as pd
        
        # Test NumPy
        arr = np.array([1, 2, 3])
        print(f"  ✅ NumPy array: {arr}")
        
        # Test Pandas
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        print(f"  ✅ Pandas DataFrame: {df.shape} shape")
        
        # Test sklearn
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        print("  ✅ Scikit-learn model created")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error during testing: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Ultimate AI/ML/LLM Learning Hub - Installation Test")
    print("=" * 55)
    
    imports_ok = test_imports()
    operations_ok = test_basic_operations()
    
    print("\\n" + "=" * 55)
    
    if imports_ok and operations_ok:
        print("🎉 Installation verification PASSED!")
        print("   You're ready to start learning AI/ML/LLM!")
        print("\\n💡 Next steps:")
        print("   1. Open README.md to see the learning paths")
        print("   2. Try: jupyter notebook")
        print("   3. Start with examples/algorithms/linear-regression/")
    else:
        print("❌ Installation verification FAILED!")
        print("   Please check the errors above and reinstall.")
'''
        
        test_path = self.cwd / "test_setup.py"
        with open(test_path, 'w') as f:
            f.write(test_content)
        
        print(f"✅ Test script created: test_setup.py")
        return test_path
    
    def print_completion_message(self, script_path: Path):
        """Print completion message with next steps."""
        print("\n🎉" + "=" * 60 + "🎉")
        print("    Setup completed successfully!")
        print("🎉" + "=" * 60 + "🎉")
        print("\n📋 Next steps:")
        print()
        
        if self.platform == "windows":
            print(f"1. Activate your environment: {script_path.name}")
        else:
            print(f"1. Activate your environment: ./{script_path.name}")
        
        print("2. Test your installation: python test_setup.py")
        print("3. Start Jupyter: jupyter notebook")
        print("4. Begin learning: Open README.md for learning paths")
        print()
        print("🌟 Happy learning! Welcome to the AI/ML/LLM community! 🌟")
    
    def run(self):
        """Run the complete setup wizard."""
        self.print_banner()
        
        # Check prerequisites
        if not self.check_python_version():
            return False
        
        if not self.check_pip():
            return False
        
        # Get user preferences
        preferences = self.get_user_preferences()
        
        # Create virtual environment
        if not self.create_virtual_environment():
            return False
        
        # Install packages
        if not self.install_packages(preferences):
            return False
        
        # Setup Jupyter kernel
        if not self.setup_jupyter_kernel(preferences):
            print("⚠️  Jupyter kernel setup failed, but continuing...")
        
        # Create helper scripts
        script_path = self.create_activation_script()
        self.create_test_script()
        
        # Print completion message
        self.print_completion_message(script_path)
        
        return True


def main():
    """Main function to run the setup wizard."""
    wizard = SetupWizard()
    
    try:
        success = wizard.run()
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())