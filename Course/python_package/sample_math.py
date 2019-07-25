
# coding: utf-8

# In[ ]:


def my_max(a):
    if not a:
         return None
    max_value = a[0] 
    for item in a:         
        if item > max_value:
            max_value = item
    return max_value
    

def my_min(a):
    if not a:
        return None  
    max_value = a[0] 
    for item in a:         
        if item < max_value:
            max_value = item
    return max_value



# def my_max(a):
#     if not a:
#         raise ValueError('列表裡不能有空值')
#     max_value = a[0] 
#     for item in a:         
#         if item > max_value:
#             max_value = item
#     return max_value