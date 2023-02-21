#include <stdio.h>
int add(int a , int b)
{
    int c  = a + b;
    return c;
}

int main()
{
    int x = 5;
    int y = 7;
    int z = add(x,y);
    printf("z=%d\n", z);
    return 0;
}