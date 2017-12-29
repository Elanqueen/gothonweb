#coding=utf-8
class Lexicon:
    """扫描器
    筛选用户输入中的关键词，组成sentence，返回sentence
    """

    direction = ['north','south','east','west','down','up','right','back']
    verb = ['climb','give','find','tell','run','type','bite','go','stop','kill','eat']
    stop=['the','in','of','from','at','it','through']
    noun = ['ladder','pine_nuts','squirrel','key','joke','number','bridge','him','princess','cabinet']

    def conver_number(self,s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(self,cls):
        result=[]
        words = cls.split(" ")
        for word in words:
            if word in self.direction:
                result.append(('direction', word))
            elif word in self.verb:
                result.append(('verb', word))
            elif word in self.stop:
                result.append(('stop', word))
            elif word in self.noun:
                result.append(('noun', word))
            elif self.conver_number(word)!=None:
                result.append(('number',int(word)))
            else:
                result.append(('error', word))
        return result

if __name__ == '__main__':
    sentence = "I would like 20 pieces of cakes!"
    lexicon=Lexicon()
    print(lexicon.scan(sentence))