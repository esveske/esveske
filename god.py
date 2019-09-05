import pandas as pd
import sys
from prog_names import prog_names

_, year, outfile = sys.argv

# read the template
with open('./god.template.html', encoding='utf-8') as template_f:
    template = template_f.read()

# put in program name
template = template.replace('@@YEAR@@', year)

# read the metadata
df = pd.read_csv('./data.csv')

# filter only this programme
df = df[df['god'] == int(year)]

content = ''

# group by program
for prog, data in df.groupby(['prog'], sort=False):
    prog_name = prog_names[prog.lower()]
    content += f'<h2>{prog_name}</h2>\n'
    content += '<ul>\n'

    # group by link / project
    for link, data_ln in data.groupby(['link']):
        title = data_ln['naslov'].iloc[0]
        authors = data_ln['autor'].str.cat(sep=', ')
        content += f'<li><a href="{link}">{title}</a> ({authors})</li>\n'

    content += '</ul>'

template = template.replace('@@CONTENT@@', content)

with open(outfile, 'w', encoding='utf-8') as outf:
    outf.write(template)

