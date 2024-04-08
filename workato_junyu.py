from flask import Flask, render_template, redirect, url_for

from jwt_token import generate_fully_embedded_url

app = Flask(__name__)

# This list represents your "My Workflows" - initially empty
my_workflows = []

@app.route('/')
def index():
    # Render an HTML template that shows the "Templates" and "My Workflows"
    return render_template('index.html', my_workflows=my_workflows)

@app.route('/add_workflow')
def add_workflow():
    # This function simulates generating a URL and opens it in a new tab
    # For this example, let's use a placeholder URL
    url = generate_fully_embedded_url("3649871", "recipes/46119083")

    new_workflow = {
        "name": "Salesforce new lead workflow",
        "url" : url
    }
    # Add the new workflow to the list
    my_workflows.append(new_workflow)
    # Redirect back to the home page
    return url

@app.route('/workflow/<int:workflow_id>')
def workflow(workflow_id):
    # Get the selected workflow URL and redirect to it
    workflow_url = my_workflows[workflow_id]["url"]
    return redirect(workflow_url)

if __name__ == '__main__':
    app.run(debug=True)