
s = ["pa_fun_activity_model"]
result = []
for i in s:
    result.append("private static final String {0} = \"{1}\";".format(i.upper(), i))

for i in result:
    print(i)
