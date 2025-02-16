from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data = {
    'injury': ['Labrum tear', 'ACL tear', 'Sprained ankle', 'Fractured arm', 'Torn muscle'],
    'rehab': ['Rest and physiotherapy', 'Surgery and physiotherapy', 'Rest and ice therapy', 
              'Surgery and physiotherapy', 'Rest and physiotherapy']
}

injury_encoder = LabelEncoder()
rehab_encoder = LabelEncoder()

X = injury_encoder.fit_transform(data['injury']).reshape(-1, 1)  
y = rehab_encoder.fit_transform(data['rehab'])                  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

def predict_rehab(user_injury):
    
    user_injury_encoded = injury_encoder.transform([user_injury])
    rehab_prediction = clf.predict(user_injury_encoded.reshape(-1, 1))
    rehab_result = rehab_encoder.inverse_transform(rehab_prediction)
    return rehab_result[0]

user_injury = input("Enter the injury: ")
predicted_rehab = predict_rehab(user_injury)
print(f"For the injury '{user_injury}', the recommended rehab is: {predicted_rehab}")
