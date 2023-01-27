# DE Review Day

## Introduction

These tasks are designed to help you practice your problem solving with Python and TDD. There is also an element of SQL but this should not be the focus.
These are the things we will be looking for today:

-   Evidence of breaking a problem down
-   Good problem solving skills
-   Sensible project structure
-   Test Driven Development
-   Good Git practices
-   Excellent code standards (PEP8 compliant and well documented)

The tasks today are divided into sections, you do not need to finish all the sections and we encourage you to focus on the first.


**However keep in mind some of the later tasks will rely on previous tasks being completed - we will signpost this in the README**

## The Task

Northcoders has decided to open up a department store selling all manner of \"unique\" items! However as we've expanded our first attempt at a database has not been as useful as we'd like. We are struggling to analyse our sales, an important thing to do if we want to bring in the big bucks 💰🤑💰.

We have hired a professional to design our new database which should mean we are able to identify the best sellers and what isn't worth stocking.

Your job is to use the data taken from the first database and manipulate it to fit the schema set out in the second database. The schemas for both databases can be found below:

> First database: https://dbdiagram.io/d/63d0e842296d97641d7bf89e

> New database: https://dbdiagram.io/d/63d1184e296d97641d7c05d0



## Section 1: Data Manipulation


Your first job is to create 6 utility functions that will format the raw data ready to be inserted into the new database tables by the pg8000 module.

Make sure you are clear on what each functions arguments should be and the structure of the data that should be returned.

### Task 1 - Manipulate Department Data

The `format_departments` function should accept a list of dictionaries in the following format and return a list of lists containing the **department_name**.

```py
# EXAMPLE INPUT
[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
]

# OUTPUT
[['Beauty'], ['Footwear']]
```

### Task 2 - Manipulate Stock Data

The `format_stock` function should accept a list of dictionaries in the following format and return a list containing the **item_name** and the **amount**.

```py
# EXAMPLE INPUT
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
]

# OUTPUT
[['Louboutin Flip Flops', 5], ['Eau de Fromage', 10]]
```

### Task 3 - Manipulate Feature Data

The `format_features` function should accept a list of dictionaries in the following format and return a list of lists containing the **feature_name**.

> The returned list should only contain unique features!

```py
# EXAMPLE INPUT
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear', 'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
]

# OUTPUT
[['Designer'], ['Faux-Faux-Leather'], ['Fragrance']]
```

### Task 4 - Manipulate Staff Data

The format_staff function should accept a list of dictionaries representing staff data and a list of dictionaries representing the **new** department data.

It should return a list of lists containing the **first_name**, **last_name**, and the _correct_ **department_id**.

```py
# EXAMPLE INPUT
# Staff list
[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
]
# Department list
[
    {
        'department_id': 1,
        'department_name':'Beauty'
    }, {
        'department_id': 2,
        'department_name':'Footwear'
    }
]

# OUTPUT
[['Duncan', 'Crawley', 1], ['Cat', 'Hoang', 2]]
```

### Task 5 - Manipulate Stock_Feature Data

The `format_stock_feature` will need data from the following data structures:

-   a list representing the newly inserted stock data
-   a list representing the newly inserted feature data
-   a list representing the original stock data

_hint: you may want to break this problem down into multiple functions._

It should return a list of lists that containing **stock_id**, and **feature_id**.

> **Keep in mind that each product could have several features and as such there may be multiple of the same `stock_id` each with a different `feature_id`**

```py
# New stock data:
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'amount_in_stock':5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    }
]
# New feature data:
[
    {
        'feature_id':1,
        'feature_name':'Designer'
    },{
        'feature_id':2,
        'feature_name':'Faux-Faux-Leather'
    }
]
# Original stock data
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Designer'],
        'department': 'Beauty',
        'amount': 10
    }
]

# OUTPUT
[[1, 1], [1, 2], [2, 1]]
```

### Task 6 - Manipulate Sales Data

The final function, `format_sales`, should accept:

-   a list representing the newly inserted stock data
-   a list representing the newly inserted staff data
-   a list representing the original sales data

_hint: you may want to break this problem down into multiple functions._

It should return a list of lists containing the following:

-   item_id - should be the correct ID based on the items name in the items name
-   salesperson - should be the correct ID based on the name of the staff member
-   price
-   quantity
-   created_at

```py
# New stock data:
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops'.
        'amount_in_stock':5
    }
]
# New staff data:
[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department_id': 1
    }
]

# Original sales data:
[
    {
        "sales_id": 1,
        "item_name": "Louboutin Flip Flops",
        "salesperson": "Duncan Crawley"
        "price": 22.49,
        "quantity": 1,
        "created_at": "2023-01-03 10:34:56"
    }
]

# OUTPUT
[[1, 1, 22.49, 1, "2023-01-03 10:34:56"]]
```



## Section 2: Get Postgres Data



Before starting this section please run the `setup-db.sql` file with the following command:

```sh
psql -f setup-db.sql
```

This will create both databases and insert data into the first database ready for the following tasks.

### Task 1: Get Initial Data

You will need a way to access all the initial data from each of the three tables.

You should write a function (or functions) for this purpose.  The function should return the data as list of dictionaries where the keys align with the column titles (see the inputs for the functions in section 1).

> You may wish to use a data manipulation util function - if so this should be unit tested. However we do not need to test that the pg8000 module is working.

**THE NEXT SECTION RELIES ON SOME DATA BEING INSERTED FIRST - MOVE ONTO THE NEXT SECTION AND COME BACK WHEN YOU HAVE THE DATA YOU NEED INSERTED**

### Task 2: Get newly inserted data for the following tables:

-   `dim_feature`
-   `dim_stock`
-   `dim_department`
-   `dim_staff`



## Section 3: Insert Formatted Data



If you've made it this far well done! 🎉

The final thing to do is to bring together everything you've done so far and populate the new database.

Think about what you need to do and the order that you need to do those things in.

**Remember you may need to do part of the data insertion and then go back to Task 2 of Section 2 to use the new data**
