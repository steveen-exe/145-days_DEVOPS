print("hey")
#Variables
env = "prod"
#Data stuctures
#types 
#int,float,bool,string
print(type(env))

#4 primitive data structures
#list, dic, set and tuple

env = ["dev", "staging", "production"]
print(type(env))

#pass this as an object, key:value
info = {
    "name":"Steven",
    "years_of_exp":"2",
    "env": ["dev", "staging", "production"]
}

print(info["years_of_exp"])
print(type(info))

#tuple
days_of_week= ("mon","tue","wed","thu","fri","sat")
#immutable, use-less mmy

#set
num ={0,1,3,4,3,3,3,6,7,3}
print(num)
