-- CS340 : Project Step 2 Draft DDL SQL SCRIPT
-- Group 58 Name: Team 58
-- Title: Human Resources Management System
-- Members:
-- Alexa Ngo (ngoale@oregonstate.edu)
-- Peter Musgrove (pmusgrov@gmail.com)


SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- -----------------------------------------------------
-- Table `Employees`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Employees` ;

CREATE TABLE IF NOT EXISTS `Employees` (
    employee_id int NOT NULL AUTO_INCREMENT UNIQUE,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    phone_number varchar(50) NOT NULL,
    job_id int NOT NULL,
    salary_commission int NOT NULL,
    department_id int NOT NULL,  
    location_id int NOT NULL,    
    PRIMARY KEY (employee_id),
    FOREIGN KEY (department_id) REFERENCES Departments(department_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `Contracts`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Contracts`;

CREATE TABLE IF NOT EXISTS `Contracts` (
    contract_id int NOT NULL AUTO_INCREMENT UNIQUE,
    client_name varchar(50),
    contract_amount int, 
    PRIMARY KEY (contract_id)
);

-- -----------------------------------------------------
-- Table `EmployeeContracts`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `EmployeeContracts`;

CREATE TABLE IF NOT EXISTS `EmployeeContracts` (
    contract_id int NOT NULL,
    employee_id int NOT NULL, 
    PRIMARY KEY (contract_id, employee_id),
    FOREIGN KEY (contract_id) REFERENCES Contracts(contract_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `Jobs`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Jobs`;

CREATE TABLE IF NOT EXISTS `Jobs` (
    start_date datetime NOT NULL, 
    end_date datetime NOT NULL,
    job_id int NOT NULL AUTO_INCREMENT UNIQUE,
    department_id int NOT NULL, 
    location_id int NOT NULL, 
    salary int NOT NULL,
    commission_eligible TINYINT(1) NOT NULL,
    PRIMARY KEY (job_id),
    FOREIGN KEY (department_id) REFERENCES Departments(department_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `Departments`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Departments`;

CREATE TABLE IF NOT EXISTS `Departments` (
    department_id int NOT NULL AUTO_INCREMENT UNIQUE,
    department_name varchar(50),
    employee_count int NOT NULL,
    location_id int NOT NULL, 
    PRIMARY KEY (department_id),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `Locations`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Locations`;

CREATE TABLE IF NOT EXISTS `Locations` (
    location_id int NOT NULL AUTO_INCREMENT UNIQUE,
    street_address varchar(50) NOT NULL,
    city varchar(20),
    state varchar(20),
    postal_code char(5),
    country varchar(20),
    PRIMARY KEY (location_id)
);

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

-- Insert test data into Employees table
INSERT INTO Employees (first_name, last_name, email, phone_number, job_id, salary_commission, department_id, location_id) 
VALUES ('Brad', 'Pitt', 'bradPitt@movies.com', '888-888-8989', 2, 14324, 1, 1),
('Jennifer', 'Aniston', 'jenniferAniston@movies.com', '999-999-9912', 1, 3433, 2, 4),
('Arnold', 'Swatrz', 'arnoldSwartz@hotmail.com', '123-321-4342', 2, 4324, 1,3);

-- Insert test data into Contracts table
INSERT INTO Contracts (client_name, contract_amount)
VALUES ('Walmart', 83932102), ('Kroger', 32939211), ('Target', 43019323), ('Costco', 23238938);

-- Insert test data into EmployeeContracts table
INSERT INTO EmployeeContracts (contract_id, employee_id)
VALUES (1, 3), (2, 1), (3, 2), (4,3);

-- Insert test data into Jobs table
INSERT INTO Jobs (start_date, end_date, job_id, department_id, location_id, salary, commission_eligible)
VALUES (20230321, 20230717, 2, 1, 1, 80000, 0), (20230117, 20230717, 1, 2, 4, 60000, 1),
(20200114, 20230509, 3, 1, 3, 85000, 1);

-- Insert test data into Departments table
INSERT INTO Departments (department_name, employee_count, location_id)
VALUES ('Human Resources', 50, 2), ('Sales', 124, 4), ('Customer Service', 302, 1), ('IT', 22, 2);

-- Insert test data into Locations table
INSERT INTO Locations (street_address, city, state, postal_code, country)
VALUES ('2200 Mission College Blvd', 'Santa Clara', 'CA', 95052, 'USA'),
('110 Fulbourn Road', 'Cambridge', '', 'CB1 9NJ', 'United Kingdom'),
('2485 Augustine Drive', 'Santa Clara', 'CA', 95054, 'USA'),
('1 New Orchard Road Armonk', 'New York', 'NY', 10504, 'USA');

SET FOREIGN_KEY_CHECKS = 1;
COMMIT;

