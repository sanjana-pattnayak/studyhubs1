from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Dashboard')

@app.route('/resources')
def resources():
    # Mock data for resources
    subjects = [
        {'name': 'Data Structures', 'code': 'CS201', 'desc': 'Arrays, Linked Lists, Trees, Graphs'},
        {'name': 'Algorithms', 'code': 'CS202', 'desc': 'Sorting, Searching, DP, Greedy'},
        {'name': 'Operating Systems', 'code': 'CS301', 'desc': 'Processes, Threads, Memory Mgmt'},
        {'name': 'DBMS', 'code': 'CS302', 'desc': 'SQL, Normalization, Transactions'},
        {'name': 'Computer Networks', 'code': 'CS303', 'desc': 'OSI Model, TCP/IP, Routing'}
    ]
    return render_template('resources.html', title='Resources', subjects=subjects)

@app.route('/planner')
def planner():
    return render_template('planner.html', title='Study Planner')

@app.route('/gpa')
def gpa():
    return render_template('gpa.html', title='GPA Calculator')

if __name__ == '__main__':
    app.run(debug=True)
