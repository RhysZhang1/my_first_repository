#include<stdio.h>

int main()
{
    double x, y, z;
    scanf("%le %le", &x, &y);
    z = x / (y * y);
    if (z > 25) {
        printf("%.1f\nPANG", z);
    }
    else {
        printf("%.1f\nHai Xing", z);
    }
    return 0;
}