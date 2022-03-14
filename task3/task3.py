import json

def have_key_in_dict(key, d_dict):
    if key in d_dict:
        return (True)
    else:
        return (False)


def change_values_dict(i, d_values):
    for i_elm in i:
        if have_key_in_dict(i_elm["id"], d_values):
            i_elm["value"] = d_values.get(i_elm["id"])
        else:
            i_elm["value"] = None
        if "values" in i_elm:
                change_values_dict(i_elm["values"], d_values)
        

with open('tests.json', 'r') as jf:
    tests = json.load(jf)

with open('values.json', 'r') as f:
    values = json.load(f)

    d_values = dict()
    tests["reports"] = tests.pop("tests")

    for i in values["values"]:
        d_values[i["id"]] = i["value"]
        
    for i in tests["reports"]:
        if have_key_in_dict(i["id"], d_values):
            i["value"] = d_values.get(i["id"])
        if "values" in i:
            change_values_dict(i["values"], d_values)
    
with open('reports.json', 'w') as wf:
    json.dump(tests, wf, indent = 4)


    
