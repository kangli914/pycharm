payRate =29
hours = 40
tax = 13.5
empName =  " Sarah"
payRate, hours, tax, empName = 29, 40, 13.5, "Sarah"
grossPay = payRate* hours
netPay=grossPay - (grossPay*tax /100)
#print ('The pay rate is' payRate, ', The deducuted tax is', tax,'%', 'The grossPay is', grossPay, ', The net pay is', \,' The employee name is', empName)
print ('the pay rate is',   payRate)
print ('the pay rate is',   payRate, sep=' ')
print ('the pay rate is',   payRate, sep=',')