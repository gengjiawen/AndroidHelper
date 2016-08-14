packages = """
java.nio
org.codehaus.mojo
"""

hacklist = packages.split()
print(hacklist)

print("processing...")
for i in hacklist:
    dontwarn = "-dontwarn {}.**".format(i)
    keep = "-keep class {}.** {{*;}}".format(i)
    print("{}\n{}".format(dontwarn, keep))
