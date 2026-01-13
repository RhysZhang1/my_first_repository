#include<stdio.h>
int main()
{
    int x;
    scanf("%d", &x);
    if (x >= 90) { printf("gong xi ni kao le %d fen!", x); }
    if (x < 90) { printf("kao le %d fen bie xie qi!", x); }//用汉字或者英文不好吗，非要用拼音？
    return 0;
}