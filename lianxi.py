from string import digits
import math
import random

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
def danci10():
    """
    给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
    单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

    示例 1：
    输入：s = "Hello World"
    输出：5
    解释：最后一个单词是“World”，长度为 5。

    示例 2：
    输入：s = "   fly me   two   the moon  "
    输出：4
    解释：最后一个单词是“moon”，长度为 4。

    示例 3：
    输入：s = "luffy is still joyboy"
    输出：6
    解释：最后一个单词是长度为 6 的“joyboy”。
    """
    exec(input("格式：s = \"字符串\"："), globals())
    ci=s.split()
    a=len(ci[-1])
    print(a)
def jiayi11():
    """
    给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。
    这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。
    将大整数加 1，并返回结果的数字数组。

    示例 1：
    输入：digits = [1,2,3]
    输出：[1,2,4]
    解释：输入数组表示数字 123。
    加 1 后得到 123 + 1 = 124。
    因此，结果应该是 [1,2,4]。

    示例 2：
    输入：digits = [4,3,2,1]
    输出：[4,3,2,2]
    解释：输入数组表示数字 4321。
    加 1 后得到 4321 + 1 = 4322。
    因此，结果应该是 [4,3,2,2]。

    示例 3：
    输入：digits = [9]
    输出：[1,0]
    解释：输入数组表示数字 9。
    加 1 得到了 9 + 1 = 10。
    因此，结果应该是 [1,0]。
    """
    exec(input("格式：digits = 列表 :"), globals())
    a=''.join(map(str,digits))
    a=int(a)
    a+=1
    a=str(a)
    hou=[]
    for i in a:
        hou.append(int(i))
    print(hou)
def jinzhi12():
    """
    给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

    示例 1：
    输入:a = "11"; b = "1"
    输出："100"

    示例 2：
    输入：a = "1010"; b = "1011"
    输出："10101"
    """
    exec(input("格式：a = \"二进制数\"; b = \"二进制数\" :"), globals())
    global a,b
    a=int(a,2)
    b=int(b,2)
    c=a+b
    print(f'"{c:b}"')
    #也可以用bin
def fanggen13():
    """
    给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
    由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
    注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

    示例 1：
    输入：x = 4
    输出：2

    示例 2：
    输入：x = 8
    输出：2
    解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去
    """
    x=int(input())
    for i in range(x):
        if i**2>x:
            print(i-1)
            break
        if i**2==x:
            print(i)
            break
        if i**2<x:
            continue
