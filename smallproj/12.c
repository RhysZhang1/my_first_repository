#include<stdio.h>
int main()
{
    double x, y;
    scanf("%lf", &x);
    if (x < 0)
    {
        printf("Invalid Value!");
    }
    else if (x >= 0 && x <= 50)
    {
        y = (x * 0.53);
        printf("cost = %.2f", y);
    }
    else
    {
        y = ((50 * 0.53) + ((x - 50) * (0.53 + 0.05)));
        printf("cost = %.2f", y);
    }//算是不可能算的，让代码算吧
    return 0;
}