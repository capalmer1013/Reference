#!/usr/bin/env python
"""
> increment data pointer (point to cell to right)
< decrement data pointer (point to cell to left)
+ increment cell at data pointer
- decrement cell at data pointer
. output char of data pointer
, accept value to store in data pointer
[ if value in data pointer is zero jump to next ] instead of next command
] if value in data pointer is nonzero jump to previous [
"""
import sys
commands = ['>', '<', '+', '-', '.', ',', '[', ']']
f = open(sys.argv[1])
code = f.read()

instructionPointer = 0
dataPointer = 0
instructionArray = []
dataArray = [0]
for character in code:
    if character in commands:
        instructionArray.append(character)

instructionArray.append('end')

# begin program

ex = instructionArray[instructionPointer]

def errorLog():
    print "ex command", ex
    print "instruction pointer:", instructionPointer
    print "data pointer:", dataPointer
    print "instruction array:", ' '.join(instructionArray)
    print "data array", dataArray

while ex != 'end':
    ex = instructionArray[instructionPointer]

    if ex == '>':
        dataPointer += 1
        while len(dataArray) <= dataPointer:
            dataArray.append(0)

    elif ex == '<':
        dataPointer -= 1
        if dataPointer < 0:
            print "stack underflow"
            errorLog()
            sys.exit()

    elif ex == '+':
        dataArray[dataPointer] += 1

    elif ex == '-':
        dataArray[dataPointer] -= 1

    elif ex == '.':
        sys.stdout.write(chr(dataArray[dataPointer]))
        sys.stdout.flush()

    elif ex == ',':
        dataArray[dataPointer] = ord(raw_input())

    elif ex == '[':
        if dataArray[dataPointer] == 0:
            while instructionArray[instructionPointer] != ']':
                instructionPointer += 1

    elif ex == ']':
        if dataArray[dataPointer] != 0:
            while instructionArray[instructionPointer] != '[':
                instructionPointer -= 1

    elif ex == 'end':
        print ''
        sys.exit()

    else:
        print "Error, ex ==", ex
        sys.exit()

    instructionPointer += 1
