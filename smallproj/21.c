#include<stdio.h>
int main()
{
    int a, m = 0, n = 0;
    scanf("%d", &a);
    while (a > 0) {
        if (a >= 30) {
            if (n > m) { m = m + 90; a = a - 30; }
            else { m = m + 30; n = n + 90; a = a - 10; }
        }
        else if (a >= 10) {
            if (n > m) { m = m + a * 3; a = 0; }
            else { m = m + 30; n = n + 90; a = a - 10; }
        }
        else {
            if (n > m) { m = m + a * 3; a = 0; }
            else { m = m + a * 3; n = n + a * 9; a = 0; }
        }
    }
    if (m > n) { printf("@_@ %d", m); }
    if (m == n) { printf("-_- %d", m); }
    if (m < n) { printf("^_^ %d", n); }
    return 0;
}