import requests
import json

with open('my_urls.json') as f:
    srcs = json.load(f)

# Remove repeated links
srcs = list(set(srcs))

# Download all the images from srcs and put them in output folder
for i, src in enumerate(srcs):
    print(f"Downloading {i+1}/{len(srcs)}\r", end='')
    with open(f"output/{i}.jpg", "wb") as f:
        f.write(requests.get(src).content)
