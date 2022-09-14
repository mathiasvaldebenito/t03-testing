# código que recorre el AST e injecta el código al inicio de cada función.
from ast import *
import threading
from multiprocessing.dummy import Array
import os

class Instrumentor(NodeTransformer):
    
    def __init__(self):
        self.functions = dict()

    def visit_Call(self, node: Call):
        transformedNode = NodeTransformer.generic_visit(self, node)
        func_name = transformedNode.func.id
        
        if func_name not in self.functions:
            self.functions[func_name] = []
        for arg in transformedNode.args:
            if isinstance(arg, Constant):
                if arg.value not in self.functions[func_name]:
                    self.functions[func_name].append(arg.value)

        return transformedNode


class Profile:
    __singleton_lock = threading.Lock()
    __singleton_instance = None
    @classmethod
    def getInstance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    @classmethod
    def reset(cls):
        cls.__singleton_instance = None

    @classmethod
    def record(cls, functionName, args):
        cls.getInstance().ins_record(cls, functionName,args)
    
    # instance method
    def __init__(self):
        self.functions_called=[]
    def ins_record(self, cls, functionName, args):   
        self.functions_called.append(functionName)
    def printReport(self):
        print("-- Funciones Cacheables --")
        for fun in self.functions_called:
            print(fun)

    
def instrument(ast):
    visitor = Instrumentor()
    return  fix_missing_locations(visitor.visit(ast)), visitor.functions