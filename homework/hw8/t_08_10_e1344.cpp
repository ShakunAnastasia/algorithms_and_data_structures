#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <tuple>

using namespace std;

struct Student {
    string surname, name;
    int grade;
    char letter;
    int d, m, y;
};

bool operator<(const Student& a, const Student& b) {
    return tie(a.grade, a.letter, a.surname, a.name) < 
           tie(b.grade, b.letter, b.surname, b.name);
}

int main() {
    int n;
    if (!(cin >> n)) return 0;

    vector<Student> students(n);

    for (int i = 0; i < n; ++i) {
        string dateStr;
        cin >> students[i].surname >> students[i].name 
            >> students[i].grade >> students[i].letter >> dateStr;
        students[i].d = stoi(dateStr.substr(0, 2));
        students[i].m = stoi(dateStr.substr(3, 2));
        students[i].y = stoi(dateStr.substr(6, 2));
    }
  
    sort(students.begin(), students.end());
    for (const auto& s : students) {
        cout << s.grade << s.letter << " " << s.surname << " " << s.name << " "
             << setfill('0') << setw(2) << s.d << "."
             << setfill('0') << setw(2) << s.m << "."
             << setfill('0') << setw(2) << s.y << endl;
    }

    return 0;
}
