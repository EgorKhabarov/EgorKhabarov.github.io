<p>```cpp@maxminmatrix.cpp</p>
<h1>include <iostream></h1>
<h1>include <vector></h1>
<h1>include <time.h></h1>
<h1>include <iomanip></h1>
<p>using namespace std;</p>
<p>int main()
{
    int rows = 3;
    int cols = 4;
    srand(time(NULL));
    vector<vector\<int>> matrix(rows, vector<int>(cols, 0));
    for (int i = 0; i &lt; rows; ++i) {
        cout &lt;&lt; "|";
        for (int j = 0; j &lt; cols; ++j) {
            int number = 1 + rand() % 999;
            matrix[i][j] = number;
            cout &lt;&lt; " " &lt;&lt; setw(3) &lt;&lt; setfill(" ") &lt;&lt; number &lt;&lt; " |";
        }
        cout &lt;&lt; "\n";
    }
    int max = 0;
    int min = 999;
    for (auto r : matrix) {
        for (auto c : r) {
            if (c &gt; max) max = c;
            if (c &lt; min) min = c;
        }
    }
    cout &lt;&lt; "max = " &lt;&lt; max &lt;&lt; "\n" &lt;&lt; "min = " &lt;&lt; min &lt;&lt; "\n";
    return 0;
}
```</p>