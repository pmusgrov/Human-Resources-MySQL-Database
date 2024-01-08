 # Citation for the following code:
 # Date: 08/02/2023
 # Copied from /OR/ Adapted from /OR/ Based on:
 # Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


# Configuration

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'cs340_'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes 

@app.route('/')
def root():
    return render_template("/index.j2")

@app.route('/employees', methods=["POST", "GET"])
def employees():

    if request.method == "POST":
        # if the user hits create employee
        if request.form.get("add_employee"):
            # grab inputted information
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]
            job_id = request.form["job_id"]
            salary_commission = request.form["salary_commission"]
            department_id = request.form["department_id"]
            location_id = request.form["location_id"]

            # inserts into table
            query = "INSERT INTO Employees (first_name, last_name, email, phone_number, job_id, salary_commission, department_id, location_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, phone_number, job_id, salary_commission, department_id, location_id))
            mysql.connection.commit()

            # return to page
            return redirect("/employees")

    if request.method == "GET":
        # Grab Employees data so we send it to our template to display
        query = "SELECT Employees.employee_id as ID, Employees.first_name as 'First Name', Employees.last_name as 'Last Name', Employees.email as 'Email', Employees.phone_number as 'Phone Number', Employees.job_id as 'Job', Employees.salary_commission as 'Commission', Employees.department_id as 'Department', Employees.location_id as 'Location' FROM Employees INNER JOIN Jobs ON Employees.job_id = Jobs.job_id INNER JOIN Departments ON Employees.department_id = Departments.department_id INNER JOIN Locations ON Employees.location_id = Locations.location_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
    

        # grabs employee for/from dropdown
        query2 = "SELECT job_id first_name FROM Employees"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        employee_data = cur.fetchall()

        # query to grab job id from dropdown
        query3 = "SELECT job_id FROM Jobs"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        job_data = cur.fetchall()

        # query to grab department id from dropdown
        query4 = "SELECT department_id  FROM Departments"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        department_data = cur.fetchall()

        # query to grab location id from dropdown
        query5 = "SELECT location_id  FROM Locations"
        cur = mysql.connection.cursor()
        cur.execute(query5)
        location_data = cur.fetchall()

        return render_template("employees.j2", data=data, employee=employee_data, job=job_data, department=department_data, location=location_data)

    
    
@app.route('/delete_employees/<int:employee_id>')
def delete_employees(employee_id):
    # mySQL query to delete employee with given id
    query= "DELETE FROM Employees WHERE employee_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (employee_id,))
    mysql.connection.commit()

    # return to page
    return redirect("/employees")

