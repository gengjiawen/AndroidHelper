name = 'tip'
content = '<b>Hello World</b>'
s = '<string name="{0}"><![CDATA[{1}]]></string>'.format(name, content)
c = 'tipTextView.setText(Html.fromHtml(getString(R.string.{0})));'.format(name)

print(s)
print(c)