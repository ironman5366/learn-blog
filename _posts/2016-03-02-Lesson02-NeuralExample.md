---
authors:
    - beddow
---

## Lesson 02 - A basic neural network example

Welcome back to learn-blog

Today, we'll give you exactly what I always wanted when learning machine learning.

A **good** example.

Let me explain a bit further.

When searching for an example of beginner-level code, I'm looking for three things.

- Easy to Install
  - A lot of popular libraries are really hard to install. And this isn't help by a write-once approach to installing (e.g. tensorflow binaries only are compatible with up to python 3.5). We feel your pain here. That's why we're providing a simple requirements.txt that should work to install.

- Code that's simple to run, and easy to understand
  - Examples that use things like MNIST are great in theory, but they can be hard to re-use for other applications. They also require downloading, and are kind of advanced for an introduction. That's why we'll just teach it how to add, using data we generate **inside** the code

- Up to date
  - Most of the tutorials that are easy to install **and** easy to run use some ancient machine learning library that only supports basic models. We're addressing this by using [Keras](https://keras.io) an amazing library that provides an easy to use high level API for some of the most modern machine learning libraries. So even if, in a few years, tensorflow is out of date, our keras code will still work with another Keras backend.

## Installing

As stated above, our installation is handled by an updated `requirements.txt`, using Python 3.6

