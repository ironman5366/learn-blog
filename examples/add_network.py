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
