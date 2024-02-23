# MongoDB Cheat Sheet


This command is used to display a list of all available databases on your MongoDB server.\
`show dbs`

This command switches to the "test" database. If the "test" database doesn't exist, MongoDB will create it for you.\
`use test` 

This switches to the "new-db1" database. If it doesn't exist, MongoDB will create it.\
`use new-db1` 

Similarly, this command switches to the "new-db2" database.\
`use new-db2` 

 This command displays the current database you are using.\
`db`

Switch to the "book" database, or create it if it doesn't exist.\
`use book`  

Create the "book-info" collection.It is the equivalent of a table in a relational database\
`db.createCollection("book-info")`  

Insert documents into the "book-name" collection.MongoDB, a "document" is analogous to a record or row in a relational database.\
`db["book-info"].insertOne({ name: "Bangla", author: "Nazrul", price: "300Tk" })`.\
`db["book-info"].insertOne({ name: "English", author: "Nafiz", price: "200Tk" })`

Show collections in the current database.\
`show collections`

Sample documents to insert into the "book-info" collection.
```javascript
const booksToInsert = [
  { name: "Book1", author: "Author1", price: 20 },
  { name: "Book2", author: "Author2", price: 25 },
  { name: "Book3", author: "Author3", price: 30 }
];
```
Insert multiple documents into the "book-info" collection.\
`db["book-info"].insertMany(booksToInsert);`

Show the documents in the "book-info" collection.`pretty`is not mandatory, and it's more of a convenience for human readability.\
`db["book-info"].find().pretty();`\
`db["book-info"].find()`

Use `insertMany` when you want to insert multiple documents into the collection in a single operation.\

```javascript
db.getCollection("book-info").insertMany([
  { name: "Python", author: "Arif", price: 500 },
  { name: "Spring", author: "Khan", price: 600 }
]);
```
Query and display all documents in the "book-info" collection.\
`db.getCollection("book-info").find()`

Query and display all documents in the "book-info" collection.\
`db["book-info"].find().pretty();`

Find a book by name in the "book-info" collection.\
`db["book-info"].find({ name: "Python" })`

Find all books in the "book-info" collection.\
`db["book-info"].find().pretty();`

querying with the numeric value.\
`db["book-info"].find({ price: 600 })`

Find the first two documents in the "book-info" collection.\
`db["book-info"].find({}).limit(2)`

Update the price of the "Python" book in the "book-info" collection.\
`db["book-info"].updateOne({ name: "Python" }, { $set: { price: 550 } });`

Check price is updated, new price is 550.\
`db["book-info"].find({ name: "Python" })`

Update the price of books with a price less than 500 in the "book-info" collection.\
`db["book-info"].updateMany({ price: { $lt: 300 } }, { $set: { price: 500 } });`

Delete a document from the "book-info" collection.\
`db["book-info"].deleteOne({ name: "Python" });`

Delete books with a price greater than or equal to 600 in the "book-info" collection
`db["book-info"].deleteMany({ price: { $gte: 600 } });`

Drop the "book-info" collection
`db["book-info"].drop();`

Delete the "book" database.\
`use book;`  // Switch to the database you want to delete.\
`db.dropDatabase();`

Check the currently selected database.\
`db`

*In MongoDB, the **default unique identifier** for documents is the _id field. If you haven't explicitly provided a value for _id during the document insertion, MongoDB automatically generates a unique identifier for each document*

Retrieve documents in ascending order based on the "price" field.\
`db["book-info"].find().sort({ price: 1 })`

Retrieve documents in descending order based on the "price" field.\
`db["book-info"].find().sort({ price: -1 })`

*The *_id* values in the result should show the order in which the documents were inserted. While they are not strictly incremental integers, you'll likely notice that they are generally increasing based on the insertion order.*.\

*In MongoDB, the **countDocuments** method is used to count the number of documents that match a specified filter in a collection. It provides a way to get the count of documents based on certain criteria.*

Count all documents in the "book-info" collection in a single line.\
`print(`Total number of documents: ${db["book-info"].countDocuments()}`);`

Count documents in the "book-info" collection where the price is greater than 30 in a single line.\
`print(`Number of books with price greater than 30: ${db["book-info"].countDocuments({ price: { $gt: 30 } })}`);`


*In MongoDB, **projection** refers to the ability to specify which fields you want to include or exclude in the result set of a query. Projection allows you to control the shape of the data returned by a query, retrieving only the fields that are relevant to your application. This can be especially useful when working with large datasets or when optimizing network and memory usage.*

How It Works:
* If a field is included with a value of 1, it will be included in the result set.
* If a field is included with a value of 0, it will be excluded from the result set.
* If a field is not included or excluded, it will be included by default.

Include only the 'name' and 'price' fields in the result set.\
`db["book-info"].find({}, { name: 1, price: 1 })`

Exclude the 'author' field from the result set.\
`db["book-info"].find({}, { price: 0 })`

*In MongoDB, **aggregation** is the process of transforming and processing documents from a collection to produce a set of aggregated results. The aggregation framework provides a flexible and powerful way to perform data transformations, filtering, grouping, sorting, and other operations on documents.*

Here are the names of common MongoDB Aggregation Framework stages without descriptions.
```
$match
$group
$project
$sort
$limit
$skip
$unwind
$lookup
```

Here's a basic structure of the aggregate method:\
`db.collectionName.aggregate([stage1, stage2, ..., stageN])`

Create a Database and Collection.\
`use bookstore`

nsert Example Documents.
```
db["book-info"].insertMany([
  { name: "Book1", author: "Author1", price: 500 },
  { name: "Book2", author: "Author1", price: 300 },
  { name: "Book2", author: "Author2", price: 400 },
  { name: "Book3", author: "Author2", price: 600 },
  { name: "Book4", author: "Author1", price: 200 }
])
```
Run Aggregation Pipeline.\
`db["book-info"].aggregate([{ $match: { author: "Author1" } }, { $group: { _id: "$author", books: { $push: { name: "$name", price: "$price" } }, totalPrice: { $sum: "$price" } } }])`