# MongoDB Install and basic CMD

**First Steps:** Install MongoDB shell mongosh **[From Here](https://www.mongodb.com/docs/mongodb-shell/install/)**, **mongosh** is the MongoDB Shell command-line interface. 

**Second Steps:** Install source **[MongoDB Shell](https://www.mongodb.com/try/download/shell)**

**Third Steps:** Download and Install MongoDB Compass **[MongoDB Compass](https://www.mongodb.com/try/download/compass)**

Connect to a MongoDB instance using the mongosh command-line tool. Default authentication database for the MongoDB mongosh shell is the "admin" database.\
`mongosh --username mongo_admin --password example --host localhost --port 27017`

Create DB, If iot_db doesn't exist, MongoDB will create iot_db database.\
`use iot_db`

Create the user with the desired username and password, and assign the necessary roles.\
```shell
db.createUser({
  user: "my-db",
  pwd: "Pass445S",
  roles: [{ role: "readWrite", db: "iot_db" }]
})
```
After creating the user, you can use show users again to confirm that the user has been added.\
`show users`

Connect `my-db` from mongo shell.\
`mongosh --username my-db --password Pass445S --host localhost --port 27017 --authenticationDatabase iot_db`

This command is used to display a list of all available databases on your MongoDB server.\
`show dbs`
