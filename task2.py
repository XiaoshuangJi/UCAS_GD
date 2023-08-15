import requests

KeyID = "2054ef3cc0a64b5daf0c3afc54f7ffae"
Secret = "6E4D50404DCC641599EAB7807D138CFA"
url = "http://cloud.gstore.cn/api"


def holder_copy(company):
    results = []
    sparql = "PREFIX name: <file:///F:/d2r-server-0.7/holder8.nt#holder_copy/> prefix :<http://localhost:2020/vocab/resource/holder_copy_holder_name> select ?x where {{name:{} : ?x}}".format(
        company)
    res = requests.post(url,
                        json={"action": "queryDB", "dbName": "jinrong", "accesskeyid": KeyID, "access_secret": Secret,
                              "sparql": sparql})
    for i in range(len(res.json()['data']['results']["bindings"])):
        results.append(res.json()['data']['results']["bindings"][i]['x']['value'].lstrip("file:///F:/d2r-server-0.7/holder8.nt#holder_copy/"))
    return results


company = input()
k = int(input())
last = [company]
now = []
for x in range(1, k + 1):
    print(company + "的" + str(x) + "级股东有：")
    for y in range(len(last)):
        for z in range(len(holder_copy(last[y]))):
            now.append(holder_copy(last[y])[z])
    for item in now:
        print(item)
    last = now
    now = []



