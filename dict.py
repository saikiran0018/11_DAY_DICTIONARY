# a={}
# print(type(a))                                 # <class 'dict">

# a={45}
# print(type(a))                                  # <class 'set'>

# a={45:'python'}                                 # <class 'dict'>
# print(type(a))
# print(a[45])                                    # python

# book={
# 1:"python programming",
# 2:"core python programming",
# 3:"advance python programming"    
# }
# print(book[3])                                   # advance python programming
# print(book[10])                                   # key error

# a={1:123,2:'python',3:6.12,4:(1,2,3),5:[1,2,3],6:{1,2,3},7:{1:"chai"},8:""}
# print(a[1],type(a[1]))                           # 123 <class 'str'>
# print(a[8],type(a[8]))                                #   <class 'str'>
# print(a[7],type(a[8]))                                     # <class 'str'>
# print(a,type(a))                     # {1:123,2:'python',3:6.12,4:(1,2,3),5:[1,2,3],6:{1,2,3},7:{1:"chai"},8:""}<class'dict'>
# print(a.keys())                       # dict_keys([1,2,3,4,5,6,7,8])
# print(a.values())                     # ([123,"pytho",6.12,(1,2,3),[1,2,3],{1,2,3},{1:'chai},""])
# print(a.items())                      # ([(1,123),(2,"python"),(3,6.12),(4,(1,2,3)),(5,[1,2,3]),(6,{1,2,3}),(7,{1:'chai'}),(8,"")])
# a.clear()
# print(a)                                 # {}

# a=[101,102,103,104,105]
# b=dict.fromkeys(a)
# print(b,type(b))                        # {101: None, 102: None, 103: None, 104: None, 105: None} <class 'dict'>
# print(dict.fromkeys(a,"sai"))           # {101: 'sai', 102: 'sai', 103: 'sai', 104: 'sai', 105: 'sai'}

# a={1:123,2:'python',3:6.12,4:(1,2,3),5:[1,2,3],6:{1,2,3},7:{1:"chai"},8:""}
# print(a.get(3))                              # 6.12
# print(a.get(10))                              # none
# a.pop(4)
# print(a)                                 # {1: 123, 2: 'python', 3: 6.12, 5: [1, 2, 3], 6: {1, 2, 3}, 7: {1: 'chai'}, 8: ''}
# a.pop()
# print(a)                                  #  TypeError: pop expected at least 1 argument, got 0
# a.popitem()
# print(a)                                   # {1: 123, 2: 'python', 3: 6.12, 5: [1, 2, 3], 6: {1, 2, 3}, 7: {1: 'chai'}}  


# a={1:123,2:'python',3:6.12,4:(1,2,3),5:[1,2,3],6:{1,2,3},7:{1:"chai"},8:""}
# a.update({8:"sai"})
# print(a)                                   #{1: 123, 2: 'python', 3: 6.12, 4: (1, 2, 3), 5: [1, 2, 3], 6: {1, 2, 3}, 7: {1: 'chai'}, 8: 'sai'}
# a.update({9:"python"})
# print(a)                            # {1: 123, 2: 'python', 3: 6.12, 4: (1, 2, 3), 5: [1, 2, 3], 6: {1, 2, 3}, 7: {1: 'chai'}, 8: 'sai', 9: 'python'}


# a={1:123,2:'python',3:6.12,4:(1,2,3),5:[1,2,3],6:{1,2,3},7:{1:"chai"},8:""}
# a.setdefault(8,"devops")
# print(a)                    # {1: 123, 2: 'python', 3: 6.12, 4: (1, 2, 3), 5: [1, 2, 3], 6: {1, 2, 3}, 7: {1: 'chai'}, 8: ''}
# a.setdefault(9,"devops")
# print(a)                    # {1: 123, 2: 'python', 3: 6.12, 4: (1, 2, 3), 5: [1, 2, 3], 6: {1, 2, 3}, 7: {1: 'chai'}, 8: '', 9: 'devops'}

# print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']



