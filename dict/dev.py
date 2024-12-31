# new_dict = dict(one='uno', two='dos', three='tres')
# print(new_dict)
# new_dict2 = {1:'uno', 2:'dos', 3:'tres'}
# print(new_dict2)
# dict_list = [(1,'uno'), (2,'dos'), (3,'tres')]
# new_dict3 = dict(dict_list)
# print(new_dict3)
get_query = {"user_id": "xyz"}

query = {"status": { "$ne": "deleted"}}



# if len(get_query) != 0:
#     # print("Empty dict")
# new_query = {**get_query, **query}
new_query = {}
print(new_query)

aggregate_query = [
        {"$match": {"$and": [{"abc": "def"}, new_query]}},
        { "$lookup": { "from": "user", "localField": "user_id", "foreignField": "_id", "as": "user_details" }},
        { "$lookup": { "from": "skill", "localField": "_id", "foreignField": "companion_id", "as": "skills" }}
]
res = []
for k,v in new_query.items():
    res.append({k: v})
print(f"result: {res}")
# else:
#     print("Dict is empty")

def get_aggregate_query(match_feild,id,query):
    match_query = [{match_feild: id}]
    for key, value in query.items():
        match_query.append({key: value})
    aggregate_query = [
            {"$match": {"$and": match_query}},
            { "$lookup": { "from": "user", "localField": "user_id", "foreignField": "_id", "as": "user_details" }},
            { "$lookup": { "from": "skill", "localField": "_id", "foreignField": "companion_id", "as": "skills" }}
    ]
    print(f'aggregate_query is ---->, {aggregate_query}')
    return aggregate_query

print(get_aggregate_query(match_feild="_id", id="xyz", query=new_query))

custom_headers = {"x-dpn-namespace": "NAMESPACE",  "Authorization": f"Bearer abcdref"}
query=dict(token="token", **custom_headers)
print(f"Query: {query}")