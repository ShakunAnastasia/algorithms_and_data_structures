#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>

using namespace std;

vector<long long> simulate(int n, int num_robots, const vector<int>& speeds) {
    vector<long long> finish_times;
    finish_times.reserve(n);

    priority_queue<pair<long long, int>, 
                   vector<pair<long long, int>>, 
                   greater<pair<long long, int>>> pq;


    for (int speed : speeds) {
        pq.push({(long long)speed, speed});
    }

    for (int i = 0; i < n; ++i) {

        pair<long long, int> current = pq.top();
        pq.pop();

        long long finish_time = current.first;
        int speed = current.second;

        finish_times.push_back(finish_time);

        pq.push({finish_time + speed, speed});
    }
    
    sort(finish_times.begin(), finish_times.end());
    
    return finish_times;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int na;
    cin >> na;
    vector<int> a(na);
    for (int i = 0; i < na; ++i) cin >> a[i];

    int nb;
    cin >> nb;
    vector<int> b(nb);
    for (int i = 0; i < nb; ++i) cin >> b[i];

    vector<long long> times_A = simulate(n, na, a);
    vector<long long> times_B = simulate(n, nb, b);

    long long max_total_time = 0;

    for (int i = 0; i < n; ++i) {
        long long current_total = times_A[i] + times_B[n - 1 - i];
        if (current_total > max_total_time) {
            max_total_time = current_total;
        }
    }

    cout << max_total_time << endl;

    return 0;
}
