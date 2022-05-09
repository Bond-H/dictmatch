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


# 性能评测
AC自动机的Python实现及其性能对比，相关测试代码存放于`eval`目录中

## 测试数据
数据存放在`eval/data`目录中，包括PKU和AS的分词数据集、jieba词库组成，分别测试三个数据集`词典装载`和`查询`的耗时

| 数据集 | 单词数 |  数据大小  |
| :----: | :----: | :--------: |
|  PKU   | 5.5W  | 1826448字  |
|   AS   | 14.1W | 8368050字 |
| Jieba  | 58.4W | 4050566字  |

## 评测结果
### 词典装载性能
|       数据集       |       PKU       |       AS       |    jieba     |
| :--------------: | :-------------: | :------------: | :----------: |
|    单词数    | 5.5W | 14.1W  | 58.4W |
|    ahocorapy    | 3 | 20  | 354 |
|    dmsearch    | 0.13 | 0.56  | 2.67 |
| prefix_dict |   0.05 |  0.14)  | 0.60 |



### 词典查询性能

|       数据集       |       PKU       |       AS       |    jieba     |
|    ahocorapy    | 0.02 | 0.34  | 0.08 |
|    dmsearch    | 4.2 | 12.8  | 6.7 |
| prefix_dict |   1.4 |  6.7  | 3.5 |