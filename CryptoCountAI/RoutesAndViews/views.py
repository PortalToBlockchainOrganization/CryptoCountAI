from django.http import HttpResponse

def hello_world(request):
    print("Hello, world!")
    return HttpResponse("Hello, world!")



import tensorflow as tf

def typeModelLayer1(request):
    # load the model
    model = tf.keras.models.load_model('my_model.h5')

    #load the transaction pipeline
    
    # evaluate the model
    #loss, accuracy = model.evaluate(x_test, y_test)

    # make predictions
    predictions = model.predict(transaction)
    
    
