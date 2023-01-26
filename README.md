# DE Review Day

## Introduction

These tasks are designed to help you practice your problem solving with Python and TDD. There is also an element of SQL but this should not be the focus. It should hopefully help you solidify what you've learnt before we move onto Cloud computing next week.

The tasks today are divided into sections, you do not need to finish all the sections and we encourage you to focus on the first.

Once you've completed the first two sections you can move onto section 3 and onwards.

**However keep in mind some of the later tasks will rely on previous tasks being completed - we will signpost this in the README**


## The Task

Northcoders has decided to open up a department store selling all manner of \"unique\" items! However as we've expanded our first attempt at a database has not been as useful as we'd like. We are stuggling to analyse our sales, an important thing to do if we want to bring in the big bucks 💰🤑💰.

We have hired a professional to design our new database which should mean we are able to identify the best sellers and what isn't worth stocking.

Your job is to use the data taken from the first database and manipulate it to fit the schema set out in the second database. The schemas for both databases can be found below:

> First database: https://dbdiagram.io/d/63d0e842296d97641d7bf89e

> New database: https://dbdiagram.io/d/63d1184e296d97641d7c05d0


---

## Section 1: Data Manipulation

Your first job is to create 6 functions that when given certain data will return formatted data in a manner that can be inserted into the new database tables by the PG8000 module.

Make sure you are clear on what each functions arguments should be and the structure of the data that should be returned.


### Task 1 - Manipulate Department Data

The `format_departments` function should accept a list of dictionaries in the following format and return a list of lists containing the **department_name**.

```py
# INPUT
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
# INPUT
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
# INPUT
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

It should return a list of lists containing the **first_name**, **last_name**, and the *correct* **department_id**.

```py
# INPUT
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
The `format_stock_feature` function should accept:
- a list representing the newly created stock data
- a list representing the newly created feature data
- a list representing the original stock data

It should return a list of lists that containing **stock_id**, and **feature_id**.

> **Keep in mind that each product could have several features and as such there may be multiple of the same `stock_id` each with a different `feature_id`**

```py
# INPUT

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

- a list representing the newly created stock data
- a list representing the newly created staff data
- a list representing the original sales data

It should return a list of lists containing the following:
- item_id - should be the correct ID based on the items name in the items name
- salesperson - should be the correct ID based on the name of the staff member
- price
- quantity
- created_at

```py
# INPUT
# New stock data:
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops'.
        'amount_in_stock':5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    }
]
# New staff data:
[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department_id': 1
    }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department_id': 2
    }
]

# OUTPUT
[[1, 1], [1, 2], [2, 1]]
```

## Section 2: Get Postgres Data

### Task 1: Get Initial Data

You will need a way to access all the initial data from each of the three tables. 

You should write a function (or functions) for this purpose. And the return value of getting the data from a table should be a list of dictionaries. The keys on each dictionary should be the relevant column name for each value in a row.

> You may wish to using a dtat manipulation util function - if so this should be unit tested. However we do not ne to test that the PG8000 module is working.

**THE NEXT SECTION RELIES ON SOME DATA BEING INSERTED FIRST - MOVE ONTO THE NEXT SECTION AND COME BACK WHEN YOU HAVE THE DATA YOU NEED INSERTED**

### Task 2: Get newly inserted data for the following tables:
- `dim_feature`
- `dim_stock`
- `dim_department`
- `dim_staff`


## Section 3: Insert Formatted Data 
