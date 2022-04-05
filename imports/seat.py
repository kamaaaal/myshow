class seat:
    def __init__(self,seat_no):
        self.no = seat_no
        self.booked_by = None

    def __str__(self):
        if self.booked_by == None:
            return str_seat(self.no)
        else :
            return 'BD'
    
    def book(self,user):
        self.booked_by = user

# helper function to print seat within two digits 
def str_seat(no):
    if len(no) == 3:
        if no[0] == '0':
            return no[1:]
        elif no[2] == '0':
            i1 = int(no[0])
            i2 = int(no[1])
            val = str(i1+i2)
            return val + no[2]
        else :
            return no
    else :
        return no
    

# helper funciton to cover user input to indices
def convert_seat(num):
    if len(num) == 2:
        if num[1] != 0 :
            row = int(num[0])
            column = int (num[1]) - 1  # decresing the second digit of int represented in string
            if row < 0 or row > 10 and column < 0 or column > 10:
                raise ValueError 
            return row,column 
        elif num[1] == 0:
            row = int(num[0]) - 1
            column = 9
            return row,column
    elif num == '100' :
        return 9,9
  


# a utility function which retunrs 2d hundered 100 seats
def seats():
    return [[seat(f'{x}{y}') for y in range(1,11) ] for x in range(0,10)]

print(str_seat('010'))