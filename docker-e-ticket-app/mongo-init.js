// Read the administrative username and password from the environment variables
var adminUsername = process.env.MONGO_INITDB_ROOT_USERNAME;
var adminPassword = process.env.MONGO_INITDB_ROOT_PASSWORD;

// Connect to the "admin" database to authenticate
var adminDB = db.getSiblingDB('admin');
adminDB.auth(adminUsername, adminPassword);

// Switch to the desired database (e.g., "eticket")
var eticketDB = db.getSiblingDB('eticket');

// Create the user with the desired username and password
eticketDB.createUser({
  user: "eticket",
  pwd: "eticket",
  roles: [{ role: "readWrite", db: "eticket" }]
});
