import subprocess

#process = subprocess.run(["git","add","-p","&&","git","commit"])

commd = "git add -p && git commit"
commdfixed = "git add -p && git diff-index --quiet HEAD || git commit -m 
'bla'"

def runcommand (cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    return proc.returncode, std_out, std_err

def main():
    print("==================================================");
    print('Running "ls -lh"...');
    print("==================================================");
    code, out, err = runcommand("ls -lh");
    print("Return code: {}".format(code));
    print("--------------------------------------------------");
    print("stdout:");
    print(out);
    print("--------------------------------------------------");
    print("stderr:");
    print(err);
    print("--------------------------------------------------");

    print("==================================================");
    print('Running parameter command...');
    print("==================================================");
    code, out, err = runcommand(commdfixed);
    print("Return code: {}".format(code));
    print("--------------------------------------------------");
    print("stdout:");
    print(out);
    print("--------------------------------------------------");
    print("stderr:");
    print(err);
    print("--------------------------------------------------");
    
if __name__ == '__main__':
    main()