@app.route('/edit_employees/<int:employee_id>', methods=["POST", "GET"])
def edit_employees(employee_id):
    if request.method == "GET":
        # query to grab info of employee given id
        query = "SELECT Employees.employee_id as ID, Employees.first_name as 'First Name', Employees.last_name as 'Last Name', Employees.email as 'Email', Employees.phone_number as 'Phone Number', Employees.job_id as 'Job', Employees.salary_commission as 'Commission', Employees.department_id as 'Department', Employees.location_id as 'Location' FROM Employees INNER JOIN Jobs ON Employees.job_id = Jobs.job_id INNER JOIN Departments ON Employees.department_id = Departments.department_id INNER JOIN Locations ON Employees.location_id = Locations.location_id WHERE employee_id = %s" % (employee_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # query to grab job id from dropdown
        query2 = "SELECT job_id FROM Jobs"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        job_data = cur.fetchall()

        # query to grab department id from dropdown
        query3 = "SELECT department_id  FROM Departments"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        department_data = cur.fetchall()

        # query to grab location id from dropdown
        query4 = "SELECT location_id FROM Locations"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        location_data = cur.fetchall()

        # render update_employee page passing data to the template
        return render_template("edit_employees.j2", data=data, job=job_data, department=department_data, location=location_data)

    if request.method == "POST":
        # if user hits update employee
        if request.form.get("Update_Employee"):
            # gets user input
            employee_id = request.form["employee_id"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]
            job_id = request.form["job_id"]
            salary_commission = request.form["salary_commission"]
            department_id = request.form["department_id"]
            location_id = request.form["location_id"]

            # inserts into table
            query = "UPDATE Employees SET Employees.first_name = %s, Employees.last_name = %s, Employees.email = %s, Employees.phone_number = %s, Employees.job_id = %s, Employees.salary_commission = %s, Employees.department_id = %s, Employees.location_id = %s WHERE Employees.employee_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, phone_number, job_id, salary_commission, department_id, location_id, employee_id))
            mysql.connection.commit()

            # back to page
            return redirect("/employees")

@app.route('/index')
def index():
    return render_template("/index.j2")

@app.route('/jobs', methods=["POST", "GET"])
def jobs():
    if request.method == "POST":
        # if the user hits create job
        if request.form.get("add_job"):
            # grab inputted information
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]
            department_id = request.form["department_id"]
            location_id = request.form["location_id"]
            salary = request.form["salary"]
            commission_eligible = request.form['commission_eligible']

            # inserts into table
            query = "INSERT INTO Jobs (start_date, end_date, department_id, location_id, salary, commission_eligible) VALUES (%s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (start_date, end_date, department_id, location_id, salary, commission_eligible))
            mysql.connection.commit()

            # return to page
            return redirect("/jobs")

    if request.method == "GET":
        # Grab Jobs data so we send it to our template to display
        query = "SELECT Jobs.start_date as 'Start Date', Jobs.end_date as 'End Date', Jobs.job_id as ID, Jobs.department_id as 'Department ID', Jobs.location_id as 'Location ID', Jobs.salary as 'Salary', Jobs.commission_eligible as 'Commission Eligible' FROM Jobs INNER JOIN Departments on Jobs.department_id = Departments.department_id INNER JOIN Locations on Jobs.location_id = Locations.location_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT department_id FROM Departments"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        department_data = cur.fetchall()

        query3 = "SELECT location_id FROM Locations"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        location_data = cur.fetchall()

        return render_template("/jobs.j2", data=data, department=department_data, location=location_data)
    

@app.route('/contracts', methods=["POST", "GET"])
def contracts():
    if request.method == "POST":
        # if the user hits create contract
        if request.form.get("add_contract"):
            # grab inputted information
            client_name = request.form["client_name"]
            contract_amount = request.form["contract_amount"]

            # if contract amount is NULL
            if contract_amount == '':
                query = "INSERT INTO Contracts (client_name) VALUES (%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (client_name))
                mysql.connection.commit()

            # otherwise inserts into table
            else:
                query = "INSERT INTO Contracts (client_name, contract_amount) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (client_name, contract_amount))
                mysql.connection.commit()

            # return to page
            return redirect("/contracts")

    if request.method == "GET":
        # Grab Contracts data so we send it to our template to display
        query = "SELECT Contracts.contract_id as ID, Contracts.client_name as 'Client Name', Contracts.contract_amount as 'Contract Amount' FROM Contracts"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("/contracts.j2", data=data)

@app.route('/delete_contracts/<int:contract_id>')
def delete_contracts(contract_id):
    # mySQL query to delete contract with given id
    query= "DELETE FROM Contracts WHERE contract_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (contract_id,))
    mysql.connection.commit()

    # return to page
    return redirect("/contracts")

@app.route('/edit_contracts/<int:contract_id>', methods=["POST", "GET"])
def edit_contracts(contract_id):
    if request.method == "GET":
        # query to grab info of contract given id
        query = "SELECT Contracts.contract_id as ID, Contracts.client_name as 'Client Name', Contracts.contract_amount as 'Contract Amount' FROM Contracts WHERE contract_id = %s" % (contract_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render update_contract page passing data to the template
        return render_template("edit_contracts.j2", data=data)

    if request.method == "POST":
        # if user hits update contract
        if request.form.get("Update_Contract"):
            # gets user input
            client_name = request.form["client_name"]
            contract_amount = request.form["contract_amount"]

             # if contract amount is NULL
            if contract_amount == '' or contract_amount == '0':
                query = "UPDATE Contracts SET Contracts.client_name = %s, Contracts.contract_amount = NULL WHERE Contracts.contract_id = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (client_name, contract_id))
                mysql.connection.commit()


            # inserts into table
            else:
                query = "UPDATE Contracts SET Contracts.client_name = %s, Contracts.contract_amount = %s WHERE Contracts.contract_id = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (client_name, contract_amount, contract_id))
                mysql.connection.commit()

            # back to page
            return redirect("/contracts")

@app.route('/departments', methods=["POST", "GET"])
def departments():
    if request.method == "POST":
        # if the user hits create Department
        if request.form.get("add_department"):
            # grab inputted information
            department_name = request.form['department_name']
            employee_count = request.form['employee_count']
            location_id = request.form['location_id']
            

            # inserts into table
            query = "INSERT INTO Departments (department_name, employee_count, location_id) VALUES  (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (department_name, employee_count, location_id))
            mysql.connection.commit()

            # return to page
            return redirect("/departments")

    if request.method == "GET":
        # Grab Department data so we send it to our template to display
        query = "SELECT Departments.department_id as ID, Departments.department_name as 'Department Name', Departments.employee_count as 'Department Count', Departments.location_id as 'Location ID' FROM Departments INNER JOIN Locations ON Departments.location_id = Locations.location_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()


        query2 = "SELECT location_id FROM Locations"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        location_data = cur.fetchall()

        return render_template("/departments.j2", data=data, location=location_data)
   

@app.route('/locations', methods=["POST", "GET"])
def locations():
    if request.method == "POST":
        # if the user hits create job
        if request.form.get("add_location"):
            # grab inputted information
            street_address = request.form["street_address"]
            city = request.form["city"]
            state = request.form["state"]
            postal_code = request.form["postal_code"]
            country = request.form['country']

            # inserts into table
            query = "INSERT INTO Locations (street_address, city, state, postal_code, country) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (street_address, city, state, postal_code, country))
            mysql.connection.commit()

            # return to page
            return redirect("/locations")

    if request.method == "GET":
        # Grab Jobs data so we send it to our template to display
        query = "SELECT Locations.location_id as ID, Locations.street_address as 'Street Address', Locations.city as 'City', Locations.state as 'State', Locations.postal_code as 'Postal Code', Locations.country as 'Country' FROM Locations"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("/locations.j2", data=data)

@app.route('/employee-contracts',  methods=["POST", "GET"])
def employee_contracts():
    if request.method == "POST":
        # if the user hits create employee-contract
        if request.form.get("add_employee-contracts"):
            # grab inputted information
            contract_id = request.form["contract_id"]
            employee_id = request.form["employee_id"]

            # inserts into table
            query = "INSERT INTO EmployeeContracts (contract_id, employee_id) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (contract_id, employee_id))
            mysql.connection.commit()

            # return to page
            return redirect("/employee-contracts")

    if request.method == "GET":
        # Grab EmployeeContracts data so we send it to our template to display
        query = "SELECT EmployeeContracts.contract_id as 'Contract ID', EmployeeContracts.employee_id as 'Employee ID' FROM EmployeeContracts INNER JOIN Contracts ON EmployeeContracts.contract_id = Contracts.contract_id INNER JOIN Employees ON EmployeeContracts.employee_id = Employees.employee_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT contract_id FROM Contracts"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        contract_data = cur.fetchall()

        query3 = "SELECT employee_id FROM Employees"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        employee_data = cur.fetchall()

        return render_template("/employee-contracts.j2", data=data, contract=contract_data, employee=employee_data)

@app.route('/delete_employeecontracts/<int:contract_id>/<int:employee_id>')
def delete_employeecontracts(contract_id, employee_id):
    # mySQL query to delete contract with given id
    query= "DELETE FROM EmployeeContracts WHERE contract_id = %s AND employee_id = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (contract_id, employee_id))
    mysql.connection.commit()

    # return to page
    return redirect("/employee-contracts")



# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 56667)) 
    
    app.run(port=port, debug=True)

