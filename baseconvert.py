import sys
from workflow import Workflow

#map of digit to their base 10 value
chars = map(str, range(0,10)) + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main(wf):
    try: 
        query = wf.args[0]
        result = convert(query)
        wf.add_item(title=result, valid=True, arg=result, copytext=result)
    except:
        wf.add_item("Invalid input. format: {base}x{number} {target-base}")
    wf.send_feedback()


def convert(query):
    query = query.upper()
    query = query.split()
    source = parseSource(query[0])
    if len(query) == 1:
        if source[1] == 10:
            query.append(str(16))
        else:
            query.append(str(10))
    if len(query) == 2 and query[1].strip() != "":
        target = parseTargetBase(query[1])
        base10 = toBase10(*source)
        return fromBase10(base10, target)
    raise Exception


"""
checks for special expressions of bases and translates them to an int
0x - 16 
0 - 14
"""
def parseTargetBase(target):
    if target == "D":
        return 10
    if target == "B":
       return 2 
    if target == "0X":
        return 16
    if target in ("0", "O"):
        return 8
    return int(target)


def parseSource(source):
    if source[0] in ("D"):
        return source[1:], 10
    if source[0] in ("B"):
        return source[1:], 2
    if source[0] in ("0", "O") and source[0:2] != "0X":
        return source[1:], 8
    if source[0:2] == ("0X"):
        return (source[2:]), 16
    source = source.split("X")
    #nothing = base 10
    if len(source) == 1:
        return source[0], 10
    return source[1], int(source[0])

def toBase10(num, base):
    power = 0
    convertedNumber = 0
    for d in num[::-1]:
        if chars.index(d) >= base:
            raise Exception
        convertedNumber += chars.index(d)*int(pow(base, power))
        power += 1
    return convertedNumber

def fromBase10(num, target):
    convertedNumber = ""
    while num > 0:
        convertedNumber += chars[num%target]
        num = int(num/target)
    return convertedNumber[::-1]

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
