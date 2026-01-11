#include<stdio.h>
#include<math.h>

int main()
{
    double x, y, m;
    scanf("%le", &x);
    if (x <= 0) { m = fabs((x * x * x) + 4); y = (23 * m) / 7; }//¾ø¶ÔÖµ
    if (x > 0 && x <= 6) { m = (log(16) / log(3)); y = x + m; }
    if (x > 6) { m = (x * x) + (4 * x) - 6; y = (5 * m) / 27; }
    printf("%.3f", y);
    return 0;
}