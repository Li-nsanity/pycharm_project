import tensorflow as tf


def linear_regression():
    """
    自实现一个线性回归
    :return:
    """
    #  1.准备数据
    X = tf.random.normal(shape=[100, 1])
    y_true = tf.matmul(X, [[0.8]]) + 0.7
    #  2.构造模型
    #   定义模型参数 用 变量
    weights = tf.compat.v1.Variable(initial_value=tf.random.normal(shape=[1, 1]))
    bias = tf.compat.v1.Variable(initial_value=tf.random.normal(shape=[1, 1]))
    y_predict = tf.matmul(X, weights) + bias
    #  3.构造损失函数
    error = tf.reduce_mean(tf.square(y_true - y_predict))
    #  4.优化损失函数
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01)
    init = tf.compat.v1.global_variables_initializer()
    with tf.compat.v1.Session() as sess:
        sess.run(init)
        print(weights, bias)
    return None


if __name__ == "__main__":
    linear_regression()
