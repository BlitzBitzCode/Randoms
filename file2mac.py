import sys
import hashlib


def display_help():
    print("file2mac.py:")
    print("python3 fil2mac.py HASHALGORITHM FILENAME")
    sys.exit()

def display_algorithms():
    print("displaying algorithms")
    algorithmCount = len(hashlib.algorithms_available)
    algorithms = hashlib.algorithms_available
    count = 0
    while count < algorithmCount:
        print(str(count) + "\t - " + algorithms.pop())
        count += 1
    sys.exit()

def get_message_digest(algo, target):
    try:
        msgdigest = hashlib.new(algo)
        f = open(target, 'rb')
        data = bytes(f.read())
        f.close()
        msgdigest.update(data)
        hash = msgdigest.hexdigest()
        print("File: " + target)
        print("Hash: " + hash)
    except OSError as osEx:
        print("File:    \'" + target + "\' not found")
        print("Message: " + osEx)
    finally:
        sys.exit()

if __name__ == "__main__":
    params = sys.argv

    if len(params)== 1:
        display_help()
    elif len(params) == 2:
        param1 = sys.argv[0]
        param2 = sys.argv[1]        
        if param2 == "--list":
            display_algorithms()
        elif param2 == "--help":
            display_help()
        else:
            sys.exit()
    elif len(params) == 3:
        get_message_digest(sys.argv[1], sys.argv[2])
    else:
        pass
