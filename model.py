import tensorflow as tf
import numpy as np
from com_in_ineuron_ai_utils.utils import return_model

class_list=['Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 'Broccoli', 
        'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 'Papaya', 'Potato', 
        'Pumpkin', 'Radish', 'Tomato']
model = return_model()
model.load_weights("TL_TF_VGG.h5")
imagename = "./inputImage.jpg"
test_image = tf.keras.preprocessing.image.load_img(imagename, target_size = (224, 224))
test_image = tf.keras.preprocessing.image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
result=np.argmax(result)
print(result)