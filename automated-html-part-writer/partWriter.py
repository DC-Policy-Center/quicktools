# Figure out if there already is a TOC writer

from string import Template

with open('epi-page-article-card-template.txt','r') as infile:
    template = infile.read()

output = Template(template)

input_dict = {
'author' : "null",
'authorDash' : "null",
'date'  : "null",
'title' : "null",
'articleURL' : "null",
'feature' : "null",
'description': "null"
}
print(type(input_dict))

for key in input_dict.keys():
    input_dict[key] = input('What is the input for { %s } : '%key)

print(type(output))
for item in input_dict.keys():
    print('replacing {%s} with %s'%(item,input_dict[item]))
    output_2 = output.safe_substitute(input_dict)



with open('output-epi-html.txt','w') as outfile:
    outfile.write(output_2)
