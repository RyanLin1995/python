#include<stdio.h>
void DeadLoop()
{
    while(1)
    {
        ;
    }
}
int main(int argc, char **argv)
{
    DeadLoop();
}
