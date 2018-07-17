# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:10:04 2018

@author: jdonovc
"""

# Python 3.5

import tensorflow as tf
from sklearn.datasets import load_iris

iris = load_iris()['data']
iris_labs = load_iris()['target']

x = tf.placeholder(tf.float32, shape=iris.shape)

w1 = tf.get_variable(name='w1', shape=[4,2], initializer=tf.random_normal_initializer())
b1 = tf.get_variable(name='b1', shape=[2], initializer=tf.constant_initializer(0))
a1 = tf.nn.sigmoid(tf.matmul(x, w1)+b1)

w2 = tf.get_variable(name='w2', shape=[2,4], initializer=tf.random_normal_initializer())
b2 = tf.get_variable(name='b2', shape=[4], initializer=tf.random_normal_initializer())
a2 = tf.matmul(a1, w2)+b2

loss = tf.reduce_mean(tf.pow(x-a2, 2))
optimizer = tf.train.RMSPropOptimizer(0.001).minimize(loss)

init = tf.global_variables_initializer()

a = []
a2s = []
with tf.Session() as sess:
    sess.run(init)
    for i in range(1, 100001):
        if i%10000==0:
            print(i)
        _, losser, new_iris, compressed = sess.run([optimizer, loss, a2, a1], feed_dict={x:iris})
        a.append(losser)
       
import pandas as pd
import matplotlib.pyplot as plt
compress_df = pd.DataFrame(compressed)
compress_df['labels'] = iris_labs
compress0, compress1, compress2 = (compress_df[compress_df['labels']==num][[0,1]] for num in range(3))
plt.scatter(compress0.iloc[:,0], compress0.iloc[:,1], c='red', marker='+')
plt.scatter(compress1.iloc[:,0], compress1.iloc[:,1], c='green', marker='o')
plt.scatter(compress2.iloc[:,0], compress2.iloc[:,1], c='blue', marker='x')