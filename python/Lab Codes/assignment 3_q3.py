ini_dict = {'a':1,'b':1, 'c':2,'d':3} 
  
# printing initial_dictionary 
print ("initial dictionary", str(ini_dict)) 
  
# code to remove duplicates 
result = {} 
  
for key, value in ini_dict.items(): 
    if value not in result.values(): 
        result[key] = value 
          
print ("result", str(result)) 