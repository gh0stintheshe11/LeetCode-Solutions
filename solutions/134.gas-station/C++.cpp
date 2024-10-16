class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalGas = 0, totalCost = 0, startIndex = 0, tank = 0;
        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                startIndex = i + 1;
                tank = 0;
            }
        }
        return totalGas >= totalCost ? startIndex : -1;
    }
};