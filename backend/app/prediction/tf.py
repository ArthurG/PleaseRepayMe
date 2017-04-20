import numpy as np
import pandas as pd
import json
from glob import glob


import tensorflow as tf

lines = []
for f_name in glob('/mnt/3F5127B6515F1249/reddit/linked_with_comments/part-00*'):
   f = open(f_name, 'r')
   lines.extend(f.read().split("\n")[:-1])
df = pd.DataFrame.from_records(map(json.loads, lines))
df.drop(["borrower", "author", "currency", "lender","repaid_thread_body","repaid_thread_id","repaid_thread_name","repaid_thread_start_date", "repaid_thread_title"], 1,inplace=True)
df.fillna(0, inplace=True)

#feature = df.drop("repaid", 1)
#label = df["repaid"].get_dummies(train["repaid"].map(lambda x:1 if x == "true" else 0))
#1example_batch, label_batch = tf.train.shuffle_batch(
#[feature, label])

train = df.sample(frac=0.8)
train_x = train.drop("repaid", 1)
train_y = pd.get_dummies(train["repaid"].map(lambda x:1 if x == "true" else 0))
test = df.drop(train.index)
test_x = test.drop("repaid", 1)
test_y = pd.get_dummies(test["repaid"].map(lambda x: 1 if x == "true" else 0))

#train_x = feature.sample(frac = 0.8)
###st_x = feature.drop(train.index)

#train_y = label.sample(frac = 0.8)
#test_y = feature.drop(train.index)

print(len(train_x))

# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1
cols = len(train_x.columns)
outputs = 2

# tf Graph Input
x = tf.placeholder(tf.float32, [None, cols]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, outputs]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([cols, outputs]))
b = tf.Variable(tf.zeros([outputs]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimize error using cross entropy
#cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
cost = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred) 
# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.initialize_all_variables()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(len(train_x)/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs = np.array_split(train_x.as_matrix()[:2900], total_batch)[i]
            batch_ys = np.array_split(train_y[:2900], total_batch)[i]
            l = np.reshape(batch_ys, [len(batch_ys), outputs])

            
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs,
                                                          y: l})
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        #if (epoch+1) % display_step == 0:
        #    print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    test_y_2 = np.reshape(test_y, [len(test_y), outputs])
    print("Accuracy:", accuracy.eval({x: test_x.as_matrix(), y: test_y_2}))

