#include<stdio.h>
int main()
{
    int x;
    scanf("%d", &x);
    if (x <= 4) { printf("继续加油哦!"); }
    else if (x > 4 && x <= 10) { printf("非常棒，继续加油哦!"); }
    else if (x > 10 && x <= 100) { printf("实力不容小觑啊!"); }
    else { printf("能力爆表，全部通关!"); }//汉字加英文感叹号，纯纯恶心人
    return 0;
}