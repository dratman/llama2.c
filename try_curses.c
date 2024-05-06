#include <ncurses.h>

int main() {
// Initialize ncurses
    initscr();
    start_color(); // Enable color support

    // Define some color pairs
    init_pair(1, COLOR_RED, COLOR_BLACK);
    init_pair(2, COLOR_GREEN, COLOR_BLACK);
    init_pair(3, COLOR_BLUE, COLOR_BLACK);

    // Clear the screen
    clear();

    // Draw some colored text
    attron(COLOR_PAIR(1));
    mvprintw(10, 10, "Red text");
    attroff(COLOR_PAIR(1));

    attron(COLOR_PAIR(2));
    mvprintw(12, 10, "Green text");
    attroff(COLOR_PAIR(2));

    attron(COLOR_PAIR(3));
    mvprintw(14, 10, "Blue text");
    attroff(COLOR_PAIR(3));

    // Refresh the screen
    refresh();

    // Wait for user input
    getch();

    // Clean up
    endwin();
}
// int main() {
//    // Initialize ncurses
//    initscr();
//    start_color(); // Enable color support
//
//    // Define some color pairs
//    init_pair(1, COLOR_RED, COLOR_BLACK);
//
//    // Clear the screen
//    clear();
//
//    // Set background color
//    attron(COLOR_PAIR(1));
//
//    // Fill the entire screen with red color
//    for (int y = 0; y < LINES; y++) {
//        for (int x = 0; x < COLS; x++) {
//            mvaddch(y, x, ' '); // Print a space character
//        }
//    }
//
//    // Turn off color attribute
//    attroff(COLOR_PAIR(1));
//
//    // Refresh the screen
//    refresh();
//
//    // Wait for user input
//    getch();
//
//    // Clean up
//    endwin();
//
//    return 0;
// }
//
// int main() {
// //    printf("\nThis is main()\n");
//
//     // Initialize ncurses
//     initscr();
//     start_color(); // Enable color support
//
//     // Define some color pairs
//     init_pair(1, COLOR_RED, COLOR_BLACK);
//
//     // Clear the screen
//     clear();
//
//     // Set background color
//     attron(COLOR_PAIR(1));
//
//     // Fill the entire screen with red color
//     for (int y = 0; y < LINES; y++) {
//         for (int x = 0; x < COLS; x++) {
//             mvaddch(y, x, ' '); // Print a space character
//         }
//     }
//
//     // Turn off color attribute
//     attroff(COLOR_PAIR(1));
//
//     // Refresh the screen
//     refresh();
//
//     // Wait for user input
//     getch();
//
//     // Clean up
//     endwin();
//
//     return 0;
// }