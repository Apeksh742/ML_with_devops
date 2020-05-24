import pandas as  pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

dataset = pd.read_csv("Placement_Data_Full_Class.csv")
dataset = pd.get_dummies(dataset, drop_first=True)

X = dataset[['ssc_p', 'hsc_p', 'degree_p', 'etest_p', 'mba_p',
       'gender_M', 'ssc_b_Others', 'hsc_b_Others', 'hsc_s_Commerce',
       'hsc_s_Science', 'degree_t_Others', 'degree_t_Sci&Tech', 'workex_Yes',
       'specialisation_Mkt&HR']]

y = dataset['status_Placed']
epochs=10

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.30, random_state=42)

model = Sequential()
model.add(Dense(input_shape=(14,), units=225, activation='relu'))
model.add(Dense(units=116, activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])


fit_model=model.fit(X_train,y_train, epochs=epochs, verbose=None)
accuracy=fit_model.history.get('accuracy')[-1]

f = open("accuracy.txt","w+")
f.write(str(accuracy*100))
f.close()
print("Accuracy for the model is : " , accuracy ,"%")

