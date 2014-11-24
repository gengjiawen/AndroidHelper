
s = """       android:textSize="14sp"
                        android:layout_marginLeft="10dp"
                        android:layout_marginRight="10dp"
                        android:layout_marginBottom="10dp"
                        android:background="@drawable/btn_pafun_fragment" """
results = ["<style name=\"\">"]

sa = s.replace("\"", "").split('\n')
for i in sa:
    ta = i.strip().split('=')
    if ta.__len__() == 2:
        results.append("\t<item name={0}>{1}</item>".format(ta[0], ta[1]))

results.append("</style>")
for i in results:
    print(i)
