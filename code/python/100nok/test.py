import sys

with open(sys.argv[1]) as f:
    lines=f.read()
    lines=repr(lines)
    check=lines.find("\t")

    print check
    print lines
    print "mm\tya"
