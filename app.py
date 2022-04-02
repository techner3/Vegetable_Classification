from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage, return_model
from predictor import Model
from logger import getLog


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

logger=getLog('clientApp.py')


#@cross_origin()
class ClientApp:
    def __init__(self):

        try: 
            self.filename = "inputImage.jpg"
            self.classifier = Model(self.filename)
            logger.info("ClientApp object initialized")

        except Exception as e:
            logger.exception(f"Failed to initialize App Object : \n{e}")
            raise Exception("Failed to initialize App Object")



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():

    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.prediction()
        return jsonify(result)

    except Exception as e:
        return jsonify(e)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    #app.run(host='0.0.0.0', port=port)
    app.run()
