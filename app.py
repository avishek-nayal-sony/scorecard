import hashlib

# Create password hashes
def hash_pass(passw):
    # Below Line(28). Code has High Severity Issue
    m = hashlib.md5()
    # Below Line(30). Fix of High Severity Issue
    m = hashlib.sha256() #using SHA-256 
    m = hashlib.sha256() #using SHA-256 
    m = hashlib.sha256() #using SHA-256....
    m.update(passw.encode('utf-8'))
    return m.hexdigest()
