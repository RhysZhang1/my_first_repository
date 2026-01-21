#include<stdio.h>
int main()
{
    long long a, b, c = 0, s = 0;
    scanf("%lld %lld", &a, &b);
    c = a;
    for (int i = 0; i < b; i++) {
        s += c;
        c = c * a;
    }
    printf("sum = %lld", s);
    return 0;
}