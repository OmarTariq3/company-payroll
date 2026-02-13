from abc import ABC, abstractmethod


class ValidationRule(ABC):
    @abstractmethod
    def is_valid_rule(self, invoice):
        pass


class TaxesVaidationRule(ValidationRule):
    def is_valid_rule(self, invoice):
        print("Validating TaxesVaidationRule")
        return True


class SuppliersDealsVaidationRule(ValidationRule):
    def is_valid_rule(self, invoice):
        print("Validating SuppliersDealsVaidationRule")
        return False


class InvoiceValidator:
    def __init__(self, rules):
        self.rules = rules

    def validate(self, invoice: ValidationRule):
        if not self.rules:
            raise ValueError("Zero rules list.")

        for rule in self.rules:
            if not rule.is_valid_rule(invoice):
                return False
        return True


class MandatoryInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rules = [TaxesVaidationRule()]
        return MandatoryInvoiceValidator(rules)


class CompleteInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rules = [TaxesVaidationRule(), SuppliersDealsVaidationRule()]
        return MandatoryInvoiceValidator(rules)


class ValidationError(BaseException):
    pass
