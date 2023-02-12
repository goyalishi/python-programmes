celcius=float(input('Enter the temperature in celcius'))
farheneit=float(input('Enter the temperature in farheneit'))
farh=celcius*1.8+32
cel=(farh-32)*0.55
print("%0.2f in celcius=%0.2f in farheneit"%(celcius,farh))
print("%0.2f in farheneit=%0.2f in celcius"%(farheneit,cel))
