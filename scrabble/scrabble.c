#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
int compute_score(string word);
int get_index(char n);

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
        if (score1 == score2)
    {
        printf("Tie!\n");
    }
        if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int length = strlen(word);
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum = sum + POINTS[get_index(word[i])];
    }
    return sum;
}

int get_index(char my_char) {
    char low[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    char up[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    int index;
    for (index = 0; index < 26; index++)
    {
        if (my_char == low[index] || my_char == up[index])
        {
            return index;
        }
    }
    index = 26;
    return index;
}
