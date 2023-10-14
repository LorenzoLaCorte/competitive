#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;
const int DEF_VAL = -10;

int64_t find_min(int64_t n, vector<int64_t>& v){
    int64_t min = n;
    for (int64_t el: v){
        if (el < min) min = el;
    }
    return min;
}

int64_t solve(int64_t n, vector<int64_t>& coins, vector<int64_t>& results) {
    if (n == 0) return 0;

    int64_t coin_needed = -1;
    vector<int64_t> coin_costs;

    for(int64_t coin: coins){
        if (coin > n) continue;
        if (results[n - coin] != DEF_VAL){
            coin_needed = results[n - coin];
        }
        else {
            coin_needed = solve(n-coin, coins, results);
            results[n - coin] = coin_needed;
        }
        if (coin_needed != -1){
            coin_costs.push_back(coin_needed);
        }
    }

    if(coin_costs.empty()) {
        return -1;
    }
    int64_t coin_cost = 1 + find_min(n, coin_costs);
    return coin_cost;
}

int main() {
    int64_t num_coins, n;

    cin >> num_coins;
    cin >> n;

    vector<int64_t> coins(num_coins);

    for (int64_t i = 0; i < num_coins; i++) {
        cin >> coins[i];
    }
    std::sort(coins.rbegin(), coins.rend());

    vector<int64_t> results(n, DEF_VAL); // Initialize results with -1

    // for (int64_t el: results)
    //     cout << "el is: " << el << endl;

    int64_t res = solve(n, coins, results);
    
    // int64_t i = 0;
    // for (int64_t el: results){
    //         cout << "I need " << el << " coins " << "for " << i << endl;
    //         i++;
    // }

    cout << res << endl;

    return 0;
}
