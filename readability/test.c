#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int a = count_sentences(text);
    printf("%d\n", a);


}


int count_sentences(string text)
{
    int n = 0;
    int count = 0;
    while (text[n] != '\0')
    {
        if ((text[n] == '.') || (text[n] == '!') || (text[n] == '?'))
        {
            count++;
        }
        n++;
    }
    return count;
}