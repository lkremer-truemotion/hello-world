import subprocess

result = subprocess.Popen("git add -p && git commit")
text = result.communicate()[0]
return_code = result.returncode
