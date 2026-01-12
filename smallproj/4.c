#include<stdio.h>

int main()
{
    double x, y, z;
    scanf("%le %le", &x, &y);
    if (y == 0.000000) { printf("%.0f/%.0f=Error", x, y); }
    else {
        if (y > 0) { z = x / y; printf("%.0f/%.0f=%.2f", x, y, z); }
        else { z = x / y; printf("%.0f/(%.0f)=%.2f", x, y, z); }
    }
    return 0;
}