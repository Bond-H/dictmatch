import time
import sys
import os

class Template:
    def __init__(self) -> None:
        pass
    def add_word(self, word, val=0) -> None:
        pass
    
    def build(self) -> None:
        pass
    
    def search(self, text, mode="ALL"):
        pass

class PrefixDict(Template):
    def __init__(self) -> None:
        super(Template, self).__init__()
        # sys.path.append("../dictmatch")
        # from prefix_dict import TriedTree
        from dictmatch import TriedTree
        self.tree = TriedTree()
    def add_word(self, word, val=0) -> None:
        self.tree.add_word(word, val)
        
    def build(self) -> None:
        self.tree.make()

    def search(self, text, mode="ALL"):
        return self.tree.search(text, mode)     

class DmDict(Template):
    def __init__(self) -> None:
        super(Template, self).__init__()
        from dmsearch import dmdict
        self.tree = dmdict.DMSearchDict()
    
    def add_word(self, word, val = 0) -> None:
        self.tree.add(word, val)
    

    def search(self, text, mode="ALL"):
        return self.tree.find(text, mode == "ALL")

class ahocorapy(Template):
    def __init__(self) -> None:
        super(Template, self).__init__()
        from ahocorapy.keywordtree import KeywordTree
        self.tree = KeywordTree()
        
    def add_word(self, word, val=0) -> None:
        self.tree.add(word)
        
    def build(self) -> None:
        self.tree.finalize()
    
    def search(self, text, mode="ALL"):
        if mode == "ALL":
            return self.tree.search_all(text)
        else:
            return self.tree.search(text)


# 评测不同词典匹配工具的性能
# from memory_profiler import profile
# @profile
def test_eval(imp, data_name):
    tree = imp()
    word_file = "data/%s_words.txt"%data_name
    data_file = "data/%s_data.txt"%data_name
    words = [word.strip() for word in open(word_file, 'r', encoding='utf8')]

    start = time.time()
    for word in words:
      tree.add_word(word)
    tree.build()
    end = time.time()
    print("%s %s load time: %f"%(imp.__name__, data_name, end-start))

    start = time.time()
    for line in open(data_file, 'r', encoding='utf8'):
      list(tree.search(line.strip()))
    end = time.time()

    print("%s %s search time: %f"%(imp.__name__, data_name, end-start))
    
if __name__ == "__main__":
  test_eval(ahocorapy, 'pku')
  test_eval(ahocorapy, 'as')
  test_eval(ahocorapy, 'jieba')
  
  test_eval(DmDict, 'pku')
  test_eval(DmDict, 'as')
  test_eval(DmDict, 'jieba')
  
  test_eval(PrefixDict, 'pku')
  test_eval(PrefixDict, 'as')
  test_eval(PrefixDict, 'jieba')
    
