from efficient_apriori import apriori
import pandas as pd
#转化Excel数据为列表
source_data = pd.read_excel('201912034.xls',sheet_name=3)
list = source_data.values.tolist()
print(len(list))
transactions = list
itemsets, rules = apriori(transactions, min_support=0.5,  min_confidence=1)
print(rules)