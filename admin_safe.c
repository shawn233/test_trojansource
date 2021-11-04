#include <stdio.h>
#include <stdbool.h>

int main() {
    bool isAdmin = false;
    /* begin admin only */ if (isAdmin) {
        printf("You are an admin.\n");
    /* end admin only */ }
    return 0;
}