#!/usr/bin/python3

import r2pipe
import sys

if len(sys.argv) < 3:
    print("Usage ./generate.py <input binary> <output file>")
    exit()

r = r2pipe.open(sys.argv[1])

r.cmd("aa")
functions = r.cmd("afll~[14] | grep -v xref | grep -v imp | grep -v entry").split("\n")

data = []

print("Found " + str(len(functions)) + " functions")

for function in functions:
    r.cmd("s " + function)
    code = r.cmd("pdg")
    p = code.split("{")[0]
    p = p.split("\n")
    prototype = ""

    for line in p:
        if not "//" in line:
            prototype += line
    prototype = prototype.replace("int64_t", "int")
    prototype = prototype.replace("undefined8", "int")
    prototype = prototype.replace("uint", "int")
    prototype = prototype.replace("(void)", "()")
    prototype = prototype.replace("undefined", "void")
    data.append((function, prototype))
    
output = ""
for a, b in data:
    print("  " + b)
    output += b + ";\n"

print("Writing .h file")
with open(sys.argv[2], "w") as f:
    f.write(output)
