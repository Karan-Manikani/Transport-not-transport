import os
import shutil

IMAGES_DIR = '../images/'
TRANSPORT_DIR = os.path.join(IMAGES_DIR, 'transport/')
NOT_TRANSPORT_DIR = os.path.join(IMAGES_DIR, 'not_transport/')


def shuttle_images(directory):
	image_count = 0
	for DIR in os.listdir(directory):
		DIR_PATH = os.path.join(directory, DIR)
		for FILE in os.listdir(DIR_PATH):
			NEW_FILENAME = DIR + FILE
			os.rename(os.path.join(DIR_PATH, FILE), os.path.join(DIR_PATH, NEW_FILENAME)) 
			FILE = os.path.join(DIR_PATH, NEW_FILENAME)
			shutil.move(FILE, directory)
			image_count += 1
		os.rmdir(DIR_PATH)

	print('Total images moved:', image_count)


if __name__ == '__main__':
	shuttle_images(TRANSPORT_DIR)
	shuttle_images(NOT_TRANSPORT_DIR)