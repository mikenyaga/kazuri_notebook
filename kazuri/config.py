import os
from dotenv import load_dotenv
from typing import Dict

def load_config() -> Dict[str, str]:
    """
    Load configuration from environment variables or .env file.

    Returns:
        Dict[str, str]: A dictionary containing the configuration.
    """
    print("Starting to load configuration...")
    # Load environment variables from .env file if it exists
    load_dotenv()
    print(f"Loaded .env file. Current working directory: {os.getcwd()}")

    config = {
        'api_endpoint_url': os.getenv('KAZURI_API_ENDPOINT_URL'),
    }
    print(f"Loaded configuration")

    # Validate required configuration
    if config['api_endpoint_url'] is None:
        print("Error: Missing api_endpoint_url in configuration")
        raise ValueError("Missing required configuration: api_endpoint_url")

    print("Configuration loaded successfully")
    return config
