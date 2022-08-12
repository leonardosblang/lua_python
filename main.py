import random

from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)

lua_order_table = lua.eval('''
     function(L)
         local t = {}
        for index, item in python.enumerate(L) do
            t[ index+1 ] = item
        end
       table.sort(t)
        return t
     end
''')


def lua_script(script_file):
    with open(script_file, 'r') as f:
        script = f.read()
    return script


def random_array(length):
    return [random.randint(0, length) for _ in range(length)]


python_version = random_array(5)
print(python_version)

table = lua_order_table(python_version)

python_version_sorted = []

for i in range(1, len(table) + 1):
    python_version_sorted.append(table[i])

print(python_version_sorted)


lua.eval(lua_script('lua_file.lua'))

print(lua.eval('16*16'))
