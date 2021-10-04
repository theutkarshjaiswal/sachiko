Create a python environment and install the requirements.py through pip

1 - python3 -m venv env #first move to your desired path
2 - source env/bin/activate #for linux and mac os
3 - pip3 intall -r requirements.txt
4 - python3 manage.py runserver
5 - open local host or go to http://127.0.0.1:8000/


super_user credentials (id = 'admin@example.com' , pass = 'admin')
test_user credentials (id = 'test@example.com' , pass = 'Password#11')


for the api--
1 - click on the user button at home page for list view only
2 - go to http://127.0.0.1:8000/transaction/3/  change the end of url to the id 
    for put,delete.