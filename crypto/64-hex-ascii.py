import base64

base_str = 'Hello World!!'

# base64 encode
def enc_base64(s):
  return base64.b64encode(s.encode('utf-8')).decode('utf-8')

# base64 decode
def dec_base64(s):
  return base64.b64decode(s).decode('utf-8')

base64_enc = enc_base64(base_str)
base64_dec = dec_base64(base64_enc)

print(base64_enc+'\n'+base64_dec)

# ascii encode
def enc_ascii(s):
  return ' '.join(str(ord(c)) for c in s)

# ascii decode
def dec_ascii(ascii_str):
  return ''.join(chr(int(num)) for num in ascii_str.split())

ascii_enc = enc_ascii(base_str)
ascii_dec = dec_ascii(ascii_enc)

print(ascii_enc+'\n'+ascii_dec)

# hex encode
def enc_hex(s):
  return s.encode('utf-8').hex()

# hex decode
def dec_hex(hex_str):
  return bytes.fromhex(hex_str).decode('utf-8')

hex_enc = enc_hex(base_str)
hex_dec = dec_hex(hex_enc)

print(hex_enc+'\n'+hex_dec)

"""
SGVsbG8gV29ybGQhIQ==
Hello World!!
72 101 108 108 111 32 87 111 114 108 100 33 33
Hello World!!
48656c6c6f20576f726c642121
Hello World!!
"""