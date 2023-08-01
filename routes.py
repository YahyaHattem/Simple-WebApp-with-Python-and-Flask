from app import app
from flask import render_template
from models import Task
from datetime import datetime

import forms

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add',methods=['GET','POST'])    
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title = form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html',form = form)