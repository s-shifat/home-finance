from .models import Bill
from datetime import datetime
from pytz import timezone

# Home Rent; Home Maid; Gas; Internet; Dish; Garbage; Electricity

TODAY = datetime.now(timezone('Asia/Dhaka'))
BILL_DATA = {
        'Home Rent': {
            'amount': 25000,
            'due_date': datetime(day=7, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
        },
        'Home Maid': {
            'amount': 2500,
            'due_date': datetime(day=13, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
        },
        'Gas': {
            'amount': 1450,
            'due_date': datetime(day=13, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
        },
        'Internet': {
            'amount': 1200,
            'due_date': datetime(day=13, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
        
        },
        'TV': {
            'amount': 400,
            'due_date': datetime(day=5, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
       
        },
        'Garbage': {
            'amount': 150,
            'due_date': datetime(day=3, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
      
        },
        'Electricity': {
            'amount': 1500,
            'due_date': datetime(day=13, month=TODAY.month, year=TODAY.year),
            'paid_amount': 0,
            'status': False,
            'clearance_date': None,
     
        },
}

def add_new_bills(model=Bill):
    for name, data in BILL_DATA.items():
        bill = Bill.objects.create(
                name=name,
                amount=data['amount'],
                paid_amount=data['paid_amount'],
                due_date=data['due_date'],
                status=data['status'],
                clearance_date=data['clearance_date']
        )

def get_bills(model=Bill):
    latest_bill = Bill.objects.filter(due_date__isnull=False).latest('due_date')
    latest_date = latest_bill.due_date
    new_month = (latest_date.month < TODAY.month) and (latest_date.year == TODAY.year)
    if new_month:
        add_new_bills(model)
    return model

