
import csv
import json
from collections import defaultdict
from operator import itemgetter

dd = defaultdict(list)
#new_dict = dict(dd)
with open('ETD_counts_final.csv') as fin:
    csvin = csv.DictReader(fin)
    for row in csvin:
        #dd.append([row['color'],[row['count'], row['year'], row['info']]])
        count = int(row['count'])
        year = int(row['year'])
        url = (row['url'])
        dd[row['college'], row['dept']].append([year, count, url])
        
#print dd.items()
reformatted = [{'dept': v, 'college': c, 'name': f} for (c, f), v in dd.items()]
#print reformatted
newlist = sorted(reformatted, key=itemgetter('name'), reverse=False)
jsonf = open('ETDv2.json','w')
data = json.dumps(newlist)
jsonf.write(data) 
jsonf.close()