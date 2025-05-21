import subprocess
import sys

def run_bandit():
    print("Running Bandit...")
    result = subprocess.run(["bandit", "-r", "kazuri", "-f", "custom"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Bandit found some issues. Please review the output above.")
    else:
        print("Bandit scan completed successfully. No issues found.")

def run_safety():
    print("Running Safety...")
    result = subprocess.run(["safety", "check", "-r", "requirements.txt"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Safety found some vulnerabilities. Please review the output above.")
    else:
        print("Safety scan completed successfully. No vulnerabilities found.")

if __name__ == "__main__":
    run_bandit()
    print("\n" + "="*50 + "\n")
    run_safety()
