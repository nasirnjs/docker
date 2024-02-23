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

`use eticket`

```
use eticket

db.createUser({
  user: "eticket",
  pwd: "eticket",
  roles: [{ role: "readWrite", db: "eticket" }]
})
```