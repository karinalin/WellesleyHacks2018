import io 
import os
from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types

def detect

features = [
	types.Feature(type=enums.Feature.Type.LABEL_DETECTION),
    types.Feature(type=enums.Feature.Type.TEXT_DETECTION),
    types.Feature(type=enums.Feature.Type.WEB_DETECTION),
    types.Feature(type=enums.Feature.Type.SAFE_SEARCH_DETECTION),
]

client = vision.ImageAnnotatorClient()

requests = []
for filename in ['trump.jpeg', 'not_cat.jpg', 'cat.jpeg']:
    with open(filename, 'rb') as image_file:
        image = types.Image(
            content=image_file.read())
    request = types.AnnotateImageRequest(
        image=image, features=features)
    requests.append(request)

response = client.batch_annotate_images(requests)

for annotation_response in response.responses:
	webDetect = annotation_response.web_detection
	entities = webDetect.web_entities
	for entity in entities:
		if 'Trump' in entity.description:
			print 'Trump found'
