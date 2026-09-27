"""
def check_services(service,namespace):
    print(f"Checking {service} in {namespace}")

check_services("mesdhagateway-service","production")

#return values:

def check_status(status):
    if status == 200:
        return True
    else:
        return False

result = check_status(200)
print(result)

#args and kargs
def log_message(*messages):
    for message in messages:
        print(message)

def deploy(**config):
    print(config)

deploy(
    app="gateway",
    namespace="prod",
    replicas=3
) 
"""


#testing *args | **kargs
def master_function(*args, **kwargs):
    print(f"args tuple: {args}")
    print(f"kwargs dict: {kwargs}")

master_function(1, 2, 3, name="Alice", age=30)