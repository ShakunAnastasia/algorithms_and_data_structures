#include <iostream>
#include <vector>

using namespace std;

class HashTable {
private:
    static const int CAPACITY = 200003;
    vector<int> table[CAPACITY];
    int unique_count;

public:
    HashTable() : unique_count(0) {}

    void add(int phone) {
        int h = phone % CAPACITY;

        for (int existing_phone : table[h]) {
            if (existing_phone == phone) {
                return;
            }
        }

        table[h].push_back(phone);
        unique_count++;
    }

    int getUniqueCount() const {
        return unique_count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    HashTable ht;
    for (int i = 0; i < n; ++i) {
        int phone;
        cin >> phone;
        ht.add(phone);
    }

    cout << ht.getUniqueCount() << endl;

    return 0;
}
