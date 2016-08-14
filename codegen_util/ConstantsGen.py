consts = """
male
"""

for i in consts.strip().splitlines():
    c = 'private static final String {0} = "{1}";'.format(i.upper(), i)
    print(c)


