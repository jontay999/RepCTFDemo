// make sure to compile with no stack protector
// gcc -fno-stack-protector -o demo demo.c
#include <stdio.h>
#include <stdlib.h>

void win(){
    puts("I'm in");
    FILE *file = fopen(".SUPER_SECRET.txt", "r");
    if (file) {
        char ch;
        while ((ch = fgetc(file)) != EOF) putchar(ch);
        fclose(file);
    }
	exit(0);
}

void shell(){
    system("/bin/bash");
    exit(0);
}


int main() {
    char buffer[60];
    puts("Hello world, this is my first C program");
    printf("Address of win() function: %p\n", (void*) win);
    printf("Address of shell() function: %p\n", (void*) shell);
    fgets(buffer, 0x60, stdin);
    return 0;
}
