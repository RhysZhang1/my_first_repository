#include<stdio.h>

int main()
{
    int x;
    scanf("%d", &x);
    if (x >= 720)
    {
        printf("Peking University");
    }
    else if (x >= 650 && x < 720)
    {
        printf("Zhejiang University");
    }
    else if (x >= 600 && x < 650)
    {
        printf("University Of Technology");
    }
    else if (x >= 550 && x < 600)
    {
        printf("Shaoxing University");
    }
    else if (x >= 500 && x < 550)
    {
        printf("Shaoxing University Yuanpei College");
    }
    else if (x >= 400 && x < 500)
    {
        printf("Shaoxing Vocational & Technical College");
    }
    else
    {
        printf("to be a farmer");
    }//下次请用中文或者缩写
    return 0;
}