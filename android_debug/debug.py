import getopt
import os

import sys


def executes_cmds(cmds):
    for i in cmds.strip().split("\n"):
        print(i)
        os.system(i)


package_name = r"com.shundaojia.travel.driver"
main_activity = r"com.shundaojia.travel.ui.main.MainActivity"

clear_app_data = r"""
adb shell pm clear {0}
adb shell am start -n "{0}/{1}" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER
""".format(package_name, main_activity)
adb_pull = r"adb pull /data/data/{0} {0}".format(package_name)


def clear():
    executes_cmds(clear_app_data)


def pull():
    os.makedirs(package_name, exist_ok=True)
    executes_cmds(adb_pull)

_options = [
    'file',
    'clear',
]
_short_options = 'fc'


def main(**kwargs):
    opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
    print(opts)
    if "clear" in args:
        clear()
    if "file" in args:
        pull()


if __name__ == '__main__':
    main()
