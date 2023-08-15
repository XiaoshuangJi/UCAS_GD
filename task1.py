import requests

KeyID = "2054ef3cc0a64b5daf0c3afc54f7ffae"
Secret = "6E4D50404DCC641599EAB7807D138CFA"
url = "http://cloud.gstore.cn/api"
para1 = input()
para2 = input()
sparql = "PREFIX : <file:///F:/d2r-server-0.7/holder8.nt#holder_copy/> SELECT ?a ?b ?c ?d ?p1 ?p2 WHERE {{{{:{x} ?a :{y}.}} union {{:{y} ?b :{x}.}} union {{:{x} ?c ?p1. ?p1 ?c :{y}.}} union {{:{y} ?d ?p2. ?p2 ?d :{x}.}}}}".format(x=para1, y=para2)
res = requests.post(url, json={"action": "queryDB", "dbName": "jinrong", "accesskeyid": KeyID, "access_secret": Secret,
                               "sparql": sparql})
for i in range(len(res.json()['data']['results']['bindings'])):
    if len(res.json()['data']['results']['bindings'][i]) == 1:
        for key in res.json()['data']['results']['bindings'][i]:
            if key == 'a':
                print("一跳：" + para1 + "->" + para2)
            elif key == 'b':
                print("一跳：" + para2 + "->" + para1)
    elif len(res.json()['data']['results']['bindings'][i]) == 2:
        for key in res.json()['data']['results']['bindings'][i]:
            if key == 'p1':
                print("两跳：" + para1 + "->" + res.json()['data']['results']['bindings'][i][key]['value'].lstrip("file:///F:/d2r-server-0.7/holder8.nt#holder_copy/") + "->" + para2)
            elif key == "p2":
                print("两跳：" + para2 + "->" + res.json()['data']['results']['bindings'][i][key]['value'].lstrip("file:///F:/d2r-server-0.7/holder8.nt#holder_copy/") + "->" + para1)
