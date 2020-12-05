from datetime import datetime
from decimal  import Decimal

class title_data:
    def __init__(self):
        self.title             = "title"
        self.budgeted          = Decimal(0)
        self.spent             = Decimal(0)
        self.remaining         = Decimal(0)
        self.variable_input_id = 0
        self.month             = 0
        self.year              = 0

class entry:
    def __init__(self):
        self.c = ""
        self.d = datetime.now().date()
        self.a = 0
