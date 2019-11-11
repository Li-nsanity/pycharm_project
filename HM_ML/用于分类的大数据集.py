from sklearn.datasets import fetch_20newsgroups

news = fetch_20newsgroups()
print(news.data)
print(news.target)