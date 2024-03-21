# React

-----frontend dev--------


-----frontend production------
npm install
npm run build
npm start

------for backend dev---------
yarn 
yarn run dev

--------for backend production------
yarn
yarn run build
yarn start


## Connect to mongo then create application database,user,password and import data

`mongosh --username mongo_admin --password NasirMango --host localhost --port 27017`

Create Database via CLI or there is also have `mongo-init.js` initialization scrip create database during boot.\
`use eticket`

```bash
use eticket

db.createUser({
  user: "eticket",
  pwd: "eticket",
  roles: [{ role: "readWrite", db: "eticket" }]
})
```
---

Lists all the databases present in your MongoDB instance.\
`show dbs;`

Switches to the "eticket" database.\
`use eticket;`

Lists all the collections present in the current database.\
`show collections;`

Retrieves all documents from the "users" collection in the current database.\
`db.users.find()`

Inserts a new document into the "users" collection.\
```bash
db.users.insertOne({
  name: "Md Nasir Uddin",
  email: "nasir@gmail.com",
  password: "123456",
  role: "user",
})
```