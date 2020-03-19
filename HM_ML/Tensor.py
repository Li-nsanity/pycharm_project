import tensorflow as tf


def test_demo():
    with tf.variable_creator_scope('chart1'):
        a = tf.Variable(40)
        b = tf.Variable(50)
    with tf.variable_creator_scope('chart2'):
        c = tf.add(a, b)
    #  init = tf.global_variables_initializer()
    print(a)
    print(b)
    print(c)
    with tf.Session() as sess:
   #     sess.run(init)
        a_value, b_value, c_value = sess.run([a, b, c])
        print("a_value", a_value)
        print("b_value", b_value)
        print("c_value", c_value)
    return None


if __name__ == "__main__":
    test_demo()
