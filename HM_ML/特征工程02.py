from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba

def dictvec():
    dic = DictVectorizer(sparse=False)
    data = dic.fit_transform(
        [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}])
    print(dic.get_feature_names())
    print(data)
    return None


def Countvec():
    cv = CountVectorizer()
    data2 = cv.fit_transform(["life is short,i like python", "life is too long,i dislike python"])
    print(cv.get_feature_names())
    print(data2.toarray())
    return None


def cutword():
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")
    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")
    #  转换成列表
    cons1 = list(con1)
    cons2 = list(con2)
    cons3 = list(con3)
    #  转换成字符串
    c1 = ' '.join(cons1)
    c2 = ' '.join(cons2)
    c3 = ' '.join(cons3)
    return c1, c2, c3


def Countvec1():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    cv1 = CountVectorizer()
    data1 = cv1.fit_transform([c1, c2, c3])
    print(cv1.get_feature_names())
    print(data1.toarray())
    return None

def Tfidfvec1():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    tf = TfidfVectorizer()
    data1 = tf.fit_transform([c1, c2, c3])
    print(tf.get_feature_names())
    print(data1.toarray())
    return None

if __name__ == "__main__":
    #  dictvec()
    #  Countvec()
    Tfidfvec1()