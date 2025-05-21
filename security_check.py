import sys
import subprocess

def run_security_check(tool_name, *args):
    try:
        print(f"Running {tool_name}...")
        result = subprocess.run([sys.executable, "-m", tool_name] + list(args), capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"{tool_name} found some issues. Please review the output above.")
        else:
            print(f"{tool_name} scan completed successfully.")
    except Exception as e:
        print(f"An error occurred while running {tool_name}: {str(e)}")
        print(f"Make sure {tool_name} is installed in your current environment.")

def run_checks():
    run_security_check("bandit", "-r", ".", "-f", "custom")
    print("\n" + "="*50 + "\n")
    run_security_check("safety", "check", "-r", "requirements.txt")

if __name__ == "__main__":
    run_checks()
