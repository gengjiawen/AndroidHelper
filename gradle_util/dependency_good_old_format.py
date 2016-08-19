import re

s = """
    compile group: 'commons-io', name: 'commons-io', version: '2.5'
    compile group: 'com.google.guava', name: 'guava', version: '19.0'
"""

for i in s.strip().splitlines():
    r = re.findall("'(.*?)'", i)
    old_good = r"compile '{}:{}:{}'".format(*r)
    print(old_good)
