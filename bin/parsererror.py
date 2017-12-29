#coding=utf-8
from bin.lexicon import Lexicon

class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self,subject,verb,object):
        #remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

def peek(word_list):
    """获取句子的第一个word"""
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list,expecting):
    """pop出word_list的第一个word
    相符，则返回word；
    反之，则返回None
    """
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list,word_type):
    """检查word_list的第一个word和匹配的类型是否相符，
    相符，则pop出word；
    反之，则跳出循环，跳出函数"""

    while peek(word_list)==word_type:
        match(word_list,word_type)

def parse_verb(word_list):
    """匹配word是否为verb词性"""

    skip(word_list,'stop')
    skip(word_list, 'error')
    if peek(word_list)=='verb':
        return match(word_list,'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    """匹配word是否为noun 或 direction 词性"""

    skip(word_list,'stop')
    skip(word_list,'error')
    next=peek(word_list)

    if next == 'noun':
        return match(word_list,'noun')
    if next == 'direction':
        return match(word_list,'direction')
    if next == None:  #此处处理，允许只有主+谓，没有宾语名词的情况
        return ('noun','')
    else:   #此处是在宾语缺少名词的时候给出的错误提示信息
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list,subj):
    """为verb和object添加subject"""

    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj,verb,obj)

def parse_sentence(word_list):
    """组装sentence"""

    skip(word_list,'stop')
    skip(word_list,'error')

    start = peek(word_list)

    if start == 'noun':
        subj=match(word_list,'noun')
        return parse_subject(word_list,subj)
    elif start == 'verb':
        return parse_subject(word_list,('noun','player'))
    else:
        raise ParserError("Must start with subject, object,or verb not: %s" % start)

if __name__ == '__main__':
    sentence = "climb"
    lexicon = Lexicon()
    world_list=lexicon.scan(sentence)
    sentence = parse_sentence(world_list)
    print(sentence.subject+" "+sentence.verb+" "+sentence.object)