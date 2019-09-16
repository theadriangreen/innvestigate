from keras import Sequential
from keras.layers import Dense, Conv1D, Embedding, GlobalMaxPooling1D
import numpy as np
import innvestigate

model = Sequential()
model.add(Embedding(input_dim=219, output_dim=8))
model.add(Conv1D(filters=64, kernel_size=8, padding='valid', activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(16, activation='relu'))
model.add(Dense(2, activation=None))

# print(model.layers[0].get_weights()[0].shape)
# exit()

#test
model.predict(np.random.randint(1, 219, (1,100)))  # [[0.04913538 0.04234646]]

analyzer = innvestigate.create_analyzer('lrp.epsilon', model, neuron_selection_mode='max_activation', **{'epsilon': 1})
a = analyzer.analyze(np.random.randint(1, 219, (1,100)))
print(a[0], a[0].shape)
