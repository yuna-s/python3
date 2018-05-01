import sys
import codecs

for line in codecs.open(sys.argv[1], "r","utf-8"):
    print(line.replace("\t", "\""))
