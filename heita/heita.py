import time,math
def main(chushi):
    if not chushi:
        return 0
    yuzhi=[x//2 for x in chushi]
    x=len(chushi)
    biaoji=[0 for i in range(x)]
    chushi.sort()
    mx=0
    for i in range(x):
        if chushi[i]>x:
            mx=i
            break
    f=mx
    for i in range(f):
        biaoji[i]=1
    n=0
    n=n+chushi[mx]-yuzhi[mx]
    chushi[mx]=yuzhi[mx]
    for i in range(x):
        chushi[i]-=1
    biaoji[mx]=1
    q=0
    while True:
        while True:
            for i in range(x-1):
                if chushi[i]<=yuzhi[i] and biaoji[i]==0:
                    q=q+1
                    biaoji[i]=1
            if q==0:
                break
            for i in range(x):
                chushi[i]-=q
            q=0
        while True:
            f+=1
            if f==x:
                break
            if biaoji[f]==0:
                n+=chushi[f]-yuzhi[f]
                chushi[f]=yuzhi[f]
                for i in range(x):
                    chushi[i]-=1
                    biaoji[f]=1
                break
        if f==x:
            break
    for i in range(x):
        chushi[i]-=mx
        if chushi[i]>0:
            n+=chushi[i]
    return n
def inputt():
    usin=input()
    while True:
        chushi=[]
        part=usin.split()
        for i in part:
            try:
                num=float(i)
                if num!=int(num):
                    num=math.ceil(num)
                else:
                    num=int(num)
                if num>0:
                    chushi.append(num)
            except (ValueError,TypeError):
                continue
        if chushi:
            return chushi
        else:
            print('error')
def runtime():
    chushi=inputt()
    start_time = time.perf_counter()
    result = main(chushi)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time
if __name__ == '__main__':
    result, elapsed_time = runtime()
    print(result)
    print(f'{elapsed_time*1000:.4f}毫秒')