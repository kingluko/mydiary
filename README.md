

# My- Diary
This is an Andela Bootcamp Challenge that provides a platform in which users can pen down their thoughts and feelings
# Contains
This project contains the following endpoints for the API

| **Endpoint** | **Functionality** |

| **POST /auth/signup** | Create an account |

| **POST /auth/signin** | Login a user |

| **GET /entries** | Fetch all entries |

| **GET /entries/<entryId>** | Fetch a single entry |

|**POST /entries**| Create an entry |

| **PUT /entries/<entryId>** | Modify an entry |

| **DELETE /entries/<entryId>** | Delete an Entry|

# Prereqisites

- Python3 (A programming language)
- Flask (A Python microframework)
- Virtualenv (Stores all dependencies used in the project)
- Pivotal Tracker (A project management tool)
- Pytest (Tool for testing)
- Postresql (Database)

# Installation
Clone the repository<br>
`git clone https://github.com/kingluko/my-diary.git`<br>
Create a virtual environment<br>
`virtualenv --python=python3 yourenvname`<br>
Install the requirements within the virtual environment<br>
`pip install -r requirements.txt`<br>
Access Postgres via command prompt<br>
`sudo -i -u postgres`<br>
Create Database on postgresql<br>
`- psql -c 'CREATE DATABASE "<yourdatabasename>";' -U postgres`<br>
Create a user to access the database <br>
`- psql -c "CREATE USER <yourusername> WITH PASSWORD '<yourpassword>' createdb;" -U postgres`<br>
Create a .env file and input configurations to the environment<br>
```
# Database Exports
export DATABASE_NAME="<yourdatabasename>"
export DATABASE_USER="<yourusername>"
export DATABASE_PASSWORD="<yourpassword>"
export DATABASE_HOST="localhost"
export SECRET="<yoursecretword>"

# App Exports
export APP_SETTINGS="development"
export APP_TESTING="testing"
```
Export environments <br>
`source .env`<br>
Create tables for the database on python<br>
`python database.py`<br>
Run the program<br>
`python run.py`<br>
View on postman<br>
`http://127.0.0.1/api/v1/<endpoint>`<br>

# Heroku
The app is live on heroku with the link below:<br>
https://my-diary-v2.herokuapp.com/api/v1