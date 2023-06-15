# Pip

- `pip install -e .`
    
    The command `pip install -e .` is used to install a Python package or project in "editable" mode. This mode is also known as "development mode" or "editable installation."
    
    When you run `pip install -e .`, it installs the package or project specified in the current directory (`.`) as an editable package. This means that any changes you make to the source code in that directory will take effect immediately without the need to reinstall the package.
    
    This can be useful during development when you are actively working on a package or project and want to test changes without repeatedly reinstalling it.
    
    To use `pip install -e .`, follow these steps:
    
    1. Open a terminal or command prompt.
    2. Navigate to the directory containing the `setup.py` file of the package or project you want to install. This directory should also contain the source code files.
    3. Run the command `pip install -e .`.
        
        The command will install the package in editable mode, and any changes you make to the source code will be reflected immediately.
        
    
    Note: Make sure you have Python and pip installed on your system and that you are running the command in the correct directory containing the `setup.py` file.