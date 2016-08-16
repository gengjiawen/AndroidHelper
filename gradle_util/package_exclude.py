from zipfile import ZipFile

from utils import file_util


def gen_package_exclude(lib_path):
    exclude_list = set()
    for i in file_util.get_files_by_extensions(lib_path, extensions=".jar"):
        print(i)
        z = ZipFile(i, 'r')
        filelist = z.namelist()
        for j in filelist:
            if j.startswith("META-INF/") and not j.endswith("/"):
                exclude_list.add(j)
    package_exclude = """packagingOptions {{ \n{0} \n}} """
    l = sorted(exclude_list)
    f = "\n".join("\texclude '{}'".format(i) for i in l)
    print(f)
    print(package_exclude.format(f))


