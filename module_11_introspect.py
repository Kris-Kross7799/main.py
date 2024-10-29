import sys
import requests
from pprint import pprint
import inspect

# class Example:
#     def __init__(self, obj):
#         self.obj = obj
#         self.atribute = 'Blue'
#
#     def metod_1(self):
#         pass
#
#     def metod_2(self):
#         pass

def introspection_info(obj):
    t = type(obj)
    attr = []
    meth = []
    for i in dir(obj):
        if i.startswith("__"):
            meth.append(i)
        else:
            attr.append(i)
    place = inspect.getmodule(obj)
    module_name = place.__name__ if place is not None else "__main__"
    res = {"type": t, "attributes": attr, "methods": meth, "module": module_name}
    return res


number_info = introspection_info(42)
print(number_info)
