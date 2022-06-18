{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Handwritten Digit Recognizer.py","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyN6C9xdf2RVBPbomLe9v2Vv"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":2,"metadata":{"id":"5XJ1CoS5ifS0","executionInfo":{"status":"ok","timestamp":1650861732159,"user_tz":-330,"elapsed":3892,"user":{"displayName":"AARON SAMUEL A","userId":"09842465037744171818"}}},"outputs":[],"source":["import pandas as pd\n","import tensorflow as tf\n","import numpy as np\n","import cv2 as cv  \n","import matplotlib.pyplot as plt\n","from tensorflow.python.keras.metrics import accuracy"]},{"cell_type":"code","source":["mnist = tf.keras.datasets.mnist\n","\n","(x_train, y_train),(x_test,y_test)=mnist.load_data()# split the data in training set as tuple\n","\n","x_train = tf.keras.utils.normalize(x_train , axis = 1)\n","x_test = tf.keras.utils.normalize(x_test , axis = 1)\n","\n","model= tf.keras.models.Sequential()\n","model.add(tf.keras.layers.Flatten(input_shape=(28,28)))\n","model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))\n","model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))\n","model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax))\n","model.compile(optimizer='adam' , loss='sparse_categorical_crossentropy',metrics=['accuracy'])\n","model.fit(x_train,y_train, epochs=5)#As the number of epochs increases beyond 11,chance of overfitting of the model on training data\n","\n","loss , accuracy  =model.evaluate(x_test,y_test)\n","print(accuracy)\n","print(loss)\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"9rkMoqtHlcpt","executionInfo":{"status":"ok","timestamp":1650863487425,"user_tz":-330,"elapsed":44341,"user":{"displayName":"AARON SAMUEL A","userId":"09842465037744171818"}},"outputId":"cea9313d-96e3-49f0-f49d-701004bf866b"},"execution_count":19,"outputs":[{"output_type":"stream","name":"stdout","text":["Epoch 1/5\n","1875/1875 [==============================] - 6s 3ms/step - loss: 0.2578 - accuracy: 0.9234\n","Epoch 2/5\n","1875/1875 [==============================] - 5s 3ms/step - loss: 0.1058 - accuracy: 0.9676\n","Epoch 3/5\n","1875/1875 [==============================] - 5s 3ms/step - loss: 0.0718 - accuracy: 0.9774\n","Epoch 4/5\n","1875/1875 [==============================] - 6s 3ms/step - loss: 0.0538 - accuracy: 0.9829\n","Epoch 5/5\n","1875/1875 [==============================] - 5s 3ms/step - loss: 0.0423 - accuracy: 0.9862\n","313/313 [==============================] - 1s 2ms/step - loss: 0.0823 - accuracy: 0.9747\n","0.9746999740600586\n","0.08231425285339355\n"]}]},{"cell_type":"code","source":["for x in range(1,4):\n","    # now we are going to read images it with open cv\n","    img=cv.imread(f'Handwritten {x}.jpg')[:,:,0]\n","    img=np.invert(np.array([img]))#invert black to white in images so that model wont get confues\n","    prediction=model.predict(img)\n","    print(\"----------------\")\n","    print(\"The predicted value is : \",np.argmax(prediction))\n","    print(\"----------------\")\n","    plt.imshow(img[0],cmap=plt.cm.binary)#change the color in black and white\n","    plt.show()\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":917},"id":"oQNqvDeClee3","executionInfo":{"status":"ok","timestamp":1650863487428,"user_tz":-330,"elapsed":28,"user":{"displayName":"AARON SAMUEL A","userId":"09842465037744171818"}},"outputId":"172ee894-7b5d-4171-c8a9-e8d20fa82d66"},"execution_count":20,"outputs":[{"output_type":"stream","name":"stdout","text":["----------------\n","The predicted value is :  3\n","----------------\n"]},{"output_type":"display_data","data":{"text/plain":["<Figure size 432x288 with 1 Axes>"],"image/png":"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\n"},"metadata":{"needs_background":"light"}},{"output_type":"stream","name":"stdout","text":["----------------\n","The predicted value is :  9\n","----------------\n"]},{"output_type":"display_data","data":{"text/plain":["<Figure size 432x288 with 1 Axes>"],"image/png":"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\n"},"metadata":{"needs_background":"light"}},{"output_type":"stream","name":"stdout","text":["----------------\n","The predicted value is :  2\n","----------------\n"]},{"output_type":"display_data","data":{"text/plain":["<Figure size 432x288 with 1 Axes>"],"image/png":"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\n"},"metadata":{"needs_background":"light"}}]}]}