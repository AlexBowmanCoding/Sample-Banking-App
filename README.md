# Banking database software (Title WIP)

## This allows communication between a banking front end and the database. 



| Endpoint                    	| Method 	| JSON Parameters                                            	| Description                          	|
|-----------------------------	|--------	|------------------------------------------------------------	|--------------------------------------	|
| ''                          	| create  	| username: str, password: str, email: str                   	| Creates a new user                   	|
| /<int:id>                   	| show   	|                                                             	| Shows a user                         	|
| ''                          	| index 	|                                                             	| Shows all users                   	|
| /<int:id>                   	| delete 	|                                                               | Deletes a User                     	|
| /<int:id>/balance             |get_balance|                                                              	| Gets user's balance                 	|
| /<int:id>/balance/add         | deposit 	| amount:int              	                                    | Deposits money into balance          	|
| /<int:id>/balance/minus       | withdraw	| amount:int                                                  	| Withdraws money from balance      	|










With input from a friend the project has these small quality of life details like if a current password isnt correct when changing password it returns 401 instead of 400. Stuff like that really helped shape this project.

I chose ORM because i still didnt fully understand it so i wanted to learn it and I did.





## How To Setup locally:

1. Create virtual environment

2. Set python interpreter to virtual environment

3. Connect database in __init__.py in the src folder uner SQLALCHEMY_DATABASE_URI

4. Install requirements.txt

5. Run "Export FLASK_APP=src/\_\_init__.py"

6. Run "Flask Run"


## How to run in Docker 

1. docker compose up --build




## How To Test App

1. Install Insomina 

2. Hit the create button and import from file and select the inlcuded Insomina-config.yml

3. Select a test and hit the send button


