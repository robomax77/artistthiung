from PIL import Image
import pyperclip

def o_to_hex(r, g, b):
    return "%x%x%x" % (r, g, b)



handle = Image.open("george.jpg")
image = handle.resize((32, 32)).convert("RGB")
data = image.getdata()

payload = []

for i in data:
    payload.append(o_to_hex(i[0], i[1], i[2]))

print(len(payload))
payload = str(payload).replace("[", "{").replace("]", "}")
pyperclip.copy(payload)
