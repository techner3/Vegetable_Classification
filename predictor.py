import numpy as np
import tensorflow as tf
from com_in_ineuron_ai_utils.utils import return_model

class Model:
    def __init__(self,filename):
        self.filename =filename
        self.class_list=['Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 'Broccoli', 
        'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 'Papaya', 'Potato', 
        'Pumpkin', 'Radish', 'Tomato']

    def prediction(self):
        model = return_model()
        model.load_weights("TL_TF_VGG.h5")
        imagename = self.filename
        test_image = tf.keras.preprocessing.image.load_img(imagename, target_size = (224, 224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        prediction=self.class_list[np.argmax(result)]
        return [{ "image" : prediction}]