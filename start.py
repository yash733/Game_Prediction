import os
import sys
import subprocess

class Setup_():
    def __init__(self, venv_name='.env', py_version=None):
        
        if py_version == None:
            py_version = self.get_version()
        
        if not os.path.exists(venv_name):  # Check if .env directory doesn't exist
            print(f"Current directory: {os.getcwd()}")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'virtualenv'])
                print("Virtualenv package installed successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Virtualenv package installation failed, error: {e}")
                return  

            command = ['virtualenv', '-p', f'python{py_version}', venv_name]
            try:
                subprocess.check_call(command)
                print(f"Virtual environment '{venv_name}' created successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Virtual environment creation failed, error: {e}")
                return  # Stop execution if virtualenv creation fails

        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirement.txt'])
            print("Requirements installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while installing requirements: {e}")
    
    def get_version(self):
        try:
            version = sys.version_info
            return f'{version.major}.{version.minor}'
        except:
            print('No python version found, Kindly download pyhon')

if __name__ == "__main__":
    setup = Setup_()