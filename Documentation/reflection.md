# Reflection and thoughts

- The application is mostly like I planned, but there are much more potential to make more SQL-queris to show more data and in addition to make it more accessible for the user. 

- There are some copy-paste -code with "dish" and "waste" -tables. I wanted to distribute the products consumption to the thrash and to the stomach, so I needed two separate datatables for that and did not find better ways to do so. 

- In the usage-folder there are dish and waste -classes as mentioned above. The "favorites"-connection table is also in the usage-folder. Dish and waste could be in a different folders, but I thought that because Dish and Waste -datatables are handling sort of the same area in the database, this might be a logical solution. 

- The "favorites" -datatable is depending on dishes and account. It is working as a connection table for the application, but favorites could be own datatable as well. This could be a bit more reasonable, as if user likes to delete his/hers dish, the favorite is alo beeing deleted in the process currently. However, deleting dishes/wastes from the usage is not recommended, as this affects to the data that is showed on the main page. 

## normalization and choises about denormalization

The database is normalized, as it is satisfying the 3 normalization phases. There could be a solution to add a certain dish/waste into one row, only growing its amount and price to make datatable more readable and less data repeting itself. Nevertheless, I chose denormalize the data, as there is more information to user _when_ certain amounts of certain product is eaten. This  make some repetitive data naturally. 