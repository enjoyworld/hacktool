import hashlib
id='admin'
md=hashlib.md5()
md.update(id.encode('utf-8'))
print(md.hexdigest())