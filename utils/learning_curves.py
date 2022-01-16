import matplotlib.pyplot as plt

def plot_learning_curves(train_acc, validation_acc, train_loss, validation_loss, fine_tune_epoch = None):
	plt.figure(figsize = (15, 10))

	plt.subplot(2, 1, 1)
	plt.plot(train_acc, label = 'Training Accuracy')
	plt.plot(validation_acc, label = 'Validation Accuracy')
	if fine_tune_epoch:
		plt.plot([fine_tune_epoch, fine_tune_epoch], plt.ylim(), label = 'Start Fine Tuning')
	plt.xlabel('Epochs')
	plt.legend()
	plt.title('Training and Validation Accuracy')

	plt.subplot(2, 1, 2)
	plt.plot(train_loss, label = 'Training Loss')
	plt.plot(validation_loss, label = 'Validation Loss')
	if fine_tune_epoch:
		plt.plot([fine_tune_epoch, fine_tune_epoch], plt.ylim(), label = 'Start Fine Tuning')
	plt.xlabel('Epochs')
	plt.legend()
	plt.title('Training and Validation Loss')

	plt.show()
