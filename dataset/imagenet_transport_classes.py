import pandas as pd
import random

# Read classes_in_imagenet.txt into a dataframe 
imagenet_classes = pd.read_csv('classes_in_imagenet.txt', sep = ',')

# Read transport_list.txt into a list
file = open('transport_list.txt', 'r')
content = file.read()
transport_list = content.split('\n')

# Replace '_' in with ' '
transport_list = [' '.join(transport.split('_')) for transport in transport_list]

# 
transport_synid = list()
not_transport_synid = list()

# Iterate over all rows in the imagenet_classes dataset and remove the ones that are not modes of transport.
for idx, class_name in enumerate(imagenet_classes['class_name']):
	if class_name in transport_list and imagenet_classes.loc[idx, 'flickr_urls'] != 0:
		transport_synid.append(imagenet_classes.loc[idx, 'synid'])
	else:
		not_transport_synid.append(imagenet_classes.loc[idx, 'synid'])


# Randomly select 500 classes from more than 21000 non-transport classes
not_transport_synid = random.sample(not_transport_synid, 500)

transport_synid_textfile = open('transport_synid_textfile.txt', 'w')

for element in transport_synid:
	transport_synid_textfile.write(element + '\n')

not_transport_synid_textfile = open('not_transport_synid_textfile.txt', 'w') 

for element in not_transport_synid:
	not_transport_synid_textfile.write(element + '\n')

