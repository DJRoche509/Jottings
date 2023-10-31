from app import app  # Import the Flask app instance from app package
from flask import render_template, redirect, url_for, flash
from app.models import db, Task
from app import forms   # Import the forms module from the app package
from datetime import datetime, timedelta

@app.route('/')
@app.route('/home')
def index():
    with app.app_context():
        tasks = Task.query.all()
    
        formatted_tasks = []
        for task in tasks:            
            formatted_task = {
                'id':task.id,
                "title":task.title.capitalize(),
                "formatted_date": task.date.strftime("%a, %b %d, %Y at %I:%M %p CST")
            }
            formatted_tasks.append(formatted_task)
            print(formatted_tasks)

    return render_template('index.html', tasks = formatted_tasks)


@app.route('/addNote', methods = ["GET", 'POST'])
def addNote():
    form = forms.AddNoteForm()
    if form.validate_on_submit():
        with app.app_context():
            t = Task(title=form.title.data, date = datetime.utcnow() - timedelta( hours=5 ))
            db.session.add(t)
            db.session.commit()
        # Flash confirmation message with the last part of user's input
        flash(f'Note about "{form.title.data.split()[-1].capitalize()}" has been successfully added.')
        return redirect(url_for('index'))
    return render_template('addNote.html', form = form)


@app.route('/editNote/<int:task_id>', methods = ['GET','POST'])
def editNote(task_id):
    form = forms.AddNoteForm()
    with app.app_context():        
        task = Task.query.get(task_id)  # Query the task_id for the task
        if task:
            if form.validate_on_submit():
                task.title = form.title.data
                task.date = datetime.utcnow()
                db.session.commit()
                flash('Task has been updated successfully')
                return redirect(url_for('index'))
            # If form is not validated on submit, continue with update form title & render it to HTML
            return render_template('editNote.html', form=form, task_id=task_id, title=task.title)
    flash('WARNING: Task not found !!!')
    return redirect(url_for('index'))


@app.route('/deleteNote/<int:task_id>', methods = ['GET','POST'])
def deleteNote(task_id):
    form = forms.DeleteNoteForm()
    with app.app_context():        
        task = Task.query.get(task_id)  # Query the task_id for the task
        if task:
            if form.validate_on_submit():
                db.session.delete(task)
                db.session.commit()
                flash('Task has been deleted successfully')
                return redirect(url_for('index'))
            # If form is not validated on submit, continue with delete form title & render it to HTML
            return render_template('deleteNote.html', form=form, task_id=task_id, title=task.title)
    flash('WARNING: Task not found !!!')
    return redirect(url_for('index'))

