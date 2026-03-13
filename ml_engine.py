import numpy as np
from sklearn.linear_model import LinearRegression

class NSEPredictor:
    """Uses Linear Regression to forecast short-term price movements."""
    
    def __init__(self):
        self.model = LinearRegression()

    def predict_next_price(self, price_history):
        """
        Trains a quick model on current session history 
        to predict the price at T+1.
        """
        if len(price_history) < 5:
            return price_history[-1]

        # Prepare data (X = time indices, y = prices)
        X = np.array(range(len(price_history))).reshape(-1, 1)
        y = np.array(price_history)

        # Fit model
        self.model.fit(X, y)

        # Predict next step (last index + 1)
        next_step = np.array([[len(price_history)]])
        prediction = self.model.predict(next_step)
        
        return prediction[0]

