from doctest import debug_script
from enum import Enum

# enum class for payment
class Payment(Enum):
    credit = 'credit'
    debit = 'debit'
    cod = 'cod'    

payments = {
    Payment.credit : 'sbi kamal',
    Payment.debit :'sbidebitkamal',
    Payment.cod : None
}