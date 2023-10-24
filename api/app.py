from flask import Flask, request
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read
import subprocess
import requests
import shutil

app = Flask(__name)

# Function to download a Colab notebook from Google Drive using the Colab API
def download_notebook_from_google_drive(notebook_link):
    # Extract the file ID from the Google Drive link
    file_id = notebook_link.split('/')[-2]

    # Create a temporary directory to store the notebook
    temp_dir = 'temp_notebook'
    notebook_path = f'{temp_dir}/notebook.ipynb'

    # Download the notebook from Google Drive using the Colab API
    download_url = f'https://colab.research.google.com/drive/1mgUWEgPIcxooLXjgaT9mgYshRnBgTFeC?usp=sharing'
    response = requests.get(download_url)
    notebook_content = response.text

    # Save the notebook content to a local file
    with open(notebook_path, 'w') as f:
        f.write(notebook_content)

    return notebook_path

@app.route('/api/execute_notebook', methods=['POST'])
def execute_notebook():
    # Replace this with the actual Google Drive notebook link
    notebook_link = request.form.get('notebook_link')

    # Download the notebook content from the link and read it
    notebook_path = download_notebook_from_google_drive(notebook_link)

    # Execute the notebook using nbconvert
    subprocess.run(['jupyter', 'nbconvert', '--to', 'html', notebook_path])

    # Clean up: Remove the temporary directory and notebook file
    shutil.rmtree('temp_notebook')

    return 'Notebook execution complete'

if __name__ == '__main__':
    app.run()
