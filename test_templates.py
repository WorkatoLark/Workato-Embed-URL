

import json

data = [
    {
      "keyword": "application",
      "name": "github",
      "provider": "github",
      "skip_validation": False,
      "account_id": 13383439
    },
    {
      "keyword": "application",
      "name": "lark_connector_3353663_1704406579",
      "provider": "lark_connector_3353663_1704406579",
      "skip_validation": False,
      "account_id": 13315058
    }
]

json_string = json.dumps(data)

escaped_json_string = json.dumps(json_string)
print(escaped_json_string)
