
import mgraph_restapi as msgraph
from dotenv import load_dotenv 
import os 
load_dotenv()
# # dotenv_path = Path('path/to/.env')
# load_dotenv(dotenv_path=dotenv_path)

load_dotenv() # loads env variables from local .env file

my_spconn = msgraph.mgraph_rest_conn(os.environ['CLIENT_ID'],os.environ['SITE_ID'],os.environ['CLIENT_SECRET'],os.environ['TENANT_ID'],'com')
# my_spconn.list_doc_libs()
my_spconn.list_doc_lib_items('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# my_spconn.upload_user_file("b!GoMzd6NImEKkS7h8psO1Mal-S2J3q-1Jvy3dfVof4t2c7wenMrV6SoA4cZEqE54K","file_toupload.txt","text/plain")