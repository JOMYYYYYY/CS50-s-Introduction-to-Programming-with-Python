#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_population;
    do{
        start_population = get_int("please input a integer bigger than or equal to 9: ");
    }
    while (start_population < 9);

    // TODO: Prompt for end size
    int end_population;
    do{
        end_population = get_int("please input a integer bigger than the start population: ");
    }
    while (end_population < start_population);

    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    int population = start_population;
    while(population < end_population){
        population = population + population/3 - population/4;
        year++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", year);
}
