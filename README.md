# UserActivitydjango
API to describes a list of users and their corresponding periods of activity across multiple months, custom management command to populate the database with some dummy data

API Endpoint to serve the data in json format : http://ashishh87.pythonanywhere.com/

custom management command to populate the database :
To Populate the User Model (by default it will create 5 users): python manage.py populate_user
To Populate the ActivityPeriod Model(by defalut it will create 20 users) : python manage.py populate_activity

The populated data will be shown in json format in the above url i.e. : http://ashishh87.pythonanywhere.com/

To see the models data login at : http://ashishh87.pythonanywhere.com/admin

