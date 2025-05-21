from .config import load_config
from .api_client import APIClient

# Load configuration
config = load_config()

# Initialize API client
api_client = APIClient(config['api_endpoint_url'])

def kazuri(prompt: str) -> None:
    """
    Generate Python code based on the given prompt and insert it into the next Jupyter notebook cell.

    Args:
        prompt (str): The prompt for code generation.
    """
    try:
        # Generate code and insert it into the next cell
        api_client.generate_and_insert_code(prompt)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)

# Export the main function
__all__ = ['kazuri']
