import subprocess
import tensorflow as tf 
import os

#subprocess.call(["source","/tool/tensorlow/bin/activate"],shell = True)
#os.system('. ./tool/tensorflow/bin/activate')

hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
sess.run(hello)
a = tf.constant(10)
b = tf.constant(32)
sess.run(a + b)

sess.close()


