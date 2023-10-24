from flask import Flask, request
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, write

app = Flask(__name)

@app.route('/execute_notebook', methods=['POST'])
def execute_notebook():
    notebook_link = request.form.get('https://colab.research.google.com/drive/1mgUWEgPIcxooLXjgaT9mgYshRnBgTFeC?usp=sharing')

    # Download the notebook content (if needed) and read it
    # Replace this with the code to fetch the notebook content
    notebook_content = fetch_notebook_content(notebook_link)

    # Read the notebook
    notebook = read(notebook_content, as_version=4)

    # Create an execution preprocessor
    execute_preprocessor = ExecutePreprocessor(timeout=None, kernel_name='python3')

    # Execute the notebook in-memory
    execute_preprocessor.preprocess(notebook, {})

    # The notebook is now executed in-memory, but not saved

    return 'Notebook execution complete'

if __name__ == '__main__':
    app.run()
