import json

from app import update_recipe_code


def test_update_recipe_code():
    # Your JSON-like structure as a Python dictionary
    data = {
        "number": 0,
        "provider": "github",
        "name": "new_issue",
        "as": "a637bf22",
        "keyword": "trigger",
        "toggleCfg": {
            "repository_owner": False,
            "repository_name": False
        },
        "input": {
            "since": "2024-01-04T00:00:00-08:00",
            "repository_owner": "afd",
            "repository_name": "agd"
        },
        "block": [
            {
                "number": 1,
                "provider": "lark_connector_3353663_1704406579",
                "name": "send_message",
                "as": "4988677b",
                "keyword": "action",
                "dynamicPickListSelection": {
                    "scope_id": "admin"
                },
                "input": {
                    "scope_id": "admin",
                    "receive_id": "receiver_id",
                    "msg_type": "org",
                    "content": "#{_dp('{\"pill_type\":\"account_property\",\"property_name\":\"{\\\\\"required\\\\\":\\\\\"true\\\\\",\\\\\"type\\\\\":\\\\\"picklist\\\\\",\\\\\"picklist_name\\\\\":\\\\\"org\\\\\"}')}'}",
                    "uuid": "#{_dp('{\"pill_type\":\"account_property\",\"property_name\":\"{\\\\\"required\\\\\":\\\\\"true\\\\\",\\\\\"type\\\\\":\\\\\"picklist\\\\\",\\\\\"picklist_name\\\\\":\\\\\"org\\\\\"}')}'}"
                },
                "visible_config_fields": [
                    "uuid",
                    "scope_id",
                    "content",
                    "msg_type",
                    "receive_id"
                ],
                "uuid": "5d39e73d-2137-43f7-847c-982c35a976c1"
            }
        ],
        "uuid": "6ca296a0-0f28-4e8d-9978-99667c6f91af",
        "unfinished": False
    }

    # Convert dictionary to JSON string
    json_string = json.dumps(data, indent=4)

    # Print the JSON string
    print(json_string)

    update_recipe_code("3353663", "43975284", json_string)

if __name__ == '__main__':
    test_update_recipe_code()