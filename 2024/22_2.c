#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUMBERS 1788
#define N_ITERATIONS 2000
#define MOD_VAL 16777216

// Function to get last digit of a number
int get_last_digit(int num) {
    return abs(num % 10);
}

// Equivalent to Python's next_secret_num function
int next_secret_num(int num) {
    long long result;
    
    // Step 1: multiply by 64
    result = (long long)num * 64;
    num = (int)((result ^ num) % MOD_VAL);
    
    // Step 2: divide by 32 and round down
    result = num / 32;
    num = (int)((result ^ num) % MOD_VAL);
    
    // Step 3: multiply by 2048
    result = (long long)num * 2048;
    num = (int)((result ^ num) % MOD_VAL);
    
    return num;
}

// Function to find max score for a sequence
int find_max_score(int *nums, int *changes, int len, int a, int b, int c, int d) {
    int best_score = 0;
    for (int j = 0; j < len - 3; j++) {
        if (changes[j] == a && changes[j+1] == b && 
            changes[j+2] == c && changes[j+3] == d) {
            int score = nums[j+4];
            if (score > best_score) {
                best_score = score;
            }
        }
    }
    return best_score;
}

int main() {
    FILE *fp = fopen("data/22.txt", "r");
    if (!fp) {
        printf("Error opening file\n");
        return 1;
    }

    // Arrays to store numbers and their sequences
    int initial_nums[MAX_NUMBERS];
    int num_count = 0;
    int **nums = malloc(MAX_NUMBERS * sizeof(int*));
    int **changes = malloc(MAX_NUMBERS * sizeof(int*));
    
    // Read numbers from file
    char line[100];
    while (fgets(line, sizeof(line), fp)) {
        initial_nums[num_count] = atoi(line);
        nums[num_count] = malloc(N_ITERATIONS * sizeof(int));
        changes[num_count] = malloc(N_ITERATIONS * sizeof(int));
        num_count++;
    }
    fclose(fp);

    // Part 1: Process each number through iterations
    long long s_total = 0;
    for (int i = 0; i < num_count; i++) {
        int num = initial_nums[i];
        nums[i][0] = get_last_digit(num);
        
        for (int j = 0; j < N_ITERATIONS; j++) {
            int new_num = next_secret_num(num);
            nums[i][j+1] = get_last_digit(new_num);
            changes[i][j] = get_last_digit(new_num) - get_last_digit(num);
            num = new_num;
        }
        s_total += num;
    }
    printf("Part 1: %lld\n", s_total);

    // Part 2: Find best score
    int best_score = 0;
    long long total_iterations = 19LL * 19 * 19 * 19;
    long long current_iteration = 0;
    for (int a = -9; a <= 9; a++) {
        for (int b = -9; b <= 9; b++) {
            for (int c = -9; c <= 9; c++) {
                for (int d = -9; d <= 9; d++) {
                    int score = 0;
                    for (int i = 0; i < num_count; i++) {
                        score += find_max_score(nums[i], changes[i], N_ITERATIONS, a, b, c, d);
                    }
                    if (score > best_score) {
                        best_score = score;
                    }
                    current_iteration++;
                    printf("\rProgress: %.2f%%", (double)current_iteration / total_iterations * 100);
                    fflush(stdout);
                }
            }
        }
    }
    printf("\nPart 2: %d\n", best_score);

    // Free allocated memory
    for (int i = 0; i < num_count; i++) {
        free(nums[i]);
        free(changes[i]);
    }
    free(nums);
    free(changes);

    return 0;
}
