#include<stdio.h>
int main()
{
    double a, b, c, y = 0, n = 1;
    scanf("%lf", &a);
    for (int i = 0; i < a; i++) {
        b = n / (2 * n - 1);
        if (i % 2 == 0) { c = b; }
        if (i % 2 == 1) { c = -b; }
        y += c;
        n += 1;
    }
    printf("%.3lf\n", y);
    return 0;
}