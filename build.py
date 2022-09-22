import subprocess

process = subprocess.run(["git","add","-p","&&","git","commit"])
stdout, stderr = process.communicate()
exit_code = process.wait()
print(stdout, stderr, exit_code)
