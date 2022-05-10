# dictmatch
高效的词典匹配工具，用于查询词典中的单词是否在字符串中，尤其在大规模词典匹配中，效果尤为显著

# 安装与使用
## 安装说明
- pip安装：`pip install dictmatch`
- clone安装：先clone本代码库，然后运行 `python setup.py install`
- 手动安装：将 dictmatch 目录放置于当前目录或者 site-packages 目录，通过 `import dictmatch` 来引用

## 快速使用
```Python
from dictmatch import TriedTree

# 待添加的词典，可以有value也可以没有
words = ["百度":"ORG", "家":"m", "家家":0, "高科技":'adj', "技公":0, "科技":"n", "科技公司":'n'}

# 加入词典
tree = TriedTree()
for word, val in words.items():
    tree.add_word(word, val)

# 进行查询
text = '百度是家高科技公司'
print("前向最大匹配结果:")
for word, begin, end, val in tree.search(text):
    print(word, begin, end, val)

print("\n全匹配结果:")
for word, begin, end, val in tree.search(text, mode="ALL"):
    print(word, begin, end, val)
```


# 性能评测
对相关的词典匹配工具进行评测，相关测试代码存放于`eval`目录中

从评测结果可以看出，本代码对比其他工具
- 内存占用上，装载性能上都有极大的优势
- 查询性能可达到每秒百万字的查询性能，与AC自动机实现代码库ahocorapy能相差无几
- 在处理大型词典时，本代码库实现的优势越发显著

## 测试数据
数据存放在`eval/data`目录中，包括PKU和AS的分词数据集、jieba词库组成，分别测试三个数据集`词典装载`和`查询`的耗时，以及`内存占用`多个方面进行评测

| 数据集 | 单词数 |  数据大小  |
| :----: | :----: | :--------: |
|  PKU   | 5.5W  | 1826448字  |
|   AS   | 14.1W | 8368050字 |
| Jieba  | 58.4W | 4050566字  |

## 评测数据

### 词典装载性能(装载时间 秒)
|       数据集       |       PKU       |       AS       |    jieba     |
| :--------------: | :-------------: | :------------: | :----------: |
|    单词数    | 5.5W | 14.1W  | 58.4W |
|    ahocorapy    | 3 | 20  | 354 |
|    dmsearch    | 0.13 | 0.56  | 2.67 |
| dictmatch |   0.05 |  0.14 | 0.60 |


### 词典查询性能(查询时间 秒)

|       数据集       |       PKU       |       AS       |    jieba     |
| :--------------: | :-------------: | :------------: | :----------: |
|    ahocorapy    | 1.0 | 5.4  | 9.27 |
|    dmsearch    | 4.2 | 12.8  | 6.7 |
| dictmatch |   1.4 |  6.7  | 3.5 |


### 内存占用
|       数据集       |       PKU       |       AS       |    jieba     |
| :--------------: | :-------------: | :------------: | :----------: |
|    单词数    | 5.5W | 14.1W  | 58.4W |
|    ahocorapy    | 300M | 800M  | 5G |
|    dmsearch    | 1G | 1G  | 2.5G |
| dictmatch |   25M |  100M | 400M |