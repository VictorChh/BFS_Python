'''
@author: Devangini Patel

Reference: https://www.python.org/doc/essays/graphs/
'''

#create a dictionary with all the mappings
connections = {}
connections["Adam"] = {"Bob", "Ema", "Victor"}
connections["Ema"] = {"Adam", "Bob", "Dolly"}
connections["Victor"] = {"Adam", "Frank", "George"}
connections["Bob"] = {"Ema", "Dolly", "Adam"}
connections["George"] = {"Victor"}
connections["Frank"] = {"Victor"}
connections["Dolly"] = {"Bob", "Ema"}







