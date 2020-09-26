def catalogUpdate(catalog, updates):
    dic = {}
    res = []
    for i in range(len(catalog)):
        dic[catalog[i][0]] = catalog[i][1:]
    
    for i in range(len(updates)):
        key = updates[i][0]
        value = updates[i]
        if key not in dic:
            dic[key] = value[1:]
        else:
            for j in range(1, len(value)):
                if value[j] not in dic[key]:
                    dic[key].append(value[j])
                    
    for i in dic.keys():
        dic[i].sort()
        
    for i in dic.keys():
        res.append([i])
        
    res.sort()
    
    for i in range(len(res)):
        res[i] += dic[res[i][0]]
        
    return(res)
    
"""
catalog = [["Books", "Classics", "Fiction"],
           ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
           ["Grocery", "Beverages", "Snacks"],
           ["Snacks", "Chocolate", "Sweets"],
           ["root", "Books", "Electronics", "Grocery"]]
           
updates = [["Snacks", "Marmalade"],
           ["Fiction", "Harry Potter"],
           ["root", "T-shirts"],
           ["T-shirts", "CodeSignal"]]
        
catalogUpdate(catalog, updates) = [["Books", "Classics", "Fiction"],
                                   ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
                                   ["Fiction", "Harry Potter"],
                                   ["Grocery", "Beverages", "Snacks"],
                                   ["Snacks", "Chocolate", "Marmalade", "Sweets"],
                                   ["T-shirts", "CodeSignal"],
                                   ["root", "Books", "Electronics", "Grocery", "T-shirts"]]
                                   
"""
