#include<stdio.h>

int main()
{
    int m, n;
    int x, y, z, p;
    scanf("%d %d", &m, &n);
    scanf("%d %d %d", &x, &y, &z);
    if (m > n && 3 - (x + y + z) >= 1) { p = 3 - (x + y + z); printf("The winner is a: %d + %d", m, p); }
    else if (m < n && 3 - (x + y + z) == 3) { printf("The winner is a: %d + 3", m); }
    else { p = x + y + z; printf("The winner is b: %d + %d", n, p); }
    return 0;
}