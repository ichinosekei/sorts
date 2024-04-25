#include <iostream>
#include <vector>
#include <sstream> 
#include "merge_sort.h"
#include "quick_sort.h"
#include "bubble_sort.h"
#include "radix_sort.h"
#include "counting_sort.h"
#include "heap_sort.h"


// Функция main, которая определяет, какую сортировку запускать
int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <algorithm>\n";
        return 1;
    }
    std::string algorithm = argv[1];
    std::string input_line;
    std::getline(std::cin, input_line);
    std::istringstream iss(input_line);
    std::vector<int> arr;
    int number;
    while (iss >> number) {
        arr.push_back(number);
    }
       std::cout << algorithm << std::endl;
    if (algorithm == "merge") {
        mergeSort(arr, 0, arr.size() - 1);
    } else if (algorithm == "quick") {
        quickSort(arr, 0, arr.size() - 1);
    } else if (algorithm == "bubble") {
        bubbleSort(arr);
    } else if (algorithm == "radix") {
        radixSort(arr);
    } else if (algorithm == "counting") {
        countingSort(arr);
    } else if (algorithm == "heap") {
        heapSort(arr);
    } else {
        std::cerr << "Unknown algorithm: " << algorithm << std::endl;
        return 1;
    }

    // for (int num : arr) {
    //     std::cout << num << " ";
    // }
    // std::cout << std::endl;
    return 0;
}
