def costFunction(theta, X, y, return_grad=False):
#COSTFUNCTION Compute cost and gradient for logistic regression
#   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
#   parameter for logistic regression and the gradient of the cost
#   w.r.t. to the parameters.

    import numpy as np 
    from sigmoid import sigmoid

    # Initialize some useful values
    m = len(y) # number of training examples

    # You need to return the following variables correctly 
    J = 0
    grad = np.zeros(theta.shape)

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta.
    #               You should set J to the cost.
    #               Compute the partial derivatives and set grad to the partial
    #               derivatives of the cost w.r.t. each parameter in theta
    #
    # Note: grad should have the same dimensions as theta
    # theta.shape = (n+1,1)
    # X.shape = (m, n+1)
    # np.dot (X,theta).shape = (m,1)
    # y.shape = (m, )
    # when y = 1 returns  - np.log(sigmoid(np.dot(X, theta))) 
    # when y = 0 returns  - np.log(1- sigmoid(np.dot(X, theta)))
    # to multiply with y we need to transpose the log functions above 
    a = y * np.transpose (np.log(sigmoid(np.dot (X,theta))))
    b = (1-y) * np.transpose (np.log (1 - sigmoid (np.dot (X, theta))))
    J = (-1/m) * (a + b).sum ()

    # we need (n+1) gradients 
    # y.shape = (m,)
    # sigmoid (np.dot (X,theta)).shape = (m,1)
    # Transpose of sigmoid (np.dot (X, theta)) has shape (1,m) [Str]
    # X.shape = (m,n+1)
    # Str.X => shape (1,n+1)
    grad = (1/m) * np.transpose(np.dot (np.transpose (sigmoid (np.dot (X,theta)) - y),X))
    if return_grad == True:
        return J, np.transpose (grad)
    elif return_grad == False:
        return J 

# =============================================================
