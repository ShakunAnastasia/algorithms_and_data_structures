#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Employee {
    int id;
    int fee;
    vector<Employee*> subordinates;

    Employee() : id(0), fee(0) {}
};

int getMinFee(Employee* e) {
    if (e->subordinates.empty()) {
        return e->fee;
    }

    int minSubFee = -1;
    for (Employee* sub : e->subordinates) {
        int currentSubFee = getMinFee(sub);
        if (minSubFee == -1 || currentSubFee < minSubFee) {
            minSubFee = currentSubFee;
        }
    }
    
    return e->fee + minSubFee;
}

int main() {
    int n;
    if (!(cin >> n)) return 0;

    vector<Employee*> staff(n + 1);
    for (int i = 1; i <= n; ++i) {
        staff[i] = new Employee();
        staff[i]->id = i;
    }

    for (int i = 1; i <= n; ++i) {
        int d, k;
        cin >> d >> k;
        staff[i]->fee = d;
        for (int j = 0; j < k; ++j) {
            int subId;
            cin >> subId;
            staff[i]->subordinates.push_back(staff[subId]);
        }
    }

    cout << getMinFee(staff[1]) << endl;

    return 0;
}
