#include <stdio.h>

int main(){
    puts("Please input the 6 digit PIN number for administrator access: ");
    int num;
    scanf("%d", &num);  
    if (num == 194832){
        puts("Welcome to the mainframe ADMIN");
    } else {
        puts("You're not the admin....");
    }
    return 0;
}
