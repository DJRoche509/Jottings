from app import app  # Import the Flask app instance from app package
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app.models import db, Task
from app import forms   # Import the forms module from the app package
from datetime import datetime, timezone, timedelta

@app.route('/')
@app.route('/home')
def index():
    with app.app_context():
        tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)


@app.route('/addNote', methods = ["GET", 'POST'])
def addNote():
    form = forms.AddNoteForm()
    if form.validate_on_submit():
        with app.app_context():
            t = Task(title=form.title.data, date = datetime.utcnow() - timedelta( hours=5 ))
            db.session.add(t)
            db.session.commit()
        flash(f'Note about {form.title.data.split()[0]} has been successfully added.')
        return redirect(url_for('index'))
    return render_template('addNote.html', form = form)


@app.route('/deleteNote/<int:task_id>', methods = ['GET','POST'])
def deleteNote(task_id):
    task = Task.query.get('task_id')
    form = forms.DeleteNoteForm()
    if task:
        if form.validate_on_submit:
            with app.app_context():
                db.session.delete(task)
                db.session.commit()
            flash('Task has been deleted successfully')
            return redirect(url_for('index'))
        # If form is not validated on submit, continue w update form title & render it to HTML
        return render_template('deleteNote.html', form=form, task_id=task_id, title=task.title)
    flash('WARNING: Task not found !!!')
    return redirect(url_for('index'))

