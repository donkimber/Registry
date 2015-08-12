import json

objs = json.load(file("datadump.txt"))

for obj in objs:
   for key in obj:
       print "%s:" % (key,)
       print obj[key]
   print

