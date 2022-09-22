import subprocess

result = subprocess.run(["git","add","-p","&&","git","commit"])
return_code = result.returncode
