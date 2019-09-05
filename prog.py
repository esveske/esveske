import pandas as pd
import sys

prog_names = {
    'ast': "Astronomija",
    'fiz': "Fizika",
    'mat': 'Matematika',
    'pfe': 'Primenjena fizika i elektronika',
    'ele': 'Elektronika',
    'rac': 'Računarstvo',
    'bio': 'Biologija',
    'bmd': 'Biomedicina',
    'hbh': 'Humana biohemija',
    'glg': 'Geologija',
    'geo': 'Geografija',
    'hem': 'Hemija',
    'ska': 'Sociokulturna antropologija',
    'fan': 'Fizička antropologija',
    'ahl': 'Arheologija',
    'ist': 'Istorija',
    'lin': 'Lingvistika',
    'psh': 'Psihologija'
}

_, program, outfile = sys.argv

# read the template
with open('./prog.template.html', encoding='utf-8') as template_f:
    template = template_f.read()

# put in program name
template = template.replace('@@PROGRAM@@', prog_names[program])

# read the metadata
df = pd.read_csv('./data.csv')

# filter only this programme
df = df[df['prog'] == program.upper()]

content = ''

# group by year
for year, data in df.groupby(['god']):
    content += f'<h2>{year}</h2>\n'
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

