#include<stdio.h>
#include<math.h>
int main()
{
    int x, y, z;
    double s, a, b;
    scanf("%d %d %d", &x, &y, &z);
    if (x > y) { x = x + y; y = x - y; x = x - y; }
    if (x > z) { x = x + z; z = x - z; x = x - z; }
    if (y > z) { y = y + z; z = y - z; y = y - z; }
    if (x + y <= z) { printf("These sides do not correspond to a valid triangle"); }
    else {
        s = (double)(x + y + z) / 2;
        a = pow(s * (s - x) * (s - y) * (s - z), 0.5);//¿ª·½
        b = x + y + z;
        printf("area = %.2f; perimeter = %.2f", a, b);
    }
    return 0;
}