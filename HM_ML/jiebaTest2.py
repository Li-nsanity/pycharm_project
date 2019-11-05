import jieba

def jb():
    strl = "此生无悔入华夏,来世还生种花家。中华人民共和国万岁。美哉我少年中华,与天不老。壮哉我中国少年,与国无疆"
    data = jieba.lcut(strl)
#  data = jieba.lcut_for_serach(strl)
#  data = jieba.lcut(strl,cut_all=True)
    print(data)
    return None
if __name__ == "__main__":
    jb()