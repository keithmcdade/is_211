import re
import json
import os
import os.path
from flask import Flask, render_template, request, redirect, flash

def create_app():
    app = Flask(__name__)
    app.secret_key = "b'\xf7\xf2\xc6\xd5S\xd2\xd32\x96Q\x8b\xdf\x17\x03\xc0\\'"
    return app


app = create_app()


@app.route('/')
def todoapp():
    # controller function for processing http requests
    
    # if os.path.isfile("todoapp.json"):
        # with open("todoapp.json", 'r+') as file:
            # todo_list = json.load(file)
            # for item in todo_list:
                # todo(item["task"], item["email"], item["priority"])
    
    columns = ["Task", "Email Address", "Priority Level"]
    table_head = f"<thead>\n<tr><th>{'</th><th>'.join(columns)}</th></tr>\n</thead>"
    table_body = "\n<tbody>\n"
    
    for instance in todo.instances:
        task_data = [instance.task, instance.email, instance.priority]
        table_body += f"<tr><td>{'</td><td>'.join(task_data)}</td></tr>\n"
    table_body += "</tbody>\n"
    
    return render_template('index.html', table=f"<table>\n{table_head}{table_body}</table>")


@app.route('/submit', methods = ['POST'])
def submit():
    # controller function for submitting to do list info
    task = request.form['task']
    
    email = request.form['email']
    email_regex = "[^@\s]+@[^@\s]+\.[^@\s]+"
    if not re.match(email_regex, email):
        flash("Invalid email address.")
        return redirect('/')
    
    priority = request.form['priority']
    if priority not in ["low", "medium", "high"]:
        flash("Something went wrong.")
        return redirect('/')
    
    to_do = todo(task, email, priority)
    print("Task incoming:\n", repr(to_do))
    
    return redirect('/')


@app.route('/clear', methods = ['POST'])
def clear():
    os.remove("todoapp.json")
    todo.instances.clear()
    return redirect('/')


@app.route('/save', methods = ['POST'])
def save():
    todo_list = []
    if os.path.isfile("todoapp.json"):
        os.remove("todoapp.json")
    with open("todoapp.json", "a") as file:
        for instance in todo.instances:
            todo_list.append(instance.__dict__)
        json.dump(todo_list, file)
        todo.instances = []
    return redirect('/')

# model for storing to do list data
class todo:
    instances = []
    def __init__(self, task, email, priority):
        self.task = task
        self.email = email
        self.priority = priority
        todo.instances.append(self)
        
    def __repr__(self):
        return f"task={self.task}, email={self.email}, priority={self.priority}"
    
    def __del__(self):
        print(f"\n{self.task} has been removed from to do list.")


def load_list():
    if os.path.isfile("todoapp.json"):
        with open("todoapp.json", 'r') as file:
            todo_list = json.load(file)
            for item in todo_list:
                todo(item["task"], item["email"], item["priority"])
            # os.remove("todoapp.json")
            # for item in json.load(file):
                # entry = todo(item)
                # print(entry)
                # print(type(entry))

if __name__ == "__main__":
    app.run()
    # load_list()
    