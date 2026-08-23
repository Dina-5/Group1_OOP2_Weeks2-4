from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0: # Part D requirement
            print("Error: Amount must be greater than 0")
            return
        print(f"Charged N${amount:.2f} to credit card.")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            print("Error: Amount must be greater than 0")
            return
        print(f"Paid N${amount:.2f} via PayPal.")

class MobileMoneyPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            print("Error: Amount must be greater than 0")
            return
        print(f"Sent N${amount:.2f} via Mobile Money.")


# STEP 9: Test loop - ADD THIS
if __name__ == "__main__":
    payments = [CreditCardPayment(), PayPalPayment(), MobileMoneyPayment()]
    
    print("--- Testing Valid Payments ---")
    for method in payments:
        method.pay(100)
    
    print("\n--- Testing Invalid Payment ---")
    payments[0].pay(-50)  # Should show error