This is a custom budgeting program made by Jon Hull.
In order to use this application a MYSQL database must be set up.
I recommend using a separate linux machine to host the database.

Requirements.
A server with internet access. Must have sudo privledges.
Access to the router or switch to set up port forwarding.

The database can be set up as follows assuming you are using ubuntu.

# insall mysql-server
sudo apt install mysql-server

# verify installation 
mysql --version 

# start mysql server
sudo systemctl start mysql

no output means success

# run on startup
sudo systemctl enable mysql

# set up mysql server
sudo mysql_secure_installation

set a password strength level. I choose 1 = MEDIUM

set root password

# create database
create database $db_name
-- replace $db_name with whatever name you want the database to be called

# create tables
use $db_name
create table budget (
  id int not null auto_increment,
  variable_input_id int,
  value decimal(12,2),
  primary key(id)
);
create table variable_input_types (
  id int not null auto_increment,
  name varchar(32),
  primary key(id)
);
create table variable_input_types (
  id int not null auto_increment,
  month int,
  variable_input_id int,
  comment varchar(256),
  date date,
  value decimal(12,2),
  primary key(id)
);


# create user
create user $u_name@`%` identified by 'pass'
-- replace $u_name with username
-- `%` allows this user to access from any IP this will allow the user to access from outside the local network
-- replace pass with password

# grant privileges
grant insert, select on $db_name.*  

