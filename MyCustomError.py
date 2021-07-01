class MyCustomError(Exception):
    def __init__(self, value):
        self.value = value
  

    def __str__(self):
        return(repr(self.value))
  
try:
    raise(MyCustomError(3*2))
  
# Value of Exception is stored in error
except MyCustomError as error:
    print('A New Exception occured: ',error.value)