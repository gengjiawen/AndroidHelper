name = 'dailyLogin'
content = '<b>Hello World</b>'
s = '<string name="{0}" formatted="false"><![CDATA[{1}]]></string>'.format(name, content)
c = '{0}TextView.setText(Html.fromHtml(getString(R.string.{0})));'.format(name)

print(s)
print(c)