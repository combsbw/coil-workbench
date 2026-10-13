import json,sys
d=json.load(open(sys.argv[1]))
n=int(sys.argv[2]) if len(sys.argv)>2 else 1800
for a in d['articles']:
    au=a['authors'][0]['last_name'] if a.get('authors') else None
    print(a['identifiers']['pmid'],'|',au,'|',a['publication_date'].get('year'),'|',a['journal']['iso_abbreviation'],'|',a['identifiers'].get('doi'),'|',a['title'])
    print('  ',a.get('abstract','')[:n])
    print()
