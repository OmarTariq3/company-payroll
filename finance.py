from validators import InvoiceValidator, ValidationError
from inventory import Item, Book, Food


class Invoice:
    def __init__(self, invoice_id, validator: InvoiceValidator):
        self.invoice_id = invoice_id
        self.validator = validator
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @property
    def amount_to_pay(self):
        if not self.validator.validate(self):
            raise ValidationError("One of the invoices are invalid")
        return sum([item.price for item in self.items])

    def __repr__(self):
        return f"{self.__class__.__name__:<28}| {self.invoice_id:^15}| {len(self.items):>10}"

    def __lt__(self, other):
        if type(self) is not type(other):
            return self.__class__.__name__ < other.__class__.__name__

        return (self.invoice_id, len(self.items)) < (other.invoice_id, len(other.items))


class Payroll:
    def __init__(self):
        self.payables = []

    def add_payable(self, payable):
        self.payables.append(payable)

    @property
    def amount_to_pay(self):
        return sum([payable.amount_to_pay for payable in self.payables])

    def __repr__(self):
        self.payables.sort()
        return "\n".join([repr(payable) for payable in self.payables])
