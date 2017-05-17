import re


def find_proguard_rules(proguard_file):
    """
    :param proguard_file: progurad waring file.For linux,you can use somthing like
    "./gradlew aR 2>&1 | tee -a build_log.txt"
    :return:
    """
    s = open(proguard_file, mode='r', encoding='utf-8').read()
    # all_class = re.findall("Warning:.*referenced class (.*)", s)
    # all_field = re.findall("Warning:.* in program class (.*)", s)
    # all_type = all_class + all_field
    tmp_all = re.findall("Warning:.*( in program|referenced|depends on program|in library|implements program) class (.*)", s)
    all_type = {i[1] for i in tmp_all}
    proguard_issue = sorted(all_type)
    refined_issue = set()
    for i in proguard_issue:
        sec_dot_pos = i.find(".", i.find(".") + 1)
        refined_issue.add(i[:sec_dot_pos])

    print("\n".join(sorted(proguard_issue)))
    print("\nrefined rule:")
    print("\n".join(sorted(refined_issue)))
    return proguard_issue

