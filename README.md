# DB_Project

## Tech Stack

- Python
- Flask
- Postgres SQL
- Pandas

## Architecture

The programming langauge which was chosen is python, this was done as it is easy to understand and takes away the pain of syntax as well as contains many compatible lbraries. As an extension of python Flask was used as the GUI, this consisted of a mix of both python code and html and css creating the front end. The way this project was desinged was with OOP in mind, hence there are many classes maintain a good level of abstraction, furthermore, the code is testbable using pytest, a framework which was implemented in order to test out the various functionalities of the program

## Compling and Running

- Python version 3.11.4
- Pip install
  - Pandas
  - SQLAlchemy
  - Psycopg2
  - Flask
  - Pytest
- Start a valid postgres instace through postgresadmin 4
- navigate to the db_actions fodler where you will find a connection string and insert your computer username in place of 'noeljohnson'
- make sure the user has valid permissions with the postgredadmin server
- Once all the dependencys have been fulfilled and postgres has been setup, enabling pytesting and naviagte to the test_handler file, here you will see the test test_create_table, once this script has been run the postgres instance will be populated
- next navigate to app.py and either run the file or type in python app.py once you are in the app directory, from there the app will start

## Work Distribution

Originally the team consisted of myself, anid, alwin, nora, and raven. However, while I started working on the project about 4 weeks in adavance my teamamates did not contribute to a single line prior till this sunday, as a reuslt I decieded to leave the group. As a result this is a list of the things I have completed. The UI, including all files found in templates and static, creation of the base schema using SQLAlechmy as well as any scripts to clean the data, consisting of all files found in the models directory, setting up the postgres server, and pushing data to it, this includes all files found in src. Furthermore integration between the front end and back end which are found in the app.py file. I wish to convey that in total I have over 24 hours of work and over 40 commits, I might not have been able to finish it all but i still hope I am able to receive a high grade and you can understand that it was difficult to implement this project from scratch by myself. Originally i was only in charge of managing the github, setting up the project, including stubbing out classes, overall architecture, implementing test, and finding a viable db and establishing a connection to it which would allow us to run our commands and pushing the data to it, wrote my own scripts for this, but ended up taking on everything else as well
