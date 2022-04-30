def dobcheck():
#To get this to work - go to the left and hit the box icon and import the python-dateutil package
  from dateutil.parser import parse
  from dateutil.relativedelta import relativedelta
  from datetime import datetime
#Obviously I just put the .capitalize in here to remind me that I could use it as a method on a string
  birth_date = parse(input('when were you born? '.capitalize()))
#The parse should put the birth date into a useable format
  now = datetime.now()

  difference = relativedelta(now, birth_date)
  print(
    f'Your age is: {difference.years} years, {difference.months} months and {difference.days} days'
)
