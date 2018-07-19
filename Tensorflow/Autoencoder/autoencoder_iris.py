# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:10:04 2018

@author: jdonovc
"""

# Python 3.5

import tensorflow as tf
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # load iris dataset
    loader = load_iris()
    iris = loader['data']
    iris_labs = loader['target']
    return iris, iris_labs

def encoder(input_data):
    # placeholder for input data
    tf.reset_default_graph()
    x = tf.placeholder(tf.float32, shape=input_data.shape)
    # defining hidden layer - 2 nodes given by weights w1 and bias b1
    # sigmoid activation a1
    w1 = tf.get_variable(name='w1', shape=[4,2], initializer=tf.random_normal_initializer(seed=42))
    b1 = tf.get_variable(name='b1', shape=[2], initializer=tf.constant_initializer(0))
    a1 = tf.nn.sigmoid(tf.matmul(x, w1)+b1)
    return x, a1

def decoder(activation):
    # output layer - 4 nodes given by weights w2 and bias b2 - no non-linear activation
    # activation = result of sigmoid activation from hidden layer
    w2 = tf.get_variable(name='w2', shape=[2,4], initializer=tf.random_normal_initializer(seed=42))
    b2 = tf.get_variable(name='b2', shape=[4], initializer=tf.constant_initializer(0))
    a2 = tf.matmul(activation, w2)+b2
    return a2

def training(learning_rate, num_epochs):
    iris_x, iris_y = load_data()
    x, a1 = encoder(iris_x)
    a2 = decoder(a1)
    # Mean Squared Error Loss + RMSProp optimizer with learning rate = 0.001
    loss = tf.reduce_mean(tf.pow(x-a2, 2))
    optimizer = tf.train.RMSPropOptimizer(0.001).minimize(loss)
    init = tf.global_variables_initializer()
    # train model for 100,000 epochs
    a = []
    with tf.Session() as sess:
        sess.run(init)
        for i in range(1, num_epochs+1):
            if i%10000==0:
                print(str(i), 'epochs done')
            _, losser, new_iris, compressed = sess.run([optimizer, loss, a2, a1], feed_dict={x:iris_x})
            a.append(losser)
    return a, iris_x, new_iris, compressed

def plot2d_iris(compress_data):
    # compress_data = 2D array of compressed iris data
    # plot this data
    compress_df = pd.DataFrame(compress_data)
    compress_df['labels'] = load_data()[1]
    compress0, compress1, compress2 = (compress_df[compress_df['labels']==num][[0,1]] for num in range(3))
    plt.scatter(compress0.iloc[:,0], compress0.iloc[:,1], c='red', marker='+')
    plt.scatter(compress1.iloc[:,0], compress1.iloc[:,1], c='green', marker='o')
    plt.scatter(compress2.iloc[:,0], compress2.iloc[:,1], c='blue', marker='x')

loss_list, original_iris, approx_iris, compressed_iris = training(0.001, 100000)
print(loss_list[0], loss_list[-1]) # initial loss vs loss after training
plot2d_iris(compressed_iris)
# setosa = 0 = red
# versicolor = 1 = green
# virginica = 2 = blue