''' class cotaining the bike rent attributes '''

class BikeRent:
    stock = 100

    '''Class  constructor'''

    def __init__(self,
                 inv):   #confused with the indentation part
        self.inv = inv

    '''
    Hourly rate function
    '''

    def bikeonhourly(self,
                     N, HR):
        """Takes number of bikes and no of hours"""
        self.N = N
        self.HR = HR
        return N*HR*5

    '''
    Daily rate function
    '''

    def bikeondaily(self,
                    N, DAY):
        """Takes number of bikes and no of days"""
        self.N = N
        self.DAY = DAY
        #BikeRent.stock=BikeRent.stock-n
        return N*DAY*20

    '''
    Weekly rate function
    '''

    def bikeonweekly(self,
                     N,
                     WEEK):
        """Takees number ofbikes and no weeks"""
        self.N = N
        self.WEEK = WEEK
        #BikeRent.stock=BikeRent.stock-n
        return N*WEEK*60

print("The number of bikes available is : 100")

print("Rent bikes on hourly basis $5 per hour.")

print("Rent bikes on daily basis $20 per day.")

print("Rent bikes on weekly basis $60 per week.")

X = int(input("Enter the number of bikes you want "))

OBJ = BikeRent(X)

if X > 100:
    print("Only 100 bikes are available , Enter a number less than 100 ")
else:
    ITEM = input("Enter hourly or daily or weekly ")
    if ITEM == "hourly":
        THR = int(input("Enter number of hrs you want the bike for "))
		# works with hr inplace of thr
        C = OBJ.bikeonhourly(X, THR)
        print("Your Total amount is : Rs", C)
    elif ITEM == "daily":
        TDY = int(input("Enter the number of days you want the bike for "))
		#works with inplace of tdy
        C = OBJ.bikeondaily(X, TDY)
        print("Your Total amount is : Rs", C)
    elif ITEM == "weekly":
        TWE = int(input("Enter the number of weeks you want the bike for "))
		#also works with week inplace of twe
        C = OBJ.bikeonweekly(X, TWE)
        print("Your Total amount is : Rs", C)
    else:
        print("Give a valid response ")
