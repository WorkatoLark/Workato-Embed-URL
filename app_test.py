import json
import webbrowser

from app import create_user, create_folder, list_all_folders, import_manifest, list_all_connections, install_app, \
    list_all_receipts, start_recipe, update_receipt, open_link_1
from jwt_token import generate_jwt, generate_token


def open_recipe():
    basic_info = json.loads('{"user_id": 3522690, "folder_id": 16715712, "recipe_id": 46119083, "connection_id_1": 13154564, "connection_id_2": 13154565}')
    try:
        token = generate_token(basic_info['user_id'])
        # token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjNDBlMWRiOTBkZDBmOTBjMDIzMmNlOTk3MmU2ZWQxMzczNDhjODBiNzE3OWZiOGU0MDI1ZWEyMWQ2MmE2NTg5OjMzNTM3MTgiLCJpYXQiOjE3MDI2MjYzNjQsImp0aSI6IjgwNjZjNWVhLTY5MzctNDA4Yi1iMjI5LWYwMTYxNjY1NWVmMyJ9.IRaS9OnEI7Xlg8W2pASCGEwoClX9qlhYFonuaeR8ZxK2RilJ9xNsANS89ruyu_i62F6YY-4MjvkcmHJKUjxWBVfo4wZw7bNDjtYOG3Xn_KtYwSyM0dzH3u0wsHkuyQEsPoQX6cbEBmtV7Feo_MM42ntVMU-XXFKve-cqmoHV8xvRoWdywbF9q6qmbuLroFWIgOyJPxEf5FC3YbADFm1IpIgGMcxmj-RGXSTV0P8onQOUNzIObLDHxN-uUGJwE7fmYi6XOVNJsK1sSlilTnO_1ZtCCNaGUzVux8Kk4903hxlrNj6PuFNdJwnzjZ9fhvpbbtiDaeIRdss60rLgmkHcqQ'
        webbrowser.open(f"https://app.workato.com/direct_link?workato_dl_path=/recipes/{basic_info['recipe_id']}&workato_dl_token={token}", new=2)

        print(f"https://app.workato.com/direct_link?workato_dl_path=/recipes/{basic_info['recipe_id']}-copy-of-deal-closed-won-in-salesforce/edit?step=80726d21-4e96-43a9-8e47-46d0522c894a&workato_dl_token={token}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # create_user('tenant_id_2')
    # install_app('tenant_id_20', 'user_id_1')

    # list_all_folders()
    # list_all_folders(parent_id='16701188')
    # user_id_1 = 16699912

    # create_folder(16701206, 'user_id_3')

    # import_manifest(3351109, 16701209)
    # start_recipe()
    # list_all_connections()
    # [{"application":"gmail","id":13131178,"name":"User222GmailConnection","description":null,"authorized_at":"2023-12-12T15:30:05.007-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-12T15:29:59.706-06:00","updated_at":"2023-12-12T15:30:05.011-06:00","external_id":null,"folder_id":16667974,"parent_id":null},{"application":"gmail","id":13131175,"name":"User111GmailConnection","description":null,"authorized_at":"2023-12-12T15:29:41.714-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-12T15:29:36.245-06:00","updated_at":"2023-12-12T15:29:41.717-06:00","external_id":null,"folder_id":16667974,"parent_id":null},{"application":"github","id":13131162,"name":"User222GithubConnection","description":null,"authorized_at":"2023-12-12T15:29:15.445-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-12T15:29:13.696-06:00","updated_at":"2023-12-12T15:29:15.447-06:00","external_id":null,"folder_id":16667974,"parent_id":null},{"application":"github","id":13131126,"name":"User111GithubConnection","description":null,"authorized_at":"2023-12-12T15:28:34.408-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-12T15:28:32.351-06:00","updated_at":"2023-12-12T15:28:34.411-06:00","external_id":null,"folder_id":16667974,"parent_id":null},{"application":"gmail","id":13123838,"name":"My second Gmail account","description":null,"authorized_at":"2023-12-11T18:56:03.926-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-11T18:55:58.592-06:00","updated_at":"2023-12-11T18:56:03.929-06:00","external_id":null,"folder_id":16672854,"parent_id":null},{"application":"github","id":13116440,"name":"My GitHub account Test 2","description":null,"authorized_at":"2023-12-11T15:47:28.633-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-10T22:21:08.554-06:00","updated_at":"2023-12-11T15:47:28.636-06:00","external_id":null,"folder_id":16667974,"parent_id":null},{"application":"github","id":13116439,"name":"My GitHub account Test 1","description":null,"authorized_at":"2023-12-10T22:20:38.092-06:00","authorization_status":"exception","authorization_error":"GitHub OAuth connection is no longer valid","created_at":"2023-12-10T22:20:38.058-06:00","updated_at":"2023-12-10T22:20:38.093-06:00","external_id":null,"folder_id":16667974,"parent_id":null},{"application":"gmail","id":13116220,"name":"My Gmail account","description":null,"authorized_at":null,"authorization_status":null,"authorization_error":null,"created_at":"2023-12-10T21:23:22.423-06:00","updated_at":"2023-12-10T21:23:22.423-06:00","external_id":null,"folder_id":16672854,"parent_id":null},{"application":"github","id":13116219,"name":"My GitHub account","description":null,"authorized_at":"2023-12-10T22:26:51.770-06:00","authorization_status":"success","authorization_error":null,"created_at":"2023-12-10T21:23:22.374-06:00","updated_at":"2023-12-10T22:26:51.773-06:00","external_id":null,"folder_id":16672854,"parent_id":null}]

    # print(list_all_receipts(3351113))
    # list_all_connections(3351113)
    # update_receipt(3351113, 43593048, "13142699", "13142710")
    # start_flow(3351113, 43593048)
    # open_link_1(3341485, 13142703)
    open_link_1()

