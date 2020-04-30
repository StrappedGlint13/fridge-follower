# User stories

| Done | Story  |
|:-----| :----------|
| x    | register MyFridge | 
| x    | login/logout |
| x    | edit your account |
| x    | delete your account | 
| x    | add a product to the fridge |
| x    | list your fridge products |
| x    | delete your products from the fridge |
| x    | throw your products to the waste from the fridge
| x    | eat dishes from your fridge
| x    | add dishes to the favorites
| x    | explore your favorite dishes
| x    | delete dishes/waste permanently
| x    | all the users are able to see their consumption from the main page


# SQL-queries fo User stories and CREATE TABLE -statements

## Signing in not required:

### Seeing stats from the users

Users will see consumption stats from registered users of the app at the main page:

`SELECT Account.username, Account.date_created,  SUM(Waste.amount) as wfood, SUM(Waste.price) as wprice, (SUM(Dish.amount) / (SUM(Waste.amount) + SUM(Dish.amount))) as usage FROM Waste
         	        LEFT JOIN Account ON Waste.account_id = Account.id
                    LEFT JOIN Dish ON Dish.account_id = Dish.id
		            GROUP BY Account.id
                    ORDER BY usage DESC;`

### Register MyFridge 

User is able to make a new account: 

`INSERT INTO Account (id, date_created, date_modified, name, username, password) VALUES (?, ?, ?, ?, ?, ?);`

Before making a new user, the application will validate, if the account username is unique:

`SELECT * FROM Account WHERE Account.username = ?;` 

### Sign in 

User is able to sign in:

`SELECT * FROM Account WHERE username = ? AND password = ?;`

## Signing in required:

These sql-queries need _account_id_, which is defined as _current_user.id_, after signing in. 

### Add a product

User is able to add a product to the fridge:

`INSERT INTO Product (id, date_created, date_modified, name, amount, price, account_id) VALUES (?, ?, ?, ?, ?, ?);`


### List products from the fridge

User can list hers/his products in alphabetical order:

`"SELECT * FROM Product"
                    JOIN Account ON Product.account_id = Account.id
                    WHERE Product.account_id = ?
		            ORDER BY Product.name ASC;`

### Delete products from the fridge

User can delete products:

`DELETE FROM Product WHERE product_id = ?;`

### Eat dishes from your fridge

User is able to eat dishes from the fridge products:

- First the amount of the eaten product should be updated:

`UPDATE Product SET amount = ? WHERE Product_id = ?;`

- Then, new dish can be made with: 

`INSERT INTO Dish (id, date_created, date_modified, name, amount, price, account_id), VALUES (?, ?, ?, ?, ?, ?);`

### Show your consumption of food

User can explore his/her consumption from two tables at this scene:

- Waste: `SELECT Waste.id, Waste.name, Waste.amount, Waste.price, Waste.date_created FROM Waste
                     JOIN Account ON Waste.account_id = Account.id
                     WHERE Waste.account_id = ?
             ORDER BY Waste.date_created DESC`

- Dishes: `Dish.id, Dish.name, Dish.amount, Dish.price, Dish.date_created FROM Dish
                     JOIN Account ON Dish.account_id = Account.id
                     WHERE Dish.account_id = :account_id
             ORDER BY Dish.date_created ASC`

### Add dishes to the favorites

User is able to add dishes to the favorites with _dish_id_ and _account_id_ foreign keys:

`INSERT INTO favorites (dish_id, account_id) VALUES (?, ?);`

Before adding new favorite food, app will check if dish is already added to the database:

`SELECT favorites.dish_id, favorites.account_id FROM favorites"
                    WHERE favorites.account_id = ? AND favorites.dish_id = ?;`


### Explore your favorite dishes

User can explore favorite dishes in alphabetical order:

`SELECT DISTINCT Dish.name, Account.id FROM Dish
                    LEFT JOIN favorites ON favorites.dish_id = Dish.id
                    LEFT JOIN Account ON Dish.account_id = Account.id
                    WHERE Dish.account_id = ?
            		ORDER BY Dish.name ASC;`

### Delete your account permanently

User is able to delete his/hers account by clicking _delete user_ - this will delete all data from the database:

`DELETE FROM Account WHERE account_id = ?`
`DELETE FROM Product WHERE account_id = ?`
`DELETE FROM Dish WHERE account_id = ?`
`DELETE FROM Waste WHERE account_id = ?`
`DELETE FROM favorites WHERE dish_id = ? AND account_id = ?`

## CREATE TABLE -SENTENCES

Location: application/auth

`CREATE TABLE account (
    id INTEGER NOT NULL, 
    date_created DATETIME, 
    date_modified DATETIME, 
    username VARCHAR(144) NOT NULL, 
    password VARCHAR(144) NOT NULL, 
    email VARCHAR(144) NOT NULL, 
    PRIMARY KEY (id)
)`

Location: application/usage

`CREATE TABLE dish (
    id INTEGER NOT NULL, 
    date_created DATETIME, 
    date_modified DATETIME, 
    name VARCHAR(144) NOT NULL, 
    amount FLOAT NOT NULL, 
    price FLOAT NOT NULL, 
    account_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
)`

`
CREATE TABLE waste (
    id INTEGER NOT NULL, 
    date_created DATETIME, 
    date_modified DATETIME, 
    name VARCHAR(144) NOT NULL, 
    amount FLOAT NOT NULL, 
    price FLOAT NOT NULL, 
    account_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
)
`

`
CREATE TABLE favorites (
    dish_id INTEGER, 
    account_id INTEGER, 
    FOREIGN KEY(dish_id) REFERENCES dish (id) ON DELETE CASCADE, 
    FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
)
`

Location: application/products

`CREATE TABLE product (
    id INTEGER NOT NULL, 
    date_created DATETIME, 
    date_modified DATETIME, 
    name VARCHAR(144) NOT NULL, 
    amount FLOAT NOT NULL, 
    price FLOAT NOT NULL, 
    account_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
)
`











