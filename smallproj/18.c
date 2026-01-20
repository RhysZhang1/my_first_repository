#include<stdio.h>
int main()
{
    long long a, b, d = 0, s = 0;
    scanf("%lld %lld", &a, &b);
    for (int i = 1; i <= b; i++) {
        d = d * 10 + a;
        s += d;
    }
    printf("S = %lld", s);
    return 0;
}