# Locally Run Code

- what is action vs choice in argparse
    
    Action
    
    - **Action** in `argparse` specifies what should be done with a command-line argument when it is parsed. Actions are predefined behaviors that the parser performs upon encountering an argument. For example, an action can dictate whether to store a value, store a boolean flag, count the number of occurrences of a specific argument, or even call a custom function.
    - Common actions include `store` (which stores the argument's value, the default action), `store_true`/`store_false` (which stores the respective Boolean value for flags), `count` (which counts the occurrences of a specific argument), and `append` (which stores multiple values for a single argument in a list).
    - Here is a simple example of specifying an action for a parser argument:
    This tells the parser to treat `-verbose` as a flag that, when present, stores `True` in the namespace object for `verbose`.
        
        ```python
        parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')
        
        ```
        
    
    Choice
    
    - **Choice** is an option you can pass to `argparse.ArgumentParser.add_argument()` that restricts the argument's value to a specific set of choices. This means the command-line argument must take a value that is among a predefined list of choices, or else the parser will raise an error.
    - The `choices` parameter is used to enforce that the command-line argument matches one of the specified values, which is useful for ensuring users select from a predefined set of options.
    - An example of using `choices` would be:
    This restricts the `-color` argument to one of the three specified options: `red`, `green`, or `blue`.
        
        ```python
        parser.add_argument('--color', choices=['red', 'green', 'blue'], help='Choose your favorite color')
        
        ```
        
    
    In summary, **action** in `argparse` defines how a command-line argument should be processed or what action should be taken when the argument is encountered, whereas **choice** restricts the values the argument can accept to a predefined list. Both are mechanisms to control and validate the input received from the command line in a Python script.
    
- store_true
    
    In the `argparse` module of Python, `store_true` is a specific action used to handle boolean command-line arguments. When you specify `store_true` as the action for an argument, it means that, if the argument is present on the command line, the corresponding attribute in the parsed namespace is set to `True`. The default value for this attribute, if the argument is not specified, is `False`. This action is particularly useful for enabling certain features or behaviors via flags without requiring the user to explicitly specify `true` or `false`.
    
    ### Understanding `store_true`
    
    Here's a simple example to illustrate how `store_true` works:
    
    ```python
    import argparse
    
    parser = argparse.ArgumentParser(description="An example of using store_true")
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    
    print('Verbose mode:', args.verbose)
    
    ```
    
    - If you run this script without any arguments, `args.verbose` will be `False`.
    - If you run it with `-verbose`, then `args.verbose` will be `True`.
    
    ### Do All Boolean Args Need It?
    
    Not all boolean arguments need to use `store_true`. The `store_true` action is just one way to handle boolean flags, where the presence of the flag sets the corresponding value to `True`. There's also a `store_false` action, which sets the attribute to `False` if the command-line argument is present, useful for disabling default behaviors.
    
    Whether to use `store_true`, `store_false`, or neither depends on the specific behavior you want:
    
    - **`store_true`**: Use this when the default behavior is `False`, and specifying the argument changes the behavior to `True`. It's useful for enabling optional features.
    - **`store_false`**: Use this when the default behavior is `True`, and specifying the argument changes the behavior to `False`. It's useful for disabling default features.
    - **No Boolean Action**: If your argument requires explicitly specifying `true` or `false` (or other boolean-equivalent values), you might not use `store_true` or `store_false`. Instead, you could use the `type=bool` parameter and handle string-to-boolean conversion yourself, but this is less common because it requires the user to type more.
    
    In many cases, using `store_true` or `store_false` is the most straightforward approach for boolean command-line arguments because it provides a clear, user-friendly way to toggle features or settings without requiring additional values to be specified.
    
    [https://stackoverflow.com/questions/70428108/whats-the-point-of-having-both-action-store-true-and-default-false-in-parser](https://stackoverflow.com/questions/70428108/whats-the-point-of-having-both-action-store-true-and-default-false-in-parser)
    
- how to make a repo allow to be install as a package using pip
    
    To make a repository installable via `pip`, you need to package your Python project properly and host it either on a platform like PyPI (Python Package Index) or directly from a Git repository (e.g., GitHub, GitLab, Bitbucket). Here's a step-by-step guide for both methods:
    
    ### Packaging for PyPI
    
    1. **Structure Your Project**: Your project should have the following structure:
        
        ```
        your_project/
        ├── your_package/
        │   ├── __init__.py
        │   └── module.py
        ├── setup.py
        ├── README.md
        └── LICENSE
        
        ```
        
        The `your_package` directory is where your actual package code resides. `setup.py` is the build script for `setuptools`. It tells setuptools about your package (such as the name and version) and the files to include.
        
    2. **Create a `setup.py` File**: This file contains metadata about your package. Here's an example:
        
        ```python
        from setuptools import setup, find_packages
        
        setup(
            name='your_package_name',
            version='0.1',
            packages=find_packages(),
            description='A description of your project',
            long_description=open('README.md').read(),
            long_description_content_type='text/markdown',
            author='Your Name',
            author_email='your.email@example.com',
            license='MIT',
            install_requires=[
                # Any dependencies your package needs,
                # e.g., 'requests >= 2.23.0'
            ],
            url='<https://github.com/yourusername/your_project>',
            classifiers=[
                # Trove classifiers
                # Full list: <https://pypi.org/classifiers/>
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: MIT License',
            ],
        )
        
        ```
        
    3. **Generate Distribution Archives**: Run the following commands in your project root directory:
        
        ```
        python setup.py sdist bdist_wheel
        
        ```
        
        This command should output a lot of text and once completed should generate two files in the `dist` directory.
        
    4. **Upload Your Package to PyPI**: First, install `twine` if you haven't already:
        
        ```
        pip install twine
        
        ```
        
        Then, upload your package to PyPI:
        
        ```
        twine upload dist/*
        
        ```
        
        You'll need to register an account on PyPI for this step.
        
    5. **Installing Your Package**: Once uploaded, anyone can install your package using:
        
        ```
        pip install your_package_name
        
        ```
        
    
    ### Installing Directly from a Git Repository
    
    If you don't want to upload your package to PyPI, `pip` can install packages directly from a Git repository. Ensure your repository is structured properly, as mentioned above. Then, to install the package directly, you can use:
    
    ```
    pip install git+https://github.com/yourusername/your_project.git
    
    ```
    
    You can specify branches or tags by using `@` and the branch or tag name:
    
    ```
    pip install git+https://github.com/yourusername/your_project.git@your_branch
    
    ```
    
    For both methods, ensure your package is properly structured and that you have a `setup.py` (for PyPI distribution) or at least a structured project (for direct Git installs). This will allow others to easily install your package using `pip`.
    
- why use src folder in repo
    
    Using a `src` folder in a repository is a common practice that offers several benefits for project organization, maintainability, and scalability. Here are the main reasons for adopting this structure:
    
    1. **Separation of Concerns**: The `src` (source) folder separates your source code from other parts of your project, such as documentation, tests, build scripts, and configuration files. This clear separation helps developers and tools easily identify where the main codebase resides.
    2. **Simplifies Build Process**: Having a dedicated source directory makes it easier to configure build tools and automation scripts. You can set the `src` directory as the root for compilation, linting, and other processes, ensuring that only the relevant files are processed.
    3. **Enhanced Readability and Organization**: Organizing your code into a `src` directory, potentially with subdirectories for different modules or components, improves the project's readability. New developers can quickly understand the project structure and find the code they are looking for.
    4. **Facilitates Testing**: By separating source code from test code (often in a `tests` or `test` directory), you can maintain a clean organization and avoid mixing production code with test scripts. This separation is crucial for understanding the project layout and ensuring that test code is not accidentally included in production builds.
    5. **Scalability**: As projects grow, the number of files and directories increases. A `src` folder allows for scalable organization, enabling you to introduce more layers or modules within the source directory without cluttering the root directory of the project.
    6. **Packaging and Distribution**: For projects that are packaged and distributed (e.g., Python packages), the `src` layout can help ensure that only the intended files are included in the package. This prevents accidental inclusion of unrelated files and makes it easier to specify what should be packaged.
    7. **Convention and Community Standards**: Many programming languages and frameworks recommend specific project structures, with a `src` directory being a common convention. Following these conventions can make your project more accessible to others familiar with these standards.
    
    In summary, using a `src` folder is about creating a clean, manageable, and scalable project structure that aligns with best practices and community standards. It helps developers and tools to efficiently interact with the project, ultimately leading to better code quality and easier maintenance.
    
- what's source code
    
    Source code refers to the collection of computer instructions and statements written by programmers in human-readable programming languages before they are compiled or interpreted into machine code that can be executed by a computer. It is essentially the set of instructions that tells a computer what to do. Source code is written in various programming languages, such as Python, Java, C++, JavaScript, and many others, depending on the application's requirements and the development environment.
    
    Key characteristics of source code include:
    
    - **Human-Readable**: It is written in a way that is understandable by humans, using a structured syntax that follows the rules of the chosen programming language.
    - **Editable**: Developers can modify the source code to change how a program operates, fix bugs, or add new features.
    - **Platform-Independent**: In its raw form, source code is generally independent of hardware and operating systems. It needs to be compiled or interpreted to run on a specific platform.
    - **Part of Software Development**: Source code is the primary component in the software development process. It goes through various stages, including writing, testing, debugging, and maintenance.
    - **Stored in Files**: Source code is typically stored in text files, although it may be organized into multiple files and directories to better manage large projects.
    
    The process of turning source code into an executable program involves compilers for compiled languages (e.g., C, C++) or interpreters for interpreted languages (e.g., Python, JavaScript). Compiled languages are transformed into machine code, which can be directly executed by a computer's CPU, while interpreted languages are read and executed line-by-line by an interpreter at runtime.
    
    Source code is not only fundamental to program creation but also central to the concept of open-source software, where the source code is made available to the public for use, modification, and distribution under specific licenses.
    
- is a function of files used for a paper's experiments considered source code
    
    Yes, the functions or files used for a paper's experiments can be considered source code, especially if these functions or files contain instructions written in a programming language to perform specific tasks, analyze data, or run simulations related to the paper's research. In the context of academic research, source code often includes:
    
    - **Scripts for Data Analysis**: Code that processes, analyzes, and visualizes data to generate the results presented in the paper.
    - **Simulation Code**: Programs that simulate models or phenomena under study, often used in fields like physics, engineering, or computational biology.
    - **Algorithm Implementations**: Detailed coding of algorithms that are proposed or tested in the paper, including computational methods, machine learning models, or statistical techniques.
    - **Data Preparation Scripts**: Code used to clean, preprocess, or transform data before analysis.
    - **Experimental Setup**: Code that configures and runs experiments, including setting parameters, executing models, and collecting results.
    
    Considering these as source code is important because:
    
    - **Reproducibility**: Sharing the source code used in experiments allows other researchers to replicate the study's results, a cornerstone of scientific integrity.
    - **Transparency**: Providing access to the code offers a detailed understanding of the methodologies and analyses performed, beyond what is described in the paper itself.
    - **Collaboration and Improvement**: Making the code available enables other researchers to build upon the work, propose improvements, or apply the methods to new problems.
    
    Therefore, in academic and scientific research, the term "source code" encompasses not only traditional software development code but also any scripts, functions, or computational routines that contribute to generating the findings reported in a paper.
    
- when running python locally, how do you import functions from a file in a different folder than the file you're in? (OR: how do I open a file from the root of the repo, if the file is called from within a folder)
    
    When running Python locally, to import functions from a file located in a different folder, you typically have a few options depending on how your project is structured and your specific needs. Here's how you can do it:
    
    ### 1. Using System Path Modification
    
    You can add the directory containing the module you want to import to the Python path at runtime using the `sys.path` list. This method is straightforward but can make your code harder to read and maintain, especially for larger projects.
    
    ```python
    import sys
    sys.path.append('/path/to/the/directory')
    import your_module
    ```
    
    Replace `'/path/to/the/directory'` with the actual path to the folder containing your module, and `your_module` with the name of the module you want to import.
    
    ### 2. Relative Imports (For Packages)
    
    If your files are organized as a package (i.e., they're in a directory with an `__init__.py` file), you can use relative imports. This is cleaner and more maintainable but requires your scripts to be part of a package.
    
    For example, if your directory structure is like this:
    
    ```
    project/
    │
    ├── package1/
    │   ├── __init__.py
    │   └── module1.py
    │
    └── package2/
        ├── __init__.py
        └── module2.py
    
    ```
    
    And you want to import `module1` into `module2`, you can do so with a relative import:
    
    ```python
    # Inside module2.py
    from ..package1 import module1
    
    ```
    
    ### 3. Using `importlib`
    
    For more dynamic imports, you can use the `importlib` module, which allows for importing modules programmatically. This is useful for more complex import patterns or when module names are determined at runtime.
    
    ```python
    import importlib.util
    import sys
    
    def module_from_path(path, name):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
        return module
    
    your_module = module_from_path('/path/to/your_module.py', 'your_module_name')
    
    ```
    
    Replace `'/path/to/your_module.py'` with the path to your module file and `'your_module_name'` with the name you want to give the module.
    
    ### Best Practices
    
    - **Use Virtual Environments:** To manage dependencies and Python paths more easily.
    - **Package Your Project:** Structure your project as a package when possible. This makes relative imports cleaner and your project easier to understand and maintain.
    - **Avoid `sys.path` Manipulation:** Although quick and easy, modifying `sys.path` directly can lead to code that's hard to debug and maintain, especially in larger projects or when working in a team.
    
    Choosing the right method depends on your project's structure and the scope of what you're trying to achieve. For smaller scripts or temporary solutions, modifying `sys.path` might be okay. For larger, more structured projects, organizing your code into packages and using relative imports or `importlib` for dynamic needs is generally better.
    

[https://stackoverflow.com/questions/4383571/importing-files-from-different-folder](https://stackoverflow.com/questions/4383571/importing-files-from-different-folder)

[https://stackoverflow.com/questions/16981921/relative-imports-in-python-3](https://stackoverflow.com/questions/16981921/relative-imports-in-python-3)

- explain more on using **init** to import
    
    Using `__init__.py` files in Python is a common approach to organize your code into packages, making it easier to manage and import modules across different parts of a project. The `__init__.py` file is placed inside a directory to tell Python that the directory should be treated as a package. This file can be empty or contain valid Python code, including import statements. When you import a package, the `__init__.py` file is automatically executed, and you can use it to perform package initialization or make certain modules or variables available at the package level.
    
    Here's how you can use `__init__.py` for importing:
    
    ### Structuring Your Package
    
    Suppose you have the following project structure:
    
    ```
    project/
    │
    ├── mypackage/
    │   ├── __init__.py
    │   ├── module1.py
    │   └── module2.py
    │
    └── main.py
    
    ```
    
    ### Using `__init__.py` to Facilitate Imports
    
    The purpose of `__init__.py` can vary, but one common use is to simplify imports for the end user of your package. For example, you might want users to access classes or functions in `module1.py` and `module2.py` directly from `mypackage` without having to import them explicitly.
    
    ### Example 1: Importing Modules in `__init__.py`
    
    In `mypackage/__init__.py`, you can import the modules or specific functions you want to be accessible:
    
    ```python
    from .module1 import ClassA, function_x
    from .module2 import ClassB, function_y
    
    ```
    
    This way, when someone imports your package, they can directly use `ClassA`, `function_x`, etc., without needing to import `module1` or `module2` explicitly:
    
    ```python
    from mypackage import ClassA, function_x
    
    ```
    
    ### Example 2: Defining an API Surface
    
    You can also use `__init__.py` to define a more controlled API surface for your package. For instance, you might have several internal functions in `module1` and `module2` that you don't want to expose directly. By selectively importing only the necessary items in `__init__.py`, you manage what's exposed to users of your package.
    
    ### Benefits of Using `__init__.py`
    
    - **Organization:** It helps in organizing your modules into packages.
    - **Simplification:** It simplifies the import statements for end-users.
    - **Initialization:** You can perform any initialization code for your package, like setting up logging, initializing database connections, etc.
    - **Control Over Imports:** You control what gets exposed to the users of your package, making your API cleaner and more intuitive.
    
    ### Python 3.3+ Implicit Namespace Packages
    
    Starting with Python 3.3, the presence of `__init__.py` is not strictly required to recognize directories as packages. This feature introduces "implicit namespace packages," which allow for the creation of packages without an `__init__.py` file. However, using `__init__.py` is still a common practice for the reasons mentioned above, including the ability to execute package-level initialization code.
    
    In summary, `__init__.py` plays a crucial role in package organization and import mechanisms in Python, providing flexibility in how modules within a package are exposed and used.
    
- do you need an init in every subfolder of src
    
    In Python, whether you need an `__init__.py` file in every subfolder of a `src` directory (or any directory intended to be used as a Python package or module) depends on the version of Python you are using and how you intend to structure and use your packages.
    
    ### Python Versions Prior to 3.3
    
    For Python versions **before 3.3**, having an `__init__.py` file in every subfolder is necessary if you want Python to treat those directories as packages. This means that if you have a structure like this:
    
    ```
    src/
    ├── package1/
    │   ├── __init__.py
    │   ├── subpackage1/
    │   │   └── __init__.py
    │   └── module1.py
    └── package2/
        ├── __init__.py
        ├── subpackage2/
        │   └── __init__.py
        └── module2.py
    
    ```
    
    Each `__init__.py` file can be empty, but its presence indicates to Python that it should treat the directory as a package, allowing you to import modules from it.
    
    ### Python 3.3 and Later
    
    Starting with **Python 3.3**, the introduction of [PEP 420](https://www.python.org/dev/peps/pep-0420/) brought implicit namespace packages, which allows Python to recognize directories as packages without needing an `__init__.py` file. This change means that for purely organizational purposes, you don't necessarily need an `__init__.py` file in every directory. However, if you want to run initialization code for your package or control what symbols the package exports when `import *` is used, you will still need to include an `__init__.py` file in the relevant directory.
    
    ### Practical Considerations
    
    Despite the allowance for omitting `__init__.py` files in newer versions of Python, many developers continue to use them for several reasons:
    
    - **Compatibility:** If your code needs to be compatible with Python versions older than 3.3, you must include `__init__.py` files.
    - **Initialization:** `__init__.py` files are useful for performing package-level initialization tasks, such as setting up logging, initializing package-wide data structures, or making submodules available at the package level.
    - **Explicitness:** Including `__init__.py` makes it clear to other developers that a directory is intended to be a Python package. This can improve code readability and maintainability.
    
    ### Conclusion
    
    So, do you need an `__init__.py` in every subfolder of `src`? It depends on your specific requirements:
    
    - For compatibility with Python versions before 3.3, yes.
    - For namespace packages in Python 3.3 and later, not necessarily, unless you need package initialization or want to make your package structure explicit.
    
    In general, including `__init__.py` files is a good practice for clarity and explicit package definition, even if they are not strictly required in all cases with modern Python versions.
    
- throw exception or assert if chosen fn arg isn't one of choices python
    
    In Python, you can use either an `assert` statement or raise an exception to ensure that the argument passed to a function is one of the allowed choices. The choice between using `assert` and raising an exception depends on how critical the check is for the ongoing function or the application's stability and what kind of feedback you want to provide to the caller.
    
    ### Using `assert`
    
    The `assert` statement is used during debugging to check for conditions that must be true if the program is running correctly. If the condition is `False`, an `AssertionError` is raised. This method is more suitable for development and debugging environments rather than production code, as assertions can be globally disabled with the `-O` and `-OO` flags when running Python scripts, which removes the `assert` statements.
    
    ```python
    def process_data(choice):
        valid_choices = ['option1', 'option2', 'option3']
        assert choice in valid_choices, f"{choice} is not a valid choice."
        # Function logic here
    
    # Example call
    process_data('option1')  # This will proceed.
    process_data('invalid_option')  # This will raise an AssertionError.
    
    ```
    
    ### Raising an Exception
    
    Raising an exception is more suitable for production code where you want to enforce the validation regardless of how the Python interpreter is executed. It allows for more granular control over error handling, letting you define custom exceptions or use built-in ones to communicate specific issues.
    
    ```python
    def process_data(choice):
        valid_choices = ['option1', 'option2', 'option3']
        if choice not in valid_choices:
            raise ValueError(f"{choice} is not a valid choice.")
        # Function logic here
    
    # Example call
    process_data('option1')  # This will proceed.
    process_data('invalid_option')  # This will raise a ValueError.
    
    ```
    
    ### Conclusion
    
    Use `assert` for conditions that you expect to never happen in a correctly functioning program (more like a sanity check) and exceptions for validation that must always be enforced, providing more robust error handling and user feedback in your application.