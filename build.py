import subprocess

result = subprocess.run(["git","add","-p","&&","git","commit"])
text = result.communicate()[0]
return_code = result.returncode
