from employees import (
    HourlyEmployee,
    SalariedEmployee,
    CommissionSalariedEmployee,
    Volunteer,
)
from inventory import Book, Food
from validators import (
    MandatoryInvoiceValidator,
    CompleteInvoiceValidator,
)
from finance import Invoice, Payroll


class Company:
    def __init__(self):
        self.payroll = Payroll()

    def fill_data(self, is_mandatory_validator=True):
        self.payroll.add_payable(Volunteer("Most", "AddressV", 700))
        self.payroll.add_payable(HourlyEmployee("Belal", "AddressH", 1, 10, 3))
        self.payroll.add_payable(SalariedEmployee("Ziad", "AddressS1", 2, 3000))
        self.payroll.add_payable(SalariedEmployee("Ashraf", "AddressS1", 2, 3000))
        self.payroll.add_payable(
            CommissionSalariedEmployee("Safa", "AddressC1", 6, 2500, 0.001, 5000)
        )
        self.payroll.add_payable(
            CommissionSalariedEmployee("ahmed", "AddressC2", 6, 2500, 0.001, 5000)
        )

        if is_mandatory_validator:
            validator = MandatoryInvoiceValidator.get_instance()
        else:
            validator = CompleteInvoiceValidator.get_instance()
        invoice = Invoice(1234, validator)
        invoice.add_item(Book("book1", 10, 7, ""))
        invoice.add_item(Food("food1", 5, 6, ""))
        self.payroll.add_payable(invoice)


if __name__ == "__main__":
    company = Company()
    company.fill_data(True)  # Try with True

    print(company.payroll.amount_to_pay)  # 11840
    print(company.payroll)
