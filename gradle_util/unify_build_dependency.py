import re

builds = r"""
    compile 'com.google.guava:guava:19.0'
    compile 'commons-io:commons-io:2.5'
    compile 'com.squareup.retrofit2:retrofit:2.1.0'

    compile 'com.google.auto.service:auto-service:1.0-rc2'
    compile 'com.google.auto:auto-common:0.6'
    compile 'com.squareup:javapoet:1.7.0'
"""

ff = [i.strip() for i in builds.strip().split("\n") if i]
versions = list()
dependencies = list()
for i in ff:
    ss= re.search(r"'(.*)'", i).group(1).split(":")
    artifact = ss[1].replace("-", "")
    version = "{}Version = '{}'".format(artifact, ss[2])
    real = '{} : "{}:{}:${}Version",'.format(artifact, ss[0], ss[1], artifact)
    versions.append(version)
    dependencies.append(real)

print("\n".join(versions))
print()
print("\n".join(dependencies))
