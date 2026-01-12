#include<stdio.h>

int main()
{
    int x, y, z;
    char m;
    scanf("%d %c %d", &x, &m, &y);
    if (m == '+') { z = x + y; printf("%d", z); }
    else if (m == '-') { z = x - y; printf("%d", z); }
    else if (m == '*') { z = x * y; printf("%d", z); }
    else if (m == '/') { z = x / y; printf("%d", z); }
    else if (m == '%') { z = x % y; printf("%d", z); }
    else { printf("ERROR"); }//Ëû***È«ÊÇif
    return 0;
}