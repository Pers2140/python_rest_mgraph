
import requests, json

class mgraph_rest_conn(object):
    
    def __init__(self,client_id,site_id,client_password,tenant_id,tenant_type):
        
        self.client_id = client_id
        self.client_password = client_password
        self.tenant_id = tenant_id
        self.user_site_id = site_id
        self.tenant_type = tenant_type
        
    def get_user_token(self):

        # address to request token from

        # Ask user information details to request token
        # ----------------------------------------------------------------
        # email = urllib.parse.quote(input("Please enter email: \n"))
        # password = urllib.parse.quote(input("please enter password: \n"))
        # client_id = input("Enter client ID \n")
        # client_secret = input("Enter client secret \n")
        # ----------------------------------------------------------------

        # payload=f'grant_type=password&client_id={client_id}&client_secret={client_secret}&resource=https%3A%2F%2Fgraph.microsoft.com&username={email}&password={password}'
        url = f"https://login.microsoftonline.{self.tenant_type}/{self.tenant_id}/oauth2/token"

        payload = f'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_password}&resource=https%3A%2F%2Fgraph.microsoft.com'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        # sends POST request
        response = requests.request("POST", url, headers=headers, data=payload)
        # print (response.text)
        # Parses JSON response and store only access token parameter 
        user_token = json.loads(response.text)['access_token']

        return user_token
    
    def list_doc_libs(self):
        
        # search for drive 
        url = f"https://graph.microsoft.{self.tenant_type}/v1.0/sites/{self.user_site_id}/drives/"

        # payload = f'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_password}&resource=https%3A%2F%2Fgraph.microsoft.com'
        headers = {
        'Authorization': f'Bearer {self.get_user_token()}',
        'Content-Type': "application/x-www-form-urlencoded"
        }
        # sends POST request
        response = requests.request("GET", url, headers=headers)
        
        """
        This GET request responses with a dictionary containing the following keys:
        
        'createdDateTime'
        'description'
        'id' ( drive id )
        'lastModifiedDateTime'
        'name'
        'webUrl'
        
         etc ... 
        
        """
        
        site_docLibs = json.loads(response.text)['value']
        # print (site_docLibs)
        for Lib in site_docLibs:
            print(f"\nThe Document Lib named \"{Lib['name']}\" has the id of {Lib['id']}")
            print(f"Web Address: {Lib['webUrl']}")
            print(f"\n")

        return site_docLibs
    
    def list_doc_lib_items(self,drive_id):
        
         # search for drive 
        url = f"https://graph.microsoft.{self.tenant_type}/v1.0/drives/{drive_id}/items/root/children"

        # payload = f'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_password}&resource=https%3A%2F%2Fgraph.microsoft.com'
        headers = {
        'Authorization': f'Bearer {self.get_user_token()}',
        'Content-Type': "application/x-www-form-urlencoded"
        }
        # sends POST request
        response = requests.request("GET", url, headers=headers)
        
        lib_items = json.loads(response.text)['value']
        
        print (f'\nThe document lib with id {drive_id} contains:')
        for item in lib_items:
            """
                dict_keys(['createdDateTime', 'eTag', 'id', 'lastModifiedDateTime', 'name', 'webUrl', 'cTag', 'size', 'createdBy', 'lastModifiedBy', 'parentReference', 'fileSystemInfo', 'folder', 'shared'])
                dict_keys(['@microsoft.graph.downloadUrl', 'createdDateTime', 'eTag', 'id', 'lastModifiedDateTime', 'name', 'webUrl', 'cTag', 'size', 'createdBy', 'lastModifiedBy', 'parentReference', 'file', 'fileSystemInfo', 'shared'])
            """
            
            print (f"\n Name: {item['name']} \n ID: {item['id']}\n WebURL: {item['webUrl']}\n")
    
    def upload_user_file(self,drive_id,file_name,type):

        # URL to upload file
        url = f"https://graph.microsoft.{self.tenant_type}/v1.0/sites/{self.user_site_id}/drives/{drive_id}/root:/{file_name}:/content"

        # get Bearer token 
        user_token = self.get_user_token()
        # open file to be uploaded
        payload=open(file_name)
        # set headers and use Bearer token
        headers = {
        'Authorization': f'Bearer {user_token}',
        'Content-Type': type
        }

        # upload file
        response = requests.request("PUT", url, headers=headers, data=payload)

        # check if response was successful 
        if response.status_code:
            print(f'code {response.status_code} File was uploaded!')
        else:
            print ('Something went wrong ...')

        return response

def main():
    print ("You have imported the Microsoft Graph REST API module directly")

if __name__ == "__main__":
    main()




