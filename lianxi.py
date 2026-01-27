def huiwen1():
    '''
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    例如，121 是回文，而 123 不是。
    '''
    a=input()
    hui=list(str(a))
    wen=hui[::-1]
    if hui==wen:
        print('True')
    else:
        print('False')
def luoma2():
    '''
     罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，
    例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。
    这个特殊的规则只适用于以下六种情况：
    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

    给定一个罗马数字，将其转换成整数。
    示例 1:
    输入: s = "III"
    输出: 3

    示例 2:
    输入: s = "IV"
    输出: 4

    示例 3:
    输入: s = "IX"
    输出: 9

    示例 4:
    输入: s = "LVIII"
    输出: 58
    解释: L = 50, V= 5, III = 3.

    示例 5:
    输入: s = "MCMXCIV"
    输出: 1994
    解释: M = 1000, CM = 900, XC = 90, IV = 4.
    '''
    a=input()
    luo=list(str(a))
    shu=0
    dui={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    cha={'I':1,'V':2,'X':3,'L':4,'C':5,'D':6,'M':7}
    biao=[]
    for i in luo:
        biao.append(0)
    for i in range(len(luo)):
        if biao[i]==1:
            continue
        if i==len(luo)-1:
            shu+=dui[luo[i]]
            break
        if cha[luo[i]]<cha[luo[i+1]]:
            shu+=(dui[luo[i+1]]-dui[luo[i]])
            biao[i]=1;biao[i+1]=1
        else:
            shu+=dui[luo[i]]
    print(shu)
def qianzhui3():
    """
    查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1：
    输入：strs = ["flower","flow","flight"]
    输出："fl"

    示例 2：
    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。
    """
    ru=input()
    ci=eval(ru)
    if not ci:
        print('""')
        return
    ci.sort(key=len)
    gong=[]
    for i in ci[0]:
        gong.append(i)
    for i in range(1,len(ci)):
        for j in range(len(gong)):
            if ci[i][j]==gong[j]:
                continue
            else:
                gong=gong[:j]
                break
    s=''.join(gong)
    print(f'"{s}"')
def kuohao4():
    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。

    示例 1：
    输入：s = "()"
    输出：true

    示例 2：
    输入：s = "()[]{}"
    输出：true

    示例 3：
    输入：s = "(]"
    输出：false

    示例 4：
    输入：s = "([])"
    输出：true

    示例 5：
    输入：s = "([)]"
    输出：false
    """
    ru=input().strip('"')
    dui={'(':1,')':-1,'[':2,']':-2,'{':3,'}':-3}
    huan=[]
    for i in ru:
        if dui[i]>0:
            huan.append(dui[i])
        else:
            if huan==[]:
                print('false')
                return
            if dui[i]+huan[-1]==0:
                huan.pop()
            else:
                print('false')
                return
    if huan==[]:
        print('true')
if __name__=='__main__':
    kuohao4()