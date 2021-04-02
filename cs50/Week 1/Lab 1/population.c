//#include <cs50.h>
#include <stdio.h>

void calculateYears(void);

int main(void)
{
    calculateYears();
}

void calculateYears()
{
    //Declaration of variables start-size and end-size
    int start_size;
    int end_size;

    // TODO: Prompt for start size
    do
    {
        start_size = get_int("Define start size: ");
    } while (start_size < 9);

    // TODO: Prompt for end size
    do
    {
        end_size = get_int("Define end size: ");
    } while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold

    int years_it_takes = 0;

    while (start_size < end_size)
    {
        start_size = start_size + start_size / 3 - start_size / 4;

        years_it_takes++;
    }
    printf("Years: %i\n", years_it_takes);
}

// Works in CS50 IDE but not in vs-code due to problems with the cs50 library