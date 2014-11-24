
wl = open("parcelable.txt").read().splitlines()

write = []
read = []

for w in wl:
    if w.strip() == '':
        continue
    wl = w.strip().split()
    wl[1] = wl[1].replace(';', '')
    # print(wl)
    if wl[0].startswith('int'):
        write.append('dest.writeInt({0});'.format(wl[1]))
        read.append('{0} = source.readInt();'.format(wl[1]))

    if wl[0].startswith('double'):
        write.append('dest.writeDouble({0});'.format(wl[1]))
        read.append('{0} = source.readDouble();'.format(wl[1]))

    if wl[0].startswith('String'):
        write.append('dest.writeString({0});'.format(wl[1]))
        read.append('{0} = source.readString();'.format(wl[1]))

    if wl[0].startswith('Date'):
        write.append('dest.writeLong({0}.getTime());'.format(wl[1]))
        read.append('{0} = new Date(source.readLong());'.format(wl[1]))

    if wl[0].startswith('boolean'):
        write.append('dest.writeInt({0} ? 1 : 0);'.format(wl[1]))
        read.append('{0} = source.readInt() == 1;'.format(wl[1]))

for w in write:
    print(w)

for r in read:
    print(r)