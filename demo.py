from dictmatch import TriedTree

if __name__ == "__main__":
    words = {"百度":"ORG", "家":"m", "家家":0, "高科技":'adj', "技公":0, "科技":"n", "科技公司":'n'}
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