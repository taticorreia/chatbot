import joblib

if __name__ == '__main__':
    frase = input('Oi, em que posso te ajudar? ')
    
    vectorizer = joblib.load('vectorizer.joblib')
    
    X = vectorizer.transform(frase)
    
    print(X)