#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include "counting_sort.h" 

void countingSort(std::vector<int>& array) {
    int max_val = *std::max_element(array.begin(), array.end());
    int min_val = *std::min_element(array.begin(), array.end());
    std::vector<int> counts(max_val - min_val + 1, 0);

    for (int num : array) {
        counts[num - min_val]++;
    }

    int index = 0;
    for (int i = 0; i <= max_val - min_val; i++) {
        while (counts[i] > 0) {
            array[index++] = i + min_val;
            counts[i]--;
        }
    }
}


