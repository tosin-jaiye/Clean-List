def clean_list(num):
    top_list = []
    i = 0

    while i < len(num):
        if num[i] == 0:
            top_list = top_list
        else: 
            top_list.append(num[i])
        i += 1

    return top_list

print (clean_list([4, 1, 7, 6, 7]))
        
    