def louti14():
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

    示例 1：
    输入：n = 2
    输出：2
    解释：有两种方法可以爬到楼顶。
    1. 1 阶 + 1 阶
    2. 2 阶

    示例 2：
    输入：n = 3
    输出：3
    解释：有三种方法可以爬到楼顶。
    1. 1 阶 + 1 阶 + 1 阶
    2. 1 阶 + 2 阶
    3. 2 阶 + 1 阶
    """
    x=int(input())
    def zong(n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        else:
            return zong(n-1)+zong(n-2)
    print(zong(x))
def hebing15():
    """
    给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
    请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
    注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
    为了应对这种情况，nums1 的初始长度为 m + n，
    其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n

    示例 1：
    输入：nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
    输出：[1,2,2,3,5,6]
    解释：需要合并 [1,2,3] 和 [2,5,6] 。
    合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

    示例 2：
    输入：nums1 = [1]; m = 1; nums2 = []; n = 0
    输出：[1]
    解释：需要合并 [1] 和 [] 。
    合并结果是 [1]。

    示例 3：
    输入：nums1 = [0]; m = 0; nums2 = [1]; n = 1
    输出：[1]
    解释：需要合并的数组是 [] 和 [1] 。
    合并结果是 [1] 。
    注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
    """
    exec(input("格式：nums1 = 列表1; m = 数1; nums2 = 列表2; n = 数2 :"), globals())
    global m,n,nums1,nums2
    nums1=nums1[0:m]
    nums2=nums2[0:n]
    nums1=nums1+nums2
    nums1.sort()
    print(nums1)
def yanghui16():
    """
    给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
    在「杨辉三角」中，每个数是它左上方和右上方的数的和。

    示例 1:
    输入: numRows = 5
    输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    示例 2:
    输入: numRows = 1
    输出: [[1]]
    """
    numRows=int(input())
    san=[]
    for i in range(numRows):
        san.append([1 if j==0 or j==i else 0 for j in range(i+1)])
    for i in range(2,numRows):
        for j in range(1,i):
            san[i][j]=san[i-1][j-1]+san[i-1][j]
    print(san)
    #换一种计算方式
    san2=[]
    for i in range(numRows):
        san2.append([math.comb(i,j) for j in range(i+1)])
    print(san2)
def gupiao17():
    """
    给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
    你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
    设计一个算法来计算你所能获取的最大利润。\
    返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。



    示例 1：
    输入：prices = [7,1,5,3,6,4]
    输出：5
    解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
         注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

    示例 2：
    输入：prices = [7,6,4,3,1]
    输出：0
    解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
    """
    prices=eval(input())
    cha=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            # prices[i]=int(prices[i])
            # prices[j]=int(prices[j])
            if prices[j]-prices[i]>0 and prices[j]-prices[i]>cha:
                cha=prices[j]-prices[i]
    print(cha)
def huiwen18():
    """
    如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
    字母和数字都属于字母数字字符。
    给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

    示例 1：
    输入: s = "A man, a plan, a canal: Panama"
    输出：true
    解释："amanaplanacanalpanama" 是回文串。

    示例 2：
    输入：s = "race a car"
    输出：false
    解释："raceacar" 不是回文串。

    示例 3：
    输入：s = " "
    输出：true
    解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
    由于空字符串正着反着读都一样，所以是回文串。
    """
    exec(input("格式：s = \"字符串\" :"), globals())
    global s
    s=s.lower()
    s=list(s)
    shan=[]
    for i in range(len(s)):
        if not ((s[i]>='0' and s[i]<='9') or (s[i]>='a' and s[i]<='z')):
            shan.append(i)
    shan.sort(reverse=True)
    for i in shan:
        s.pop(i)
    s1=[]
    for i in range (len(s)):
        s1.append(s[-1-i])
    if s==s1:
        print('true')
    else:
        print('false')
def yici19():
    """
    给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次
    找出那个只出现了一次的元素。
    你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

    示例 1 ：
    输入：nums = [2,2,1]
    输出：1

    示例 2 ：
    输入：nums = [4,1,2,1,2]
    输出：4

    示例 3 ：
    输入：nums = [1]
    输出：1
    """
    exec(input("格式：nums = 列表 :"), globals())
    fu=[]
    for i in nums:
        if i not in fu:
            fu.append(i)
            continue
        if i in fu:
            fu.remove(i)
            continue
    print(fu[0])
def excel20():
    """
    给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

    例如：
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

    示例 1：
    输入：columnNumber = 1
    输出："A"

    示例 2：
    输入：columnNumber = 28
    输出："AB"

    示例 3：
    输入：columnNumber = 701
    输出："ZY"

    示例 4：
    输入：columnNumber = 2147483647
    输出："FXSHRXW"
    """
    a=int(input('输入整数:'))
    m=[]
    h={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',
       8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',
       15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',
       22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    while True:
        if a>26:
            x=a%26
            a=a//26
            m.append(h[x])
            continue
        else:
            m.append(h[a])
            break
    m.reverse()
    p=''.join(m)
    print(p)
def caishu21():
    """
    猜数字大小：0-100
    """
    num=random.randint(1,101)
    a=int(input("输入一个0到100的整数:"))
    max=100;min=0
    while True:
        if a==num:
            print("猜对了！！！")
            break
        if a>100 or a<0:
            print("范围错了，是0到100！！！")
            a=int(input("请重新输入一个数："))
            continue
        if a>num:
            max=a
            print(f"{min}到{max}")
            a=int(input("继续输入："))
            continue
        if a<num:
            min=a
            print(f"{min}到{max}")
            a=int(input("继续输入："))
            continue
def fanzhuan22():
    """
    颠倒给定的 32 位有符号整数的二进制位。

    示例 1：
    输入：n = 43261596
    输出：964176192
    解释：
    整数	        二进制
    43261596	00000010100101000001111010011100
    964176192	00111001011110000010100101000000

    示例 2：
    输入：n = 2147483644
    输出：1073741822
    解释：
    整数	        二进制
    2147483644	01111111111111111111111111111100
    1073741822	00111111111111111111111111111110
    """
    n=int(input())
    n=format(n,'b')
    x=len(n)
    n=int(n,2)
    c=[];q=0;t=0
    for i in range(x):
        q=n%2
        c.append(q)
        n=n//2
    r=len(c)
    if r<32:
        while True:
            c.append(t)
            if len(c)==32:
                break
    w=''.join(map(str,c))
    e=int(w,2)
    priht(e)
def weiyi23():
    """
    给定一个正整数 n，编写一个函数，获取一个正整数的二进制形式
    并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。

    示例 1：
    输入：n = 11
    输出：3
    解释：输入的二进制串 1011 中，共有 3 个设置位。

    示例 2：
    输入：n = 128
    输出：1
    解释：输入的二进制串 10000000 中，共有 1 个设置位。

    示例 3：
    输入：n = 2147483645
    输出：30
    解释：输入的二进制串 1111111111111111111111111111101 中，共有 30 个设置位。
    """
    n=int(input())
    n=format(n,'b')
    x=len(n)
    n=int(n,2)
    q=0
    for i in range(x):
        if n%2==1:
            q+=1
            n=n//2
            continue
        else:
            n=n//2
            continue
    print(q)
def kuaile24():
    """
    编写一个算法来判断一个数 n 是不是快乐数。
    「快乐数」 定义为：
    对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
    然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
    如果这个过程 结果为 1，那么这个数就是快乐数。
    如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

    示例 1：
    输入：n = 19
    输出：true
    解释：
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

    示例 2：
    输入：n = 2
    输出：false
    """
if __name__=='__main__':
    weiyi23()