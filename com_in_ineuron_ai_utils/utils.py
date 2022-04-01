import base64
import tensorflow as tf

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())


def return_model():
  vgg=tf.keras.applications.vgg16.VGG16(include_top=False, weights=None,input_shape=(224,224,3))
  x=tf.keras.layers.Flatten()(vgg.output)
  x = tf.keras.layers.Dense(128, activation='relu')(x)
  x=tf.keras.layers.Dropout(0.2)(x)
  prediction=tf.keras.layers.Dense(15, activation='softmax')(x)
  model = tf.keras.models.Model(inputs=vgg.input, outputs=prediction)
  return model