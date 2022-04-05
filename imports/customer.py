from user import User
from payment import Payment 

class Customer(User):

    def __init__(self,name,mail,password) -> None:
        super().__init__(name,mail,password)
        self.is_admin = False
        # using enum payment class for payment
        self.payments = {
            Payment.credit.value : None,
            Payment.debit.value : None,
            Payment.cod.value : True,
        }
        # actions will be stored here  
        self.history = []
        self.last_payment_method = None

    # sets a card_value(a string) to one of the available payment method 
    def edit_payment(self,payment_type,card_value):
        if payment_type in self.payments:
            self.payments[payment_type] = card_value
            self.history.append(('edited payment',f'{payment_type} : {card_value}'))

        # raising exception is user entered an undefined payment method
        elif payment_type == 'cod':
            raise(Exception('cod payment cannot be changed'))

        else :
            raise(Exception('unsupported payment method'))