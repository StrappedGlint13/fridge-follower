# User stories

| Done | Story  |
|:-----| :----------|
| x    | register MyFridge | 
| x    | login/logout |
| x    | edit your account |
| X    | add a product to the fridge |
| X    | list your fridge products |
| x    | delete your products in the fridge |
| x    | throw your products to the waste from the fridge
| x    | eat dishes from your fridge
| x    | explore your consumption
| x    | add dishes to the favorites
| x    | check your favorite dishes
| x    | all the users are able to see their consumption from the main page


# User stories SQL-queries

## Signing in not required:

### Seeing stats from the users

Users will see consumption stats from registered users of the app at the main page:

`SELECT Account.username,  SUM(Waste.amount) as wfood, SUM(Waste.price) as wprice, (SUM(Dish.amount) / (SUM(Waste.amount) + SUM(Dish.amount))) as usage FROM Waste
         	        LEFT JOIN Account ON Waste.account_id = Account.id
                    LEFT JOIN Product ON Product.account_id = Account.id
                    LEFT JOIN Dish ON Dish.account_id = Account.id
		            GROUP BY Account.id
                    ORDER BY Account.username ASC;`

### Register MyFridge 

User is able to make a new account: 

`INSERT INTO Account (id, date_created, date_modified, name, username, password) VALUES (?, ?, ?, ?, ?, ?);`

Before making a new user, the application will validate, if the account username is unique:

`SELECT * FROM Account WHERE Account.username = ?;` 


## Signing in required:

These sql-queries need _account_id_, which is defined as _current_user.id_, after signing in. 

### Add a product

User is able to add a product to the fridge:

`INSERT INTO Product (id, date_created, date_modified, name, amount, price, account_id), VALUES (?, ?, ?, ?, ?, ?);`


### List products

User can list hers/his products in alphabetical order:

`"SELECT * FROM Product"
                    JOIN Account ON Product.account_id = Account.id
                    WHERE Product.account_id = :account_id
		            ORDER BY Product.name ASC;`





