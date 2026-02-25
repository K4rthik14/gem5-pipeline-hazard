#include <stdio.h>
int arr[1000];
int main() {
    for (int i = 0; i < 1000; i++) {
        arr[i] = i * 2;
        int x = arr[i] + arr[0];
        printf("%d\n", x);
    }
    return 0;
}
