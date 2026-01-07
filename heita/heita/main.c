#include <stdio.h>
#include <stdlib.h>
#define N 100
int main()
{
    int a[N];
    int b[N];
    int z[N];
    int x=0,n=0,f=0,q=0,t;
    for(int i=0;i<N;i++){
        a[i]=0;b[i]=0;z[i]=0;
    }
    while (x<N && scanf("%d",&a[x])==1){
        x++;
        if(getchar()=='\n') break;
    }
    for(int i=0;i<x;i++){
        for(int j=0;j<x-i-1;j++){
            if(a[j]>a[j+1]){
                t=a[j];a[j]=a[j+1];a[j+1]=t;
            }
        }
    }
    for(int i=0;i<x;i++){
        b[i]=a[i]/2;
    }
    int mx=0;
    for(int i=0;i<x;i++){
        if(a[i]>x) {
                mx=i;
                break;
        }
    }
    f=mx;
    for(int i=0;i<mx;i++) z[i]=1;
aa:a[mx]-=1;n+=1;
    if(a[mx]!=b[mx]) goto aa;
    for(int i=0;i<x;i++) a[i]-=1;
    z[mx]=1;
bb:for(int i=1;i<x;i++){
        if(a[i]<=b[i] && z[i]==0){q+=1;z[i]=1;}
    }
    if(q>0){
        for(int i=0;i<x;i++) a[i]-=q;
        q=0;
        goto bb;
    }
cc:f++;
    if(f==x) goto ee;
    if(z[f]!=0) goto cc;
dd:a[f]-=1;n+=1;
    if(a[f]>b[f]) goto dd;
    for(int i=0;i<x;i++) a[i]-=1;
    z[f]=1;
    goto bb;
ee:for(int i=0;i<x;i++){
        a[i]-=mx;
        if(a[i]>0) n=n+a[i];
    }
    printf("%d",n);
    return 0;
}
