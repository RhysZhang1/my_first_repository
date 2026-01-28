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
def lianbiao5():
    '''
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的

    示例 1：
    输入：l1 = [1,2,4]; l2 = [1,3,4]
    输出：[1,1,2,3,4,4]

    示例 2：
    输入：l1 = []; l2 = []
    输出：[]

    示例 3：
    输入：l1 = []; l2 = [0]
    输出：[0]

    链表？？？列表？？？
    '''
    exec(input("格式：l1 = 第一个列表 ; l2 = 第二个列表 ："),globals())
    l3=l1+l2
    l3.sort()
    print(f'{l3}')
def quchong6():
    """
    给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
    元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
    考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。

    示例 1：
    输入：nums = [1,1,2]
    输出：2, nums = [1,2,_]
    解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

    示例 2：
    输入：nums = [0,0,1,1,1,2,2,3,3,4]
    输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
    解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
    """
    exec(input("格式：nums = 原列表 ："),globals())
    cha=[]
    shan=[]
    for i in range(len(nums)):
        if nums[i] not in cha:
            cha.append(nums[i])
        else:
            shan.append(i)
    for i in sorted(shan,reverse=True):
        nums.pop(i)
    print(nums)
    print(f'{len(nums)}')
def yichu7():
    """
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。
    元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
    假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
    更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
    返回 k。

    示例 1：
    输入：nums = [3,2,2,3]; val = 3
    输出：2, nums = [2,2,_,_]
    解释：你的函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
    你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

    示例 2：
    输入：nums = [0,1,2,2,3,0,4,2]; val = 2
    输出：5, nums = [0,1,3,0,4,_,_,_]
    解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
    注意这五个元素可以任意顺序返回。
    你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
    """
    exec(input("格式：nums = 原列表; val = 需要删的元素 ："), globals())
    shan=[]
    for i in range(len(nums)):
        if nums[i]==val:
            shan.append(i)
    for i in sorted(shan,reverse=True):
        nums.pop(i)
    print(f'{len(nums)},',end='')
    print(f'nums = {nums}')
def pipei8():
    """
    给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
    如果 needle 不是 haystack 的一部分，则返回  -1 。

    示例 1：
    输入：haystack = "sacdbutsad"; needle = "sad"
    输出：7
    解释："sad" 在下标 0 和 6 处匹配。
    第一个匹配项的下标是 0 ，所以返回 0 。

    示例 2：
    输入：haystack = "leetcode"; needle = "leeto"
    输出：-1
    解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

    呃，还是不直接find了，自己实现一下试试
    """
    exec(input("格式：haystack = \"被查找的字符串\"; needle = \"要查找的字符串\"："), globals())
    a=0
    b=-1
    for i in range(len(haystack)):
        if haystack[i]!=needle[0]:
            continue
        else:
            a=0;b=i
            for j in range(len(needle)):
                if i + j >= len(haystack):
                    break
                if needle[j]==haystack[i+j]:
                    a+=1
                    continue
                else:
                    a=0
                    b=-1
                    break
        if a==len(needle):
            print(f'{b}')
            return
    print(f'{b}')
def sousuo9():
    """
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

    示例 1:
    输入: nums = [1,3,5,6]; target = 5
    输出: 2

    示例 2:
    输入: nums = [1,3,5,6]; target = 2
    输出: 1

    示例 3:
    输入: nums = [1,3,5,6]; target = 7
    输出: 4
    """
    exec(input("格式：nums = 原列表 ; target = 目标数字 ："), globals())
    a=-1
    for i in range(len(nums)):
        if nums[i]==target:
            a=i
            break
    if a==-1:
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break
    print(f'{a}')
if __name__=='__main__':
    sousuo9()