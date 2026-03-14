#include <iostream>
#include <list>
#include <string>
using namespace std;

class HashMap {
private:
    int capacity;
    list<pair<int, int>>* table;

    int hashFunction(int key) {
        return key % capacity;
    }

public:
    HashMap(int cap = 10) : capacity(cap) {
        table = new list<pair<int, int>>[capacity];
    }

    ~HashMap() {
        delete[] table;
    }

    // Insert key-value pair
    void insert(int key, int value) {
        int index = hashFunction(key);
        for (auto& p : table[index]) {
            if (p.first == key) {
                p.second = value; // update if key exists
                return;
            }
        }
        table[index].push_back({key, value});
    }

    // Get value by key
    int get(int key) {
        int index = hashFunction(key);
        for (auto& p : table[index]) {
            if (p.first == key)
                return p.second;
        }
        return -1; // not found
    }

    // Remove a key
    void remove(int key) {
        int index = hashFunction(key);
        table[index].remove_if([key](const pair<int,int>& p) {
            return p.first == key;
        });
    }

    // Check if key exists
    bool contains(int key) {
        int index = hashFunction(key);
        for (auto& p : table[index]) {
            if (p.first == key) return true;
        }
        return false;
    }

    void display() {
        for (int i = 0; i < capacity; i++) {
            if (!table[i].empty()) {
                cout << "Bucket " << i << ": ";
                for (auto& p : table[i])
                    cout << "[" << p.first << "=" << p.second << "] ";
                cout << "\n";
            }
        }
    }
};

int main() {
    HashMap map;

    map.insert(1, 10);
    map.insert(2, 20);
    map.insert(11, 30); // collision with key 1 (11 % 10 == 1)
    map.insert(3, 40);

    map.display();

    cout << "Get key 2: " << map.get(2) << "\n";
    cout << "Contains key 11: " << map.contains(11) << "\n";

    map.remove(11);
    cout << "After removing key 11:\n";
    map.display();

    return 0;
}
```

**Key concepts used:**

- **Hash function** — `key % capacity` maps keys to bucket indices
- **Chaining** — each bucket holds a `list` of pairs to handle collisions
- **Operations** — `insert`, `get`, `remove`, `contains` all run in O(1) average, O(n) worst case

**Output:**
```
Bucket 1: [1=10] [11=30]
Bucket 2: [2=20]
Bucket 3: [3=40]
Get key 2: 20
Contains key 11: 1
After removing key 11:
Bucket 1: [1=10]
Bucket 2: [2=20]
Bucket 3: [3=40]