To install the dependencies:
```
git clone https://github.com/ironman5366/learn-blog
cd learn-blog/examples
pip install -r requirements.txt
```
Our requirements.txt is available [In the examples folder of the repository](https://github.com/ironman5366/learn-blog/blob/master/examples/requirements.txt)

That `examples` folder also contains all the example networks that we write, including the one we're writing here, which will be in `examples/add_network.py`. If you're impatient, you can see the full code [here.](https://github.com/ironman5366/learn-blog/blob/master/examples/add_network.py)

## The code

### Imports
Let's start by importing the Keras layers and activations we'll be using, as well as numpy and the random library

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import random
```


## Data

To train any network, we need a good dataset. For this network, we just want to teach it how to add. So we'll generate a bunch of sample inputs and outputs, that look like this:

```python
#Sample Inputs
# [[1,2]]
#Sample Outputs
# [[3]]
```
We'll need a lot more data than just that, though. Let's generate it.

```python
sample_inputs = []
sample_outpus = []
#A list of numbers from 1 to 100. We'll pick random numbers from here to make our examples
hundred_nums = list(range(1,100)) #Nums 100
#Generate 100k sample data points. Wow!
for num in range(100000):
  #Pick two random numbers, and append them to i. Add them, and append the result to o.
	num_1 = random.choice(hundred_nums)
	num_2 = random.choice(hundred_nums)
	i = [num_1,num_2]
	o = [num_1+num_2]
  #Put the input numbers in sample_inputs, and the output numbers in sample_outputs
	sample_inputs.append(i)
	sample_outputs.append(o)
```

There we go. Now, we'll convert them to a numpy list, that's the "vector" that you'll input.

```python
X = np.array(sample_inputs)
Y = np.array(sample_outputs)
```

We have our data. To summarize, `X` is 100,000 lists of 2 numbers each, and `Y` is 100,000 lists of 1 number each.

If you added the line `print(X.shape, Y.shape)` right here, you'd see `(100000, 2) (100000, 1)`.

We have everything we need to make our network

## Layers and models

The base of a Keras network is the `model`.

The most common one, and what we'll be using all of our tutorials, is the `Sequential` model.

This is basically just a stack of "layers", or operations to perform on the neuron.

You can picture it like a pipe.

You define how much "water" (your data), goes in, and in what shape, it gets manipulated in the middle (although you don't see that, hence the term `hidden` layer), and then finally it comes out in a certain shape.

For this tutorial we'll only use one layer.

Let's define it.

We'll make a `Sequential` model, and create a single `Dense` layer with information about our data

```python
model = Sequential()
#Add a dense model, with an input length of 2 (like [1,2]) and an output length of 1 (like [3])
model.add(Dense(input_dim=2, output_dim=1))
```
Great. If you were dealing with a more advanced model you would add cool stuff like softmax regression here, but since we're doing something pretty simple we can just go straight to compiling the model.

```python
model.compile(optimizer='adadelta',
          loss='mae',
          metrics=['accuracy'])
```

This part of the code may seem pretty intimidating, but it's actually not that hard to understand once you break it down.

First, we set the optimizer. Keras provides a number of different methods for this, and it's usually a good idea to play around with them and figure out which is best for your model. You can find the complete list [here.](https://keras.io/optimizers/)

Next, we'll set the loss. This just defines how to calculate the success of the algorithm. For this simple model, the best method is `mae`, or `mean absolute error`. You can find a complete list of loss methods [here.](https://keras.io/objectives/).

Finally, we'll set the metrics. We want to see the accuracy of the algorithm... and that's about it.
You can find a complete list of metrics [here.](https://keras.io/metrics/)

All these links are also available as the Keras section of our useful links page.

Now, let's train the model. The first two arguments are just the input data and the output data, our `X` and `Y`.

Next, we'll set the `validation_split`. The validation split is the portion of your data that should **just** be tested on, not trained. This makes sure that there's not any erroneous relations that will only work for your training data.

Finally, we set `nb_epoch`. This is just the number of cycles to run it for. For this, 10 should probably be fine.

```python
#Split the data to validate the results
model.fit(X, Y, validation_split=0.3,nb_epoch=5)
```

The training output in your console should look something like this:

```
Epoch 1/5
70000/70000 [==============================] - 3s - loss: 34.5730 - acc: 0.0384 - val_loss: 0.4594 - val_acc: 0.5836
Epoch 2/5
70000/70000 [==============================] - 3s - loss: 0.1344 - acc: 0.9758 - val_loss: 0.0658 - val_acc: 1.0000
Epoch 3/5
70000/70000 [==============================] - 2s - loss: 0.0562 - acc: 1.0000 - val_loss: 0.0596 - val_acc: 1.0000
Epoch 4/5
70000/70000 [==============================] - 3s - loss: 0.0697 - acc: 1.0000 - val_loss: 0.0517 - val_acc: 1.0000
Epoch 5/5
70000/70000 [==============================] - 3s - loss: 0.0781 - acc: 1.0000 - val_loss: 0.0625 - val_acc: 1.0000
```

You can see that over time the loss, or error, get's smaller and the accuracy grows.

The validation accuracy (`val_acc`), which represents the accuracy of the training data we separated with `validation_split`, also grows, showing us that our model should work on data that it wasn't trained with.

And that's it! You just trained your model! We'll test it in a second, but let's save it first

```python
model.save("addition_model")
```

Now that that's taken care of, let's try it out. Remember it expects a list of lists, so that's how we'll set it up

```python
while True:
	i = np.array([eval(input(">"))])
	answer = model.predict(i)
	print (answer)
```

Here's a couple example inputs and outputs. Your results will probably vary ever so slightly, but that's to be expected based on how neural networks work.

```
>[2,4]
[[ 5.99304199]]
>[1,2]
[[ 2.99416757]]
>[100,300]
[[ 399.88665771]]
>[5366,27]
[[ 5386.53808594]]
>
```
It's not perfect, and when it gets into the bigger numbers that we didn't train on it staggers a bit. But for a neural network trained with a single layer, it's pretty dang accurate.

If you want try out this example, here's the full code:

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import random

sample_inputs = []
sample_outputs = []
hundred_nums = list(range(1,100)) #Nums 100
#Lets generate some data
for num in range(100000):
	num_1 = random.choice(hundred_nums)
	num_2 = random.choice(hundred_nums)
	i = [num_1,num_2]
	o = [num_1+num_2]
	sample_inputs.append(i)
	sample_outputs.append(o)


X = np.array(sample_inputs)
Y = np.array(sample_outputs)


model = Sequential()
model.add(Dense(input_dim=2, output_dim=1))
model.compile(optimizer='adadelta',
          loss='mae',
          metrics=['accuracy'])

#Split the data to validate the results
model.fit(X, Y, validation_split=0.3,nb_epoch=5)

model.save("addition_model")

while True:
	i = np.array([eval(input(">"))])
	answer = model.predict(i)
	print (answer)
```

As mentioned earlier, it, as well as our requirements.txt and all our examples, are available [in the examples folder.](https://github.com/ironman5366/learn-blog/tree/master/examples)
