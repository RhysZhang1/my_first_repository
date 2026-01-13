#include<stdio.h>
int main()
{
    int x, y, a, b, c;
    double d;
    scanf("%d %d", &x, &y);
    a = x + y; b = x - y; c = x * y;
    printf("%d + %d = %d\n", x, y, a);
    printf("%d - %d = %d\n", x, y, b);
    printf("%d * %d = %d\n", x, y, c);
    if (x % y == 0) { d = x / y; printf("%d / %d = %.0f\n", x, y, d); }
    else { d = (double)x / y; printf("%d / %d = %.2f\n", x, y, d); }
    return 0;
}