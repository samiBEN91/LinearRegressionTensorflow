
import numpy as np 
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 
import matplotlib.pyplot as plt 


#In order to make the random numbers predictable, 
#we will define fixed seeds for both Numpy and Tensorflow.
np.random.seed(101)  
#tf.random.set_seed(101)

# Genrating random linear data 
# There will be 50 data points ranging from 0 to 50 
x = np.linspace(0, 50, 50) 
y = np.linspace(0, 50, 50) 

# Adding noise to the random linear data 
x += np.random.uniform(-4, 4, 50) 
y += np.random.uniform(-4, 4, 50) 

n = len(x) # Number of data points 

# Plot of Training Data 
plt.scatter(x, y) 
plt.xlabel('x') 
plt.ylabel('y') 
plt.title("Training Data") 
plt.show() 

#Now we will start creating our model by defining the placeholders X and Y, 
#so that we can feed our training examples X and Y into the optimizer during the training process.
X = tf.placeholder("float") 
Y = tf.placeholder("float")
print ("X=",X)


#Now we will declare two trainable Tensorflow Variables for the Weights and Bias 
#and initializing them randomly using np.random.randn().
W = tf.Variable(np.random.randn(), name = "W") 
b = tf.Variable(np.random.randn(), name = "b")
print ("sami") 
print ("W=",W) 

#Now we will define the hyperparameters of the model, 
#the Learning Rate and the number of Epochs.
learning_rate = 0.01
print ("learning_rate",learning_rate)
training_epochs = 1000
print ("training_epochs",training_epochs)


#Now, we will be building the Hypothesis, the Cost Function, 
#and the Optimizer. We won’t be implementing the Gradient Descent Optimizer 
#manually since it is built inside Tensorflow. After that, we will be initializing the Variables.

# Hypothesis 
y_pred = tf.add(tf.multiply(X, W), b)
print ("y_pred=",y_pred) 

# Mean Squared Error Cost Function 
cost = tf.reduce_sum(tf.pow(y_pred-Y, 2)) / (2 * n)
print ("cost=",cost)
  
# Gradient Descent Optimizer 
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) 
print ("optimizer=",optimizer)
  
# Global Variables Initializer 
init = tf.global_variables_initializer() 

#Now we will begin the training process inside a Tensorflow Session.

# Starting the Tensorflow Session 
with tf.Session() as sess: 
    
    # Initializing the Variables 
    sess.run(init) 
    
    # Iterating through all the epochs 
    for epoch in range(training_epochs): 
        
        # Feeding each data point into the optimizer using Feed Dictionary 
        for (_x, _y) in zip(x, y): 
            sess.run(optimizer, feed_dict = {X : _x, Y : _y}) 
        
        # Displaying the result after every 50 epochs 
        if (epoch+1 ) % 50 == 0: 
            # Calculating the cost a every epoch 
            c = sess.run(cost, feed_dict = {X : x, Y : y}) 
            print("Epoch", (epoch + 1), ": cost =", c, "W =", sess.run(W), "b =", sess.run(b)) 
    
    # Storing necessary values to be used outside the Session 
    training_cost = sess.run(cost, feed_dict ={X: x, Y: y}) 
    weight = sess.run(W) 
    bias = sess.run(b)

# Calculating the predictions 
predictions = weight * x + bias 
print("Training cost =", training_cost, "Weight =", weight, "bias =", bias, '\n')

#end