from xpinyin import Pinyin
p = Pinyin()
def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
def judge(l1,l2):
    ret = 1
    for i in range(min(len(l1), len(l2))):
        l1i = l1[i]
        l2i = l2[i]
        if isChinese(l1i) == True:
            l1i = p.get_pinyin(l1i)
        if isChinese(l2i) == True:
            l2i = p.get_pinyin(l2i)
        l1i = l1i.lower()
        l2i = l2i.lower()
        print(l1i,l2i)
        if l1i > l2i:
            ret = 2
            break
        elif l1i == l2i:
            continue
        else:
            ret = 1
            break
    return ret
def main():
    lines = []
    with open(r'data.txt', 'r',encoding = 'utf-8') as f:
        lines = f.readlines()
    print(lines)
    print(lines[0].split('	')[1])
    #冒泡排序
    slow = 0
    fast = 0
    flag = len(lines) - 1
    while slow < len(lines)-1:
        if fast == flag:
            slow = slow + 1
            fast = 0
            flag = flag - 1
        if judge(lines[fast].split('	')[1],lines[fast+1].split('	')[1]) == 2:
            temp = lines[fast]
            lines[fast] = lines[fast+1]
            lines[fast + 1] = temp
            fast = fast + 1
        else:
            fast = fast + 1
            if fast + 1 > len(lines) - 1:
                break        
    for i in range(len(lines)):
        lines[i] = lines[i].split('	')[1]
    with open(r'new.txt', 'w') as f:
        for l in lines:
                f.write(l)
    f.close()
        
main()

        