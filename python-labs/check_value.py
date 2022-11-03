def checkvalue(valuetocheck): 
    assert (valuetocheck.lstrip("-").isdigit() is True), "You must enter a number." 
    valuetocheck = int(valuetocheck)
    assert (valuetocheck > 0), "Value entered must be greater than 0" 
    if valuetocheck > 4: 
        print("Value is greater than 4") 

var = input("Enter a number greater than 0: ")
checkvalue(var)

