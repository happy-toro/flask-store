# Flask Store Restful API
## Installation

```
+ python 3.9
+ Flask 2.0.1
+ Flask-JWT 0.3.2
+ Flask-RESTful 0.3.9
+ Flask-SQLAlchemy 2.5.1
```
## Description
+ provide endpoints to list, retreive, create, update and delete items and store

```
>    + GET `url/stores`
>    + GET `url/store/<<string:name>>`
>    + POST `url/store/<<string:name>>`
>    + DELETE `url/store/<<string:name>>`

>    + GET `url/items`
>    + GET `url/item/<<string:name>>`
>    + POST `url/item/<<string:name>>`
>    + DELETE `url/item/<<string:name>>`
```

+ Each stores (id, name) contains list of items (id, name, price, store_id)

+ Also includes endpoints to register the users (id, username, password)

+ The caller of the endpoints is required to authenticate via /auth endpoint whereby a JWT token will be assigned for subsequent calls to the rest of endpoints

## Implementation
+ The endpoints are implemented using **Python Flask** micro framework and **SQLite**
