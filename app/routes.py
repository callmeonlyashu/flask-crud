from flask import render_template, request, redirect
from app import app, db
from app.models import Employee

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    entries = Employee.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        salary = form.get('salary')
        if not name or salary:
            employee = Employee(name = name, salary = salary)
            db.session.add(employee)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        employee = Employee.query.get(id)
        if employee:
            return render_template('update.html', employee=employee)

    return "of the jedi"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        employee = Employee.query.get(id)
        if employee:
            form = request.form
            name = form.get('name')
            salary = form.get('salary')
            employee.name = name
            employee.salary = salary
            db.session.commit()
        return redirect('/')

    return "of the jedi"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        employee = Employee.query.get(id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
        return redirect('/')

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"