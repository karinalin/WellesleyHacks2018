import io 
import os
from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Whack-eb9c97f19641.json"

client = vision.ImageAnnotatorClient()

def get_keyword(file_path):
	"""
	file_name = os.path.join( 
		os.path.dirname(__file__), 
		file_path) 
	  
	with io.open(file_name, 'rb') as image_file: 
		content = image_file.read() 

	image = types.Image(content=content) 
	"""

	image = vision.types.Image()
	image.source.image_uri = file_path

	response = client.label_detection(image=image) 
	labels = response.label_annotations 
	print labels[0].description
	keyword = labels[0].description.split(' ')[0]
	return keyword