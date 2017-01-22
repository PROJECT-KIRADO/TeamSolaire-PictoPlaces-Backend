import json
from clarifai import rest
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp


app = ClarifaiApp("GTF60JGAGKtuJhxp6tjiRGzZtbAx3jTF2Coywz-m","1xRtAJg1X6waDzo0WfNSSlpik5FOG2uAJcSj6Ym7")
model = app.models.get('general-v1.3')
image = ClImage(url='http://www.founderspublications.com/wp-content/uploads/2014/12/Round-Pencil.jpg')
data = model.predict([image])
print json.dumps(data)

app.auth.get_token()
