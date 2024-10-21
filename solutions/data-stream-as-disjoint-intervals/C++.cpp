#include <set>
#include <vector>

using namespace std;

class SummaryRanges {
public:
    set<pair<int, int>> intervals;

    SummaryRanges() {}

    void addNum(int value) {
        auto it = intervals.lower_bound({value, value});

        if (it != intervals.begin() && prev(it)->second + 1 >= value) {
            --it;
        }

        int start = value, end = value;

        while (it != intervals.end() && it->first <= end + 1) {
            start = min(start, it->first);
            end = max(end, it->second);
            it = intervals.erase(it);
        }

        intervals.insert(it, {start, end});
    }

    vector<vector<int>> getIntervals() {
        vector<vector<int>> result;
        for (const auto &interval : intervals) {
            result.push_back({interval.first, interval.second});
        }
        return result;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */