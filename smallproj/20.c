#include<stdio.h>
int main()
{
    long long a, b = 1, s = 0;
    scanf("%lld", &a);
    for (int i = 0; i < a; i++) {
        b = b * (i + 1);
        s += b;
    }
    printf("sum = %lld", s);
    return 0;
}