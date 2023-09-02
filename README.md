# Home Finance

A nifty web app to keep track of my home's monthly expenses and some personal utility.

## Tech stack

1. Django
2. PostgreSQL
3. Bootstrap

Developed and hosted on Raspberry Pi 4

## Features

* Multi account support for family members and shared payment information records for each bill
* Monthly fixed bills records plus bill adjustments
* Personal expenses records
* Personal TODO list

## Setup Locally

1. Install requirements:
   
   ```shell
   pip install -r requirements.txt
   ```
2. To configure your database, you can use the [`creds`](./creds) directory. For example to add PostgreSQL, create a copy of [`sqlite_db.py`](./creds/sqlite_db.py) rename to something like `postgresql_db.py`. Edit the file with proper credentials. After that, update the [`settings.py`](./home_fin/settings.py) file accordingly by importing the credentials and editing the `DB` variable.

## Screenshots

### Dashboard

![dashboard](./readme_statics/dashboard.jpg)


### Bill paymenet or adjustments


![bill_payment](./readme_statics/payment_page.jpg)
Pay Bills


![bill_adjust](./readme_statics/bill_adjust_page.jpg)
Adjust Bills

### Personal Expense

![personal_expense](./readme_statics/personal_expense_page.jpg)


![category](./readme_statics/add_catagory.jpg)
Create categories too!

### Todo Lists

![todo_lists](./readme_statics/todo_lists.jpg)
Create separate lists

Add tasks and mark/unmark tasks!

![todos](./readme_statics/todos.jpg)

