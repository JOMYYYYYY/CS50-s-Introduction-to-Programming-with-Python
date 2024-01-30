#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
int count_words(string text);
int count_letters(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    //printf("letters: %d\nwords: %d\nsentences: %d\n", count_letters(text), count_words(text), count_sentences(text));
    float L = ((float)count_letters(text) / (float)count_words(text)) * 100.0;
    float S = ((float)count_sentences(text) / (float)count_words(text)) * 100.0;
    //printf("L: %f\nS: %f\n", L, S);
    float long_index = 0.0588 * L - 0.296 * S - 15.8;
    int index = round(long_index);
    if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    else
    {
        printf("Grade %d\n", index);
        return 0;
    }



}

int count_words(string text)
{
    int n = 0;
    int count = 1;
    while (text[n] != '\0')
    {
        if (text[n] == ' ')
        {
            count++;
        }
        n++;
    }
    return count;
}

int count_letters(string text)
{
    int n = 0;
    int m = 0;
    while (text[n] != '\0')
    {
        n++;
    }
    for (int i = 0; i <= n; i++)
    {
         if (isalpha(text[i]))
        {
            m++;
        }
    }
    return m;
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