#include<stdio.h>
int main()
{
    int a, b, i = -1000000, x = 0;
    scanf("%d", &a);
    while (x < a) {
        scanf("%d", &b);
        if (b > i) { i = b; }
        x += 1;
    }
    printf("%d", i);
    return 0;
}