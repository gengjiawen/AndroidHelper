import re

builds = r"""
    compile "com.squareup.okhttp3:okhttp:3.4.1"

    compile 'com.github.bumptech.glide:glide:3.7.0'

    compile 'io.reactivex.rxjava2:rxandroid:2.0.0-RC1'
    compile 'io.reactivex.rxjava2:rxjava:2.0.0-RC2'

    // data
    compile 'com.google.code.gson:gson:2.7'
    compile 'com.google.protobuf:protobuf-java:3.0.2'
    compile 'com.squareup.wire:wire-runtime:2.2.0'

    compile 'com.google.dagger:dagger:2.6.1'
    annotationProcessor 'com.google.dagger:dagger-compiler:2.6.1'
    provided 'org.glassfish:javax.annotation:10.0-b28' //Required by Dagger2
"""

ff = [i.strip() for i in builds.strip().split("\n") if i]
versions = list()
dependencies = list()
for i in ff:
    if i and not i.startswith("//"):
        ss= re.search(r"['|\"](.*)['|\"]", i).group(1).split(":")
        if ss and len(ss) == 3:
            artifact = ss[1].replace("-", "")
            version = "{}Version = '{}'".format(artifact, ss[2])
            real = '{} : "{}:{}:${}Version",'.format(artifact, ss[0], ss[1], artifact)
            versions.append(version)
            dependencies.append(real)

print("\n".join(versions))
print()
print("\n".join(dependencies))
