#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdbool.h>

void initialize_sim(int *road, int *velocities, int roadLength, int numCars, FILE *filename, int printData, int vMax);
int update(int *road, int *velocities, int roadLength, int numCars, FILE *filename, float brakeProb, int printData, int vMax, int speedModified);

int main(int argc, char *argv[])
{
    // Checks that user put in correct number of arguments.
    if (argc < 8)
    {
        printf("Program Run Layout\n");
        printf("./test.x density brake Probability road length number of iterations printData? rain probability Speed change based on location?\n");
        return 0;
    }

    // Various quantities that user can change.
    double density = atof(argv[1]);
    double brakeProb = atof(argv[2]);
    int roadLength = atoi(argv[3]);
    int iterations = atoi(argv[4]);
    int printData = atoi(argv[5]);
    float rainProb = atof(argv[6]);
    int speedModified = atoi(argv[7]);
    int vMax = 5;

    // File IO stuff.
    FILE *data, *flowData, *velocityData;

    // Declare arrays that are needed for the program.
    int numCars = (int)(density * roadLength);
    int road[roadLength];
    int velocities[numCars];

    // Time-keeping stuff.
    clock_t start, end;
    double elapsed_time;

    // This is needed for calculating the flux correctly.
    // Based on how the paper calculated these numbers.
    int counter = 0;
    int dummy;
    int t0 = 10 * roadLength;
    double calculatedFlow;
    double velocityAverage = 0.0;

    start = clock();
    srand(time(NULL));

    // Start writing to the files.
    data = fopen("roaddata.txt", "w");
    flowData = fopen("flowdata.txt", "a");
    velocityData = fopen("velocitydata.txt", "a");

    // Initialize road state.
    initialize_sim(road, velocities, roadLength, numCars, data, printData, vMax);

    for (int i = 0; i < iterations + t0; i++)
    {
        // This is where we iterate through our program. The dummy part is just for getting the right simulation results 
        // since that is how the paper conducted the simulation.
        if (i <= t0)
        {
            dummy = update(road, velocities, roadLength, numCars, data, brakeProb, printData, vMax, speedModified);
        }
        else
        {
            // Check if it is raining or sunny.
            if ((float)rand() / (float)RAND_MAX < rainProb)
            {
                counter += update(road, velocities, roadLength, numCars, data, brakeProb, printData, vMax - 2, speedModified);
            }
            else
            {
                counter += update(road, velocities, roadLength, numCars, data, brakeProb, printData, vMax, speedModified);
            }

            for (int i = 0; i < numCars; i++)
            {
                velocityAverage += velocities[i];
            }
            velocityAverage /= numCars;
        }
    }

    // Calculate the flow and write to file.
    calculatedFlow = (double)counter / (double)(iterations);
    fprintf(flowData, "%f\t%f\n", (double)density, (double)calculatedFlow);
    fprintf(velocityData, "%f\t%f\n", (double)density, (double)velocityAverage);
    fclose(data);
    fclose(flowData);
    fclose(velocityData);

    end = clock();
    elapsed_time = ((double)end - start) / CLOCKS_PER_SEC;

    printf("Elapsed time: %f\n", elapsed_time);
    return 0;
}

void initialize_sim(int *road, int *velocities, int roadLength, int numCars, FILE *filename, int printData, int vMax)
{
    /*
    Initializes the road state.
    Takes in the road, velocities, road length, etc.
    Returns nothing.
    */
    int pos;
    for (int i = 0; i < roadLength; i++)
    {
        // Initialize array to be have empty states.
        road[i] = -1;
    }

    for (int i = 0; i < numCars; i++)
    {
        // Randomly choose a position for the car.
        do
        {
            pos = rand() % roadLength;
        } while (road[pos] != -1);

        // Assign car id to that road position.
        road[pos] = i;

        // velocities[i] = rand() % VMAX + 1;

        // Initialize the velocity to zero since the paper initialized that way.
        velocities[i] = 0;
    }
    if (printData != 0)
    {
        // Decides to print the data or not.

        for (int i = 0; i < roadLength; i++)
        {
            if (road[i] != -1)
            {
                // Print the velocity at the ith position for the each car.
                fprintf(filename, "%d", velocities[road[i]]);
            }
            else
            {
                // Print . for empty spaces.
                fprintf(filename, ".");
            }
        }
        fprintf(filename, "\n");
    }
}

int update(int *road, int *velocities, int roadLength, int numCars, FILE *filename, float brakeProb, int printData, int vMax, int speedModified)
{
    /*
    Updates the positions of the cars along our road.
    Takes the road, velocities, road length, and other data.
    Outputs the number of cars that cross.
    */
    int nextCarPosition[roadLength];
    int car;
    int distance;
    int is_inSection = 0;
    int carsCrossed = 0;

    for (int i = 0; i < roadLength; i++)
    {
        // Initializes a temporary array so that we do not
        // modify our original cars array.
        nextCarPosition[i] = -1;
    }

    for (int i = 0; i < roadLength; i++)
    {
        if (road[i] != -1) // Check if there is a car on this cell.
        {
            car = road[i]; // Assign the current car the id number along the road.

            if (speedModified == 1)
            {
                // Check if there are speed limits along the road.

                if ((int)roadLength / 2 < i && (int)(3 * roadLength / 4) > i && !is_inSection)
                {
                    // If car is within 1/2 of road and less than 3/4 of the road its max speed
                    // will decrease by 2.
                    vMax -= 2;
                    is_inSection = 1;
                }
            }

            if (velocities[car] < vMax)
            {
                // Rule 1: If car is not going the max speed then increase the speed by 1.
                velocities[car]++;
            }

            distance = 1; // Measures the distance between the current car and the next
            while (road[(i + distance) % roadLength] == -1 && distance <= velocities[car] && distance <= vMax)
            {
                // While the cell ahead is empty and the distance is not greater than the
                // velocity, increase the distance.
                distance++;
            }

            // Rule 2: If there is a car ahead that is a distance less than the velocity then make the
            // new velocity the distance of the car minus 1.
            // Note: If the velocity is max then the while loop above will make the distance 6, and
            // the current velocity will be 6-1 = 5.
            velocities[car] = distance - 1;

            if ((float)rand() / (float)RAND_MAX <= brakeProb && velocities[car] > 0)
            {
                // Rule 3: Spontaneous breaking. Interpretation-wise this can be a number of things
                // but this is what makes our simulation more realistic than a typical cellular
                // automata model.
                velocities[car]--;
            }

            // Rule 4: Move the car ahead by its velocity but keep in mind
            // of periodic boundary conditions.
            nextCarPosition[(i + velocities[car]) % roadLength] = car;

            if (i + velocities[car] >= roadLength)
            {
                // This checks for the number of cars that crosses some point
                // (in this case the "end" of the road) and helps us
                // calculate the flux.
                carsCrossed++;
            }
        }
    }

    for (int i = 0; i < roadLength; i++)
    {
        // Now that we've calculated everything let's update the road state.
        road[i] = nextCarPosition[i];
    }

    if (printData != 0)
    {
        // Just checks if we want to print the road data.
        // This will be slow if we have a large road and many timesteps.
        for (int i = 0; i < roadLength; i++)
        {
            if (road[i] != -1)
            {
                // If the cell is occupied, print the velocity of that car at the ith spot.
                fprintf(filename, "%d", velocities[road[i]]);
            }
            else
            {
                // Print a . for non-occupied cells.
                fprintf(filename, ".");
            }
        }
        fprintf(filename, "\n");
    }

    // Return the number of cars that crossed.
    return carsCrossed;
}