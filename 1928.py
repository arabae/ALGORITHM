import base64

a = "TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u"
a = a.encode()
print(a)
b = base64.decodebytes(a)
print(b.decode('ascii'))