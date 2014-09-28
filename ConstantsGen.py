
s = ["activity_id", "friendName", "avatar", "title", "bg", "interstedNo", "joinNo", "isInterested"]
result = []
for i in s:
    result.append("private static final String {0} = \"{1}\";".format(i.upper(), i))

for i in result:
    print(i)
