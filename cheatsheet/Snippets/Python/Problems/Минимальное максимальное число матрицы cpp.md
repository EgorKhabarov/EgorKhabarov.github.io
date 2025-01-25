```cpp@maxminmatrix.cpp
#include <iostream>
#include <vector>
#include <time.h>
#include <iomanip>

using namespace std;

int main() {
    int rows = 3;
    int cols = 4;
    srand(time(NULL));
    vector<vector<int>> matrix(rows, vector<int>(cols, 0));
    for (int i = 0; i < rows; ++i) {
        cout << "|";
        for (int j = 0; j < cols; ++j) {
            int number = 1 + rand() % 999;
            matrix[i][j] = number;
            cout << " " << setw(3) << setfill(" ") << number << " |";
        }
        cout << "\n";
    }
    int max = 0;
    int min = 999;
    for (auto r : matrix) {
        for (auto c : r) {
            if (c > max) max = c;
            if (c < min) min = c;
        }
    }
    cout << "max = " << max << "\n" << "min = " << min << "\n";
    return 0;
}
```
