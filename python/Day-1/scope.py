x = 'global'
print(x)
def local_scope():
    x = 'local'
    print(x)
    def inner_local_scope():
        x = 'inner_local'
        print(x)
    inner_local_scope()
local_scope()