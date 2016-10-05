import lxml.etree as et

from utils import xml_util

sense = r"""
<template name="t{1}" value="{2}.{1}(&quot;$END$&quot;);" description="{0}.{1}(message)" toReformat="false" toShortenFQNames="true">
    <context>
      <option name="JAVA_EXPRESSION" value="true" />
    </context>
</template>
"""

sense_variable = r"""
  <template name="t{1}v" value="{2}.{1}(&quot;$EXPR_COPY$ = &quot; + $EXPR$);" description="Prints a value to {0}.{1}(message)" toReformat="true" toShortenFQNames="true">
    <variable name="EXPR" expression="variableOfType(&quot;&quot;)" defaultValue="&quot;expr&quot;" alwaysStopAt="true" />
    <variable name="EXPR_COPY" expression="escapeString(EXPR)" defaultValue="" alwaysStopAt="false" />
    <context>
      <option name="JAVA_CODE" value="false" />
      <option name="JAVA_STATEMENT" value="true" />
      <option name="GROOVY" value="false" />
      <option name="GROOVY_STATEMENT" value="false" />
    </context>
  </template>
"""

root = et.Element("templateSet")

xml_util.set_elem_attr(root, {"group": "Timer"})

for i in ["v", "d", "i", "e"]:
    root.append(et.fromstring(sense.format("Timer", i, r"timber.log.Timber")))
    root.append(et.fromstring(sense_variable.format("Timer", i, "timber.log.Timber")))

xml_util.save_xml("Timber", root, False)
