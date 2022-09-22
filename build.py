import subprocess


print subprocess.check_output('git add -p && git commit', shell = True)

result = subprocess.run(["git","add"])
text = result.communicate()[0]
return_code = result.returncode
