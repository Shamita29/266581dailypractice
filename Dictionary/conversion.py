_dict = {'SFID' : 266581 , 'Branch' : "CSE", 'Name' : "Shamita C"} 
_list = [1, 2, 3]
  
result = {}
for key, ele in zip(_list, _dict.items()):
    result[key] = dict([ele])
          
print(result) 