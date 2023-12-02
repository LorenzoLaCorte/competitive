#include <bits/stdc++.h>
using namespace std;

int64_t INF = 9223372036854775806;

int solve(int64_t n, vector<int64_t> results){
    ostringstream os;
    os << n;
    string digits = os.str();

    if (results[n] == INF){
        for(char digit : digits){
            int64_t d = digit - '0';
            int64_t res; 
            if (results[n-d] == INF){
                res = solve(n-d, results);
                results[n-d] = res;
            }
            if (results[n-d] < results[n]){
                results[n] = results[n-d]; 
            }
        }
    }

    cout << "results["<< n << "] + 1 is " << results[n] + 1 << endl;
    return results[n] + 1;
}

int main(){
    int64_t n;
    cin >> n;
    vector<int64_t> results(n+1);
    for(int i=0; i<results.size(); i++){
        if(i<10) results[i] = 0;
        else results[i] = INF;
    }
    cout << solve(n, results) << endl;
}