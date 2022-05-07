# dictmatch
高效的词典匹配工具，用于查询词典中的单词是否在字符串中

# 安装与使用
## 安装说明
- pip安装：`pip install dictmatch`
- clone安装：先clone本代码库，然后运行 `python setup.py install`
- 手动安装：将 dictmatch 目录放置于当前目录或者 site-packages 目录，通过 `import dictmatch` 来引用

## 快速使用
```Python
words = ["百度":"ORG", "家":"m", "家家":0, "高科技":'adj', "技公":0, "科技":"n", "科技公司":'n'}
text = '百度是家高科技公司'
tree = TriedTree()
for word, val in words.items():
    tree.add_word(word, val)

print("前向最大匹配结果:")
for word, begin, end, val in tree.search(text):
    print(word, begin, end, val)

print("\n全匹配结果:")
for word, begin, end, val in tree.search(text, mode="ALL"):
    print(word, begin, end, val)
```