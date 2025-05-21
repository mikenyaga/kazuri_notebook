import textwrap
import re

def insert_code_into_next_cell(text: str) -> None:
    """
    Extract code from text (if in code blocks) and insert into the next Jupyter notebook cell.
    Works reliably in both classic Jupyter Notebook and JupyterLab.
    
    Args:
        text (str): The text containing code, potentially within code blocks.
    """
    try:
        # Check if the text contains a code block (```python ... ```)
        code_block_pattern = r'```(?:python)?\s*([\s\S]*?)\s*```'
        code_blocks = re.findall(code_block_pattern, text)
        
        # If code blocks are found, extract just the code
        if code_blocks:
            # Join multiple code blocks with newlines if there are multiple
            code = '\n\n'.join(code_blocks)
        else:
            # If no code blocks found, use the original text
            code = text
        
        # Clean up the code indentation
        code = textwrap.dedent(code).strip()
        
        # Get IPython shell instance
        from IPython.core.getipython import get_ipython
        shell = get_ipython()
        
        if shell is None:
            print("Not in an IPython environment. Cannot insert code into cell.")
            print("Here's the extracted code:\n")
            print(code)
            return
        
        # Create the payload for inserting a new cell
        payload = dict(
            source='set_next_input',
            text=code,
            replace=False,
        )
        
        # Write the payload to insert the new cell with code
        shell.payload_manager.write_payload(payload, single=False)
        
        print("Code extracted and inserted into new cell.")
        
    except Exception as e:
        print(f"Error during code insertion: {str(e)}")
        print("\nHere's the original text:")
        print(text)