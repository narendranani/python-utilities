from pprint import pprint
import jsonref
import json

json_str = """{"real": [1, 2, 3, 4], "ref": {"$ref": "#/real"}}"""
json_str = """{ "mouth":
    { "teeth":{
        "$id" : "711"
        ,"name": "shanthan"
    }
    },
    "$ref":"711",
    "references":[{
        "0":{
            "$ref":"711"
        }}
    ]
}"""
obj = json.loads(json_str)
# data = jsonref.loads(json_str)
js_ref = jsonref.JsonRef(obj, jsonschema=True)
# data = js_ref.loads(json_str)
pprint(js_ref)

