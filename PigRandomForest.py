import joblib

class PigRandomForest:
    def __init__(self):
        pass

    def load_model(self, filename:str):
        print("[ ]Loading model",filename,"...")
        self.lr = joblib.load(filename)
        #print("[✓]Loaded model",filename)
        return self

    def predict(self, data):
        #print("[ ]Predict data",[data])
        if not all(-0.1 <= val <= 0.1 for val in data):
            p = self.lr.predict([data])
        else:
            p = 0
        #print("[✓]Predict data",[data], p)
        return p

    # def train(self, filename:str, output_filename:str):
    #     datasets = pd.read_csv(filename)
    #     X = datasets.iloc[:, [0,1,2]].values
    #     Y = datasets.iloc[:, 3].values
    #     X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.3, random_state = 42, stratify=Y)

    #     # Feature Scaling
    #     '''
    #     from sklearn.preprocessing import StandardScaler
    #     sc_X = StandardScaler()
    #     X_Train = sc_X.fit_transform(X_Train)
    #     X_Test = sc_X.transform(X_Test)
    #     '''
    #     # Fitting the classifier into the Training set


    #     classifier = RandomForestClassifier(n_estimators = 200, criterion = 'gini', random_state = 42)
    #     classifier.fit(X_Train,Y_Train)

    #     # Predicting the test set results

    #     joblib.dump(classifier, output_filename)
    #     lr = joblib.load(output_filename)
    #     Predict = lr.predict(X_Test)
    #     print(X_Test)
    #     print('Predict : ', Predict)

    #     # plot learning curve
    #     train_results = []
    #     test_results = []
    #     list_nb_trees = [1, 5, 10, 15, 30, 45, 60, 80, 100, 150, 200]

    #     for nb_trees in list_nb_trees:
    #         classifier = RandomForestClassifier(n_estimators = nb_trees, criterion = 'gini', random_state = 42)
    #         classifier.fit(X_Train,Y_Train)

    #         train_results.append(mean_squared_error(Y_Train, classifier.predict(X_Train)))
    #         #test_results.append(mean_squared_error(Y_Test, classifier.predict(X_Test)))
    #         print("train score:", mean_squared_error(Y_Train, classifier.predict(X_Train)))
    #         #print("test score:",mean_squared_error(Y_Test, classifier.predict(X_Test)))

    #     line1, = plt.plot(list_nb_trees, train_results, color="r", label="Training Score")
    #     #line2, = plt.plot(list_nb_trees, test_results, color="g", label="Testing Score")

    #     plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
    #     plt.ylabel('MSE')
    #     plt.xlabel('n_estimators')
    #     plt.show()
    #     # plot learning curve



    
