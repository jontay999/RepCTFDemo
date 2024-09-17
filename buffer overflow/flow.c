#include <stdio.h>
#include <stdlib.h>

void win(){
    puts("I'm in 😎");
    FILE *file = fopen(".SUPER_SECRET.txt", "r");
    if (file) {
        char ch;
        while ((ch = fgetc(file)) != EOF) putchar(ch);
        fclose(file);
    }
	exit(0);
}

int main() {
    puts("Time to hack the mainframe...");
    char name[60];
    int secret = 0xdeadbeef;
    fgets(name, 0x600, stdin);
    if (secret == 0x1337) {
        win();
    } else {
        printf("The secret is 0x%x\n", secret);
        puts("I guess you're not cool enough to see my secret");
    }
}