import os
import subprocess
from datetime import datetime

class BrandEngine:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        os.makedirs(repo_path, exist_ok=True)
        # Initialize git if not already done
        subprocess.run(["git", "init"], cwd=self.repo_path)

    def save_iteration(self, filename, content, message):
        """Saves a design change and commits it to Git history"""
        file_path = os.path.join(self.repo_path, filename)
        
        with open(file_path, "w") as f:
            f.write(content)
            
        # Git Workflow: Add and Commit
        subprocess.run(["git", "add", filename], cwd=self.repo_path)
        subprocess.run(["git", "commit", "-m", f"ITERATION: {message}"], cwd=self.repo_path)
        print(f"Successfully versioned: {message}")

    def get_history(self):
        """Retrieves the iteration log"""
        result = subprocess.run(["git", "log", "--oneline"], cwd=self.repo_path, capture_output=True, text=True)
        return result.stdout

if __name__ == "__main__":
    engine = BrandEngine(repo_path="./design_repo")
    engine.save_iteration("logo_v1.txt", "Yellow/Blue Logo", "Initial Gas Station Branding")
    engine.save_iteration("logo_v1.txt", "Red/White Logo", "Refined Palette for visibility")
    
    print("\n--- Iteration History ---")
    print(engine.get_history())