import json

# Original JSON string
# original_json_string = "{\"number\":0,\"provider\":\"github\",\"name\":\"new_issue\",\"as\":\"a637bf22\",\"keyword\":\"trigger\",\"toggleCfg\":{\"repository_owner\":false,\"repository_name\":false},\"input\":{\"since\":\"2024-01-04T00:00:00-08:00\",\"repository_owner\":\"#{_dp('{\\\"pill_type\\\":\\\"account_property\\\",\\\"property_name\\\":\\\"{\\\\\\\\\\\"required\\\\\\\\\\\":\\\\\\\\\\\"true\\\\\\\\\\\",\\\\\\\\\\\"type\\\\\\\\\\\":\\\\\\\\\\\"picklist\\\\\\\\\\\",\\\\\\\\\\\"picklist_name\\\\\\\\\\\":\\\\\\\\\\\"org\\\\\\\\\\\"}\\\"}')}\",\"repository_name\":\"#{_dp('{\\\"pill_type\\\":\\\"account_property\\\",\\\"property_name\\\":\\\"github_org\\\"}')}\"},\"block\":[{\"number\":1,\"provider\":\"lark_connector_3353663_1704406579\",\"name\":\"send_message\",\"as\":\"4988677b\",\"keyword\":\"action\",\"dynamicPickListSelection\":{\"scope_id\":\"admin\"},\"input\":{\"scope_id\":\"admin\",\"receive_id\":\"#{_dp('{\\\"pill_type\\\":\\\"account_property\\\",\\\"property_name\\\":\\\"{\\\\\\\\\\\"required\\\\\\\\\\\":\\\\\\\\\\\"true\\\\\\\\\\\",\\\\\\\\\\\"type\\\\\\\\\\\":\\\\\\\\\\\"picklist\\\\\\\\\\\",\\\\\\\\\\\"picklist_name\\\\\\\\\\\":\\\\\\\\\\\"org\\\\\\\\\\\"}\\\"}')}\",\"msg_type\":\"#{_dp('{\\\"pill_type\\\":\\\"account_property\\\",\\\"property_name\\\":\\\"{\\\\\\\\\\\"required\\\\\\\\\\\":\\\\\\\\\\\"true\\\\\\\\\\\",\\\\\\\\\\\"type\\\\\\\\\\\":\\\\\\\\\\\"picklist\\\\\\\\\\\",\\\\\\\\\\\"picklist_name\\\\\\\\\\\":\\\\\\\\\\\"org\\\\\\\\\\\"}\\\"}')}\",\"content\":\"#{_dp('{\\\"pill_type\\\":\\\"account_property\\\",\\\"property_name\\\":\\\"{\\\\\\\\\\\"required\\\\\\\\\\\":\\\\\\\\\\\"true\\\\\\\\\\\",\\\\\\\\\\\"type\\\\\\\\\\\":\\\\\\\\\\\"picklist\\\\\\\\\\\",\\\\\\\\\\\"picklist_name\\\\\\\\\\\":\\\\\\\\\\\"org\\\\\\\\\\\"}\\\"}')}\",\"uuid\":\"#{_dp('{\\\"pill_type\\\":\\\"account_property\\\",\\\"property_name\\\":\\\"{\\\\\\\\\\\"required\\\\\\\\\\\":\\\\\\\\\\\"true\\\\\\\\\\\",\\\\\\\\\\\"type\\\\\\\\\\\":\\\\\\\\\\\"picklist\\\\\\\\\\\",\\\\\\\\\\\"picklist_name\\\\\\\\\\\":\\\\\\\\\\\"org\\\\\\\\\\\"}\\\"}')}\"},\"visible_config_fields\":[\"uuid\",\"scope_id\",\"content\",\"msg_type\",\"receive_id\"],\"uuid\":\"5d39e73d-2137-43f7-847c-982c35a976c1\"}],\"uuid\":\"6ca296a0-0f28-4e8d-9978-99667c6f91af\",\"unfinished\":false}"
#
#
#
# # Convert to a Python dictionary
# parsed_json = json.loads(original_json_string)
#
# # Convert back to string with pretty formatting
# prettified_json_string = json.dumps(parsed_json, indent=2)
#
# print(prettified_json_string)
