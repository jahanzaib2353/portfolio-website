from flask import Flask, render_template

app = Flask(__name__)

# Sample projects data
projects = [
    {
        'title': 'Project One',
        'description': 'This is the first project.',
        'image': '/static/images/project1.png',  # Replace with the actual path to your image file
        'url': 'https://jahanzaib-nlp.streamlit.app/',
    },
    {
        'title': 'Project Two',
        'description': 'This is the second project.',
        'image': '/static/images/project2.png',  # Replace with the actual path to your image file
        'url': 'https://n-gram-generator-jahanzaib2353.streamlit.app/',
    },

]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def project():
    return render_template('projects.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

if __name__ == '__main__':
    app.run(debug=True)
