# Kazuri

Kazuri is a self-hosted AI code assistant for Jupyter notebooks. It generates high-quality Python code based on natural language prompts and automatically inserts the generated code into the next cell of the notebook.

## Features

- Generates clean, efficient, and well-documented Python code
- Follows best practices and PEP 8 style guidelines
- Includes appropriate error handling and type hints
- Supports various tasks including data science, web development, and automation
- Prioritizes security and avoids insecure patterns

## Installation

Kazuri is not available on PyPI. To install it, you need to clone the repository and install it locally. Follow these steps carefully:

1. Ensure you have Python 3.7 or later installed.

2. Upgrade pip to the latest version:
   ```
   python -m pip install --upgrade pip
   ```

3. Install setuptools and wheel:
   ```
   pip install --upgrade setuptools wheel
   ```

4. Clone the repository:
   ```
   git clone https://github.com/hillaryhitch/kazuri_notebook.git
   cd kazuri
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Install the package in editable mode:
   ```
   pip install -e .
   ```

   This will install Kazuri in editable mode, allowing you to make changes to the code and immediately see the effects without reinstalling.

   If you're using this in a production environment, you may want to install it in non-editable mode:
   ```
   pip install .
   ```

If you encounter any issues during installation, please try the following:

1. Ensure you're using the latest versions of pip, setuptools, and wheel:
   ```
   pip install --upgrade pip setuptools wheel
   ```

2. If you're using a virtual environment, make sure it's activated before running the installation commands.

3. If you still encounter issues, try installing the package dependencies manually before installing Kazuri:
   ```
   pip install boto3 requests ipython python-dotenv
   ```

If problems persist, please check your Python installation and environment settings, or seek help in the project's issue tracker.

## Configuration

Kazuri requires configuration for the API endpoint. There are two ways to set this up:

### For Production Environments (Recommended)

Set the environment variable on your server. This is the preferred method for production environments as it keeps sensitive information out of your codebase.

1. On your server, set the following environment variable:

```bash
export KAZURI_API_ENDPOINT_URL=https://your-api-endpoint.com/generate
```

2. To make this change permanent, add the above line to your shell's configuration file (e.g., `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc`), or set it in your server's environment configuration.

### For Local Development

For local development, you can use a `.env` file in your project directory.

1. Create a `.env` file in your project directory with the following content:

```
KAZURI_API_ENDPOINT_URL=https://your-api-endpoint.com/generate
```

2. Ensure that your `.env` file is listed in your `.gitignore` to avoid accidentally committing sensitive information to your repository.

Kazuri will automatically load the configuration from either the environment variable or the `.env` file, with the environment variable taking precedence if both are set.

## Usage

To use Kazuri in your Jupyter notebook:

1. Import the library:

```python
from kazuri import kazuri
```

2. Use the `kazuri` function to generate code:

```python
kazuri("Create a function that calculates the factorial of a number")
```

The generated code will be automatically inserted into the next cell of your Jupyter notebook as executable Python code.

## Security Checks

Kazuri integrates two powerful security tools: Bandit and Safety. These tools help ensure the security of your code and dependencies.

### Running Security Checks

To run the security checks, use the `security_check.py` script in the root directory of the project:

```bash
python security_check.py
```

This script will:

1. Run Bandit to perform a security analysis of your Python code.
2. Run Safety to check your dependencies for known security vulnerabilities.

It's recommended to run these checks regularly, especially before deploying your code or after adding new dependencies.

### Understanding the Results

- Bandit will report any potential security issues in your code, along with their severity and confidence levels.
- Safety will alert you to any known vulnerabilities in your project's dependencies.

If any issues are found, review the output carefully and address the concerns as needed. This may involve updating dependencies, refactoring code, or implementing additional security measures.

## Example

Here's an example of how to use Kazuri:

```python
from kazuri import kazuri

# Generate a function to calculate factorial
kazuri("Create a function that calculates the factorial of a number using recursion")

# The generated code will be inserted into the next cell
# You can then execute the generated code and use the function
# For example:
# factorial(5)  # This will work with the generated code
```

## Code Generation Principles

Kazuri follows these principles when generating code:

1. Generates only code, without explanations (unless requested)
2. Focuses on practical, functioning solutions
3. Prioritizes readability, maintainability, and best practices
4. Includes appropriate error handling
5. Uses modern Python idioms and libraries
6. Adds concise docstrings and comments for complex segments
7. Considers performance implications for operations on large datasets
8. Implements security best practices

## Error Handling

If an error occurs during code generation or insertion, Kazuri will print an error message and insert it as a comment in the next cell. The function will return an empty string in case of errors.

## Contributing

Contributions to Kazuri are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
