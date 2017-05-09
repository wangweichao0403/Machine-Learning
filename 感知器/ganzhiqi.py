import numpy as np

class perceptron(object):
    '''perceptron classifier(感知器)

    parameters （参数）
    ----------------------------
    eta：float 学习速率，介于0到1之间
    n_iter：int 训练集的迭代次数

    Attributes (属性)
    ------------------------------
    w_ ：id_array 训练后的权重
    errors : list 每一次迭代错误分类的数量
    '''
    def __init__(self,eta,n_iter):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self,X,y):
        '''
        :param self:
        :param x: {array-like} shape=[n_sample,n_features] 训练数据集 n_sample是样本的数量，n_feature是样本的特征
        :param y: array-like shape=[n_sample] 目标值
        :return: object (对象)
        '''

        self.w_=np.zeros(1+X.shape[1])
        self.errors_=[]
        for _ in range(self.n_iter):
            errors=0
            for xi,target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0]=update
                self.errors+=int(update=0.0)
            self.errors_.append(errors)


    def net_input(self,X):
        '''计算净输入'''
        return np.dot(X,self.w_[1:])+self.w_[0]
    def predict(self,X):
        '''经过单位跃级函数返回类标'''
        return np.where(self.net_input(x)>=0,1,-1)