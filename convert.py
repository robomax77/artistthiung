FILE_NAME = "https://i1.sndcdn.com/artworks-xygcn2L1yy7W86IA-suySVw-t500x500.png"

from PIL import Image
import pyperclip

def clamp(x):
  return max(0, min(x, 255))

def better_hex(r, g, b):
    return "{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))

def o_to_hex(r, g, b):
    return "%x%x%x" % (r, g, b)


handle = Image.open(FILE_NAME)
image = handle.resize((32, 32)).convert("RGB")
data = image.getdata()

payload = []

for i in data:
    payload.append(better_hex(i[0], i[1], i[2]))

print(len(payload))
payload = str(payload).replace("[", "{").replace("]", "}")
pyperclip.copy(payload)
