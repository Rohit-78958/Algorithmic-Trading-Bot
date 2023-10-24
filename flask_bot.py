from flask import Flask, request
import gdown
import subprocess

app = Flask(__name)

@app.route('/execute_notebook', methods=['POST'])
def execute_notebook():
    notebook_link = request.form.get('notebook_link')

    gdown.download(notebook_link, output='notebook.ipynb', quiet=False)

    subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebook.ipynb'])

    return 'Notebook execution complete'

if __name__ == '__main__':
    app.run()
