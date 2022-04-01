import numpy as np
import tensorflow as tf
from com_in_ineuron_ai_utils.utils import return_model
from logger import getLog

logger=getLog('predictor.py')

class Model:
    def __init__(self,filename):

        try:
            self.filename =filename
            self.class_list=['Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 'Broccoli', 
        'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 'Papaya', 'Potato', 
        'Pumpkin', 'Radish', 'Tomato']

        except Exception as e:
            logger.exception(f"Failed to initialize Model Object : \n{e}")
            raise Exception("Failed to initialize Model Object")

    def prediction(self):

        try:
            model = return_model()
            logger.info("Model Created")
            model.load_weights("TL_TF_VGG.h5")
            logger.info("Weights loaded")
            imagename = self.filename
            test_image = tf.keras.preprocessing.image.load_img(imagename, target_size = (224, 224))
            logger.info("Image loaded")
            test_image = tf.keras.preprocessing.image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = model.predict(test_image)
            logger.info("Prediction Completed")
            prediction=self.class_list[np.argmax(result)]
            return [{ "image" : prediction}]

        except Exception as e:
            logger.exception(f"Failed to make a prediction : \n{e}")
            raise Exception("Failed to make a prediction")