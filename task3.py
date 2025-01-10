import requests

KeyID = "Your keyid"
Secret = "Your secret"
url = "http://cloud.gstore.cn/api"
sparql = "PREFIX : <file:///F:/d2r-server-0.7/holder8.nt#holder_copy/>" \
         "select (cycleBoolean(:{}, :{}, true, {{}}) as ?x)where{{ }}"
para1 = input()
para2 = input()
sparql = sparql.format(para1, para2)
res = requests.post(url, json={"action": "queryDB", "dbName": "jinrong", "accesskeyid": KeyID, "access_secret": Secret,
                               "sparql": sparql})
if res.json()['data']['results']['bindings'][0]['x']['value'] == 'true':
    print(para1 + '和' + para2 + "之间存在环路")
else:
    print(para1 + '和' + para2 + "之间不存在环路")
