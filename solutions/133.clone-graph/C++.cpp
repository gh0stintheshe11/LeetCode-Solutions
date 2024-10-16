/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        unordered_map<Node*, Node*> cloned;
        queue<Node*> q;
        q.push(node);

        // Create the clone for the root node.
        cloned[node] = new Node(node->val);

        while (!q.empty()) {
            Node* current = q.front();
            q.pop();

            // Iterate through each neighbor of the node
            for (Node* neighbor : current->neighbors) {
                if (cloned.find(neighbor) == cloned.end()) {
                    // Clone the neighbor node and push it to the queue
                    cloned[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                // Link the clone node to the clone of its neighbors
                cloned[current]->neighbors.push_back(cloned[neighbor]);
            }
        }

        return cloned[node];
    }
};