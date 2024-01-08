-- CS340 : Project Step 3 Draft DML SQL SCRIPT
-- Group 58 Name: Team 58
-- Title: Human Resources Management System
-- Members:
-- Alexa Ngo (ngoale@oregonstate.edu)
-- Peter Musgrove (pmusgrov@gmail.com)

-- -----------------------------------------------------
-- Page: `Employees`
-- -----------------------------------------------------
-- gets all employees and their jobs, departments, and locations 
SELECT Employees.employee_id, first_name, last_name, email, phone_number, Jobs.job_id AS job_id, salary_commission, 
    Departments.department_id AS department_id, Locations.location_id as location_id
    FROM Employees
        INNER JOIN Jobs
        ON job_id = Jobs.job_id
        INNER JOIN Departments
        ON department_id = Departments.department_id
        INNER JOIN Locations
        ON location_id = Locations.location_id

-- get one employee and their jobs, departments, and locations 
SELECT * FROM Employees
    WHERE employee_id = :employee_id_from_dropdown

-- gets all job ids for dropdown
SELECT job_id FROM Jobs

-- gets all department ids  for dropdown
SELECT department_id  FROM Departments

-- gets all location ids  for dropdown
SELECT location_id_id  FROM Locations

-- add a new employee
INSERT INTO Employees (first_name, last_name, email, phone_number, job_id, salary_commission, department_id, location_id)
    VALUES (:first_name_input, :last_name_input, :email_input, :phone_number_input, :job_id_from_dropdown, :salary_commission_input, 
    :department_id_from_dropdown, :location_id_from_dropdown)

-- delete an employee
DELETE FROM Employees WHERE employee_id = :employee_id_from_dropdown

-- update an employee
UPDATE Employees
    SET first_name = first_name_input, last_name = :last_name_input, email = :email_input, phone_number = :phone_number_input, 
    job_id = :job_id_from_dropdown, salary_commission = :salary_commission_input, department_id = :department_id_from_dropdown, 
    location_id = :location_id_from_dropdown
    WHERE employee_id = employee_id_from_dropdown

-- -----------------------------------------------------
-- Page: `contracts`
-- -----------------------------------------------------
-- get all contracts id, name, amount
SELECT Contracts.contract_id, client_name, contract_amount
    FROM Contracts

-- get one contract id, name, amount
SELECT * FROM Contracts
    WHERE contract_id = :contract_id_from_dropdown

-- add a new contract
INSERT INTO Contracts (client_name, contract_amount)
    VALUES (:client_name_input, :contract_amount_input)

-- delete a contract
DELETE FROM Employees WHERE contract_id = :contract_id_from_dropdown

-- update a contract
UPDATE Contracts
    SET client_name = :client_name_input, contract_amount = :client_name_input
    WHERE contract_id = :contract_id_from_dropdown

-- -----------------------------------------------------
-- Page: `departments`
-- -----------------------------------------------------
-- get all department id, name, count, location_id
SELECT Departments.department_id, department_name, employee_count, Locations.location_id AS locations
    FROM Departments
        INNER JOIN Locations
        ON locations = Locations.location_id

-- get one department id, name, amount
SELECT * FROM Departments
    WHERE department_id = :department_id_from_dropdown

-- add a new department
INSERT INTO Departments (department_name, employee_count, location_id)
    VALUES (:department_name_input, :employee_count_input, :location_id_from_dropdown)

-- delete a department
DELETE FROM Departments WHERE department_id= :department_id_from_dropdown

-- update a department
UPDATE Departments
    SET department_name = :department_name_input, employee_count = :employee_count_input, location_id = :location_id_from_dropdown
    WHERE department_id = :department_id_from_dropdown

-- -----------------------------------------------------
-- Page: `jobs`
-- -----------------------------------------------------
-- get all jobs start_date, end_date, job_id, department_id, location_id, salary, commission_eligible
Select start_date, end_date, Jobs.job_id, Departments.department_id AS department, Locations.location_id AS location, salary, 
    commission_eligible
    From Jobs
        INNER JOIN Departments
        on department = Departments.id
        INNER JOIN Locations
        on location = Locations.id 

-- get one job
SELECT * FROM Jobs
    WHERE jobs_id = :jobs_id_from_dropdown

-- add a new job
INSERT INTO Jobs (end_date, start_date, department_id, location_id, salary, commission_eligible)
    Values(:end_date_input, start_date_input, :department_id_from_dropdown, location_id_from_dropdown, salary_input, 
    commission_eligible_input)

-- delete a job
DELETE FROM Jobs WHERE job_id =:job_id_from_dropdown

-- update a job
UPDATE Jobs
    SET end_date = :end_date_input, start_date = :start_date_input, department_id = :department_id_from_dropdown, 
    location_id = :location_id_from_dropdown, salary = :salary_input, commission_eligible = :commission_eligible_input
    WHERE job_id = :job_id_from_dropdown

-- -----------------------------------------------------
-- Page: `locations`
-- -----------------------------------------------------
-- gets all locations, ids, address, city, state, postal code, country
SELECT Locations.id, street_address, city, state, postal_code, country

-- gets one location
SELECT * FROM Locations
    WHERE location_id = :location_id_from_dropdown

-- add a new location
INSERT INTO Locations (street_address, city, state, postal_code, country)
    VALUES(:street_address_input, :city_input, :state_input, :postal_code_input, :country_input)

-- delete a location
DELETE FROM Locations WHERE location_id =:location_id_from_dropdown

-- update a location
UPDATE Locations
    SET street_address = :street_address_input, city = :city_input, state = :state_input, postal_code = :postal_code_input, 
    country = :country_input
    WHERE location_id = :location_id_from_dropdown

-- -----------------------------------------------------
-- Page: `employee-contracts`
-- -----------------------------------------------------
-- gets all employee-contracts
SELECT Contracts.contract_id AS contracts, Employees.employee_id AS employees,
    FROM EmployeeContracts
        INNER JOIN Contracts
        ON contracts = Contracts.id
        INNER JOIN Employees
        ON employees = Employees.id