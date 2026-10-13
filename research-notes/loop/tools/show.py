import json,sys
n=int(sys.argv[2]) if len(sys.argv)>2 else 1500
d=json.load(open(sys.argv[1]))
for a in d['articles']:
    print(a['identifiers'].get('pmid'),a['identifiers'].get('doi'),a['publication_date']['year'],a['journal']['iso_abbreviation'],(a['authors'][0]['last_name'] if a['authors'] else ''), a['identifiers'].get('pmc',''))
    print(a['title']);print((a.get('abstract') or '')[:n]);print()
