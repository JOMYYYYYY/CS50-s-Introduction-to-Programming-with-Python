#include <stdio.h>
// #include <cs50.h>

int main (void)
{
    // int n = 50;
    // int *p = &n;
    // printf("%p\n", p);
    // printf("%i\n", *p);

    //string s = "hi"; // string require #include <cs50.h> to work well
    char *s = "hi!";
    printf("%s\n", s); //print "hi"
    printf("%p\n", s); //print the memory location
    printf("%c\n", s[0]); //print the first character of s
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("%c\n", s[3]);

    printf("-----\n");

    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    //printf("%c\n", *(s + 30000)); // print whatever in there

    printf("-----\n");

    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);

    printf("-----\n");

    printf("%s\n", s);
    printf("%s\n", s + 1);
    printf("%s\n", s + 2);




}