import sys

def success():
    print("==> Exiting with standard success exit code")
    sys.exit(0)
    #return None

def failure():
    print("==> Exiting with standard failure exit code")    # Syntax Error
    sys.exit(1)
    return None

if __name__ == "__main__":

    method_name = sys.argv[1]
    print(method_name)

    if method_name == 'success':
        success()
    else:
        failure()
