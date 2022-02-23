import requests

img = 'images.jpeg'

url = 'https://pl-ml.herokuapp.com/api'
my_img = {'image': open(img, 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())