#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

string toLower(string s) {
    for (int i = 0; i < s.length(); i++) {
        s[i] = (char)tolower((unsigned char)s[i]);
    }
    return s;
}

struct Node {
    string word;
    bool used;
    Node* next;
    Node(string w) : word(w), used(false), next(nullptr) {}
};

class VocabularyTable {
private:
    static const int CAPACITY = 5003;
    Node* table[CAPACITY];

    int getHash(string s) {
        long long h = 0;
        for (char c : s) {
            h = (h * 31 + (unsigned char)c) % CAPACITY;
        }
        return (int)h;
    }

public:
    VocabularyTable() {
        for (int i = 0; i < CAPACITY; i++) table[i] = nullptr;
    }

    void insert(string s) {
        int h = getHash(s);
        Node* curr = table[h];
        while (curr) {
            if (curr->word == s) return;
            curr = curr->next;
        }
        Node* newNode = new Node(s);
        newNode->next = table[h];
        table[h] = newNode;
    }

    bool checkAndMark(string s) {
        int h = getHash(s);
        Node* curr = table[h];
        while (curr) {
            if (curr->word == s) {
                curr->used = true;
                return true;
            }
            curr = curr->next;
        }
        return false;
    }

    bool allUsed() {
        for (int i = 0; i < CAPACITY; i++) {
            Node* curr = table[i];
            while (curr) {
                if (!curr->used) return false;
                curr = curr->next;
            }
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    VocabularyTable vt;
    string w;
    for (int i = 0; i < n; i++) {
        cin >> w;
        vt.insert(toLower(w));
    }

    string line;
    getline(cin, line); 

    bool unknownFound = false;

    for (int i = 0; i < m; i++) {
        if (!getline(cin, line)) break;
        string currentWord = "";
        for (unsigned char c : line) {
            if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                currentWord += (char)tolower(c);
            } else {
                if (!currentWord.empty()) {
                    if (!vt.checkAndMark(currentWord)) {
                        unknownFound = true;
                    }
                    currentWord = "";
                }
            }
        }
        if (!currentWord.empty()) {
            if (!vt.checkAndMark(currentWord)) {
                unknownFound = true;
            }
        }
    }

    if (unknownFound) {
        cout << "Some words from the text are unknown." << endl;
    } else if (!vt.allUsed()) {
        cout << "The usage of the vocabulary is not perfect." << endl;
    } else {
        cout << "Everything is going to be OK." << endl;
    }

    return 0;
}
