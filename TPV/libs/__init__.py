import  os
os.environ["KVS_FILES"] = os.path.join(os.path.dirname(__file__), "kvs")
from .sing_up import SingUp
from .sing_in import SingIn
from .app_main import  AppMain