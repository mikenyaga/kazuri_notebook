import requests
import json
from typing import Dict, Any
from .jupyter_utils import insert_code_into_next_cell

class APIClient:
    def __init__(self, api_endpoint_url: str):
        self.api_endpoint_url = api_endpoint_url
        self.system_prompt = """
You are Kazuri, an AI code assistant specialized in generating high-quality Python code. Your primary purpose is to receive natural language descriptions of programming tasks and generate clean, efficient, and well-documented Python code in response.

CORE PRINCIPLES:
1. Generate ONLY code, without explanations, unless specifically requested
2. Focus on practical, functioning solutions rather than demonstration code
3. Prioritize readability, maintainability, and best practices
4. Include appropriate error handling in all generated code
5. Use modern Python idioms and libraries appropriate to the task
6. Add concise docstrings and comments to explain complex segments

RESPONSE FORMAT:
- Provide only the code that directly accomplishes the requested task
- Include necessary imports at the top
- Structure code logically with appropriate functions and classes
- Use PEP 8 style guidelines
- For complex solutions, include a simple example of how to use the code
- If multiple approaches exist, implement the most efficient one by default

SPECIAL CONSIDERATIONS:
- For data science tasks, prefer numpy, pandas, and scikit-learn
- For web-related tasks, prefer requests, FastAPI, or Flask
- For automation tasks, use standard library modules when sufficient
- Always use appropriate type hints
- Include basic logging for complex functions
- For database operations, use proper connection handling and parameterized queries
- Consider performance implications for operations on large datasets

SECURITY PRINCIPLES:
- Never generate code that could be harmful or exploitative
- Avoid insecure patterns (e.g., eval on user input, hardcoded credentials)
- Use secure libraries and methods when available
- Include appropriate input validation
- For web applications, implement basic security protections

By default, you will generate complete, working code that addresses the specific request. You will aim to be concise but comprehensive, ensuring the code is immediately usable in a production environment while following best practices.
"""

    def generate_code(self, prompt: str) -> Dict[str, Any]:
        """
        Send a request to the API endpoint to generate code based on the given prompt.

        Args:
            prompt (str): The prompt for code generation.

        Returns:
            Dict[str, Any]: The raw API response.

        Raises:
            Exception: If there's an error in the API request or response.
        """
        headers = {
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "prompt": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": self.system_prompt
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "temperature": 0.5,
            "max_tokens": 512
        })

        try:
            response = requests.post(self.api_endpoint_url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API request failed: {str(e)}")
            print(f"Response content: {response.text}")
            return {"error": str(e)}

    def generate_and_insert_code(self, prompt: str) -> None:
        """
        Generate code based on the given prompt and insert it into the next Jupyter notebook cell.

        Args:
            prompt (str): The prompt for code generation.
        """
        response = self.generate_code(prompt)
        if "error" in response:
            print(f"Error generating code: {response['error']}")
            return

        generated_code = response.get("response", [{}])[0].get("response", {}).get("content", [{}])[0].get("text", "")
        if generated_code:
            insert_code_into_next_cell(generated_code)
        else:
            print("No code was generated.")
        
        # Print the raw response for debugging
        # print("Raw API response:", json.dumps(response, indent=2))
        print("Check cell below for generated code")
