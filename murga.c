#include<stdio.h>
int main(){
    int legs=94;
    int heads=35;
    int x=35/2;
    int y=x+1;
    while(2*x+4*y!=legs){
        x++;
        y--;
    }
    if(2*x+4*y==legs){
        printf("%d\n%d",x,y);
    }
}