#import codecs to deal with utf8 (what text in mac uses)
#This is using a Generator expressions
import re

s = "523319229035323393    RT @bonita_kayla: say they love you , but you know they don't 😅 523319229035335680    wtf is this true? LOL http://t.co/WA1LuPgIrp"
print(re.findall(r'((\w)\2)', s))
