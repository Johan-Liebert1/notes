#include <iostream>

using namespace std;

struct Node {
    int value;
    struct Node* next;
    struct Node* prev;
};

class LinkedList {
   private:
    struct Node* start;
    struct Node* end;

   public:
    LinkedList(int val) {
        struct Node node;

        node.value = val;
        node.next = NULL;

        start = &node;
        end = &node;

        cout << "constructor start = " << start->value << "&start, &end" << &start << &end << "\n";
    }

    void insertNode(int value) {
        cout << "inserting " << value << " start = " << start->value << endl;

        struct Node newNode;

        newNode.value = value;

        end->next = &newNode;
        end = end->next;
    }

    int iterate() {
        cout << start->value;
        return 1;

        Node* ptr = start;

        while (ptr->next != NULL) {
            cout << "value " << ptr->value << " ";
            ptr = ptr->next;
        }
    }
};

int main() {
    LinkedList ll(6);

    ll.insertNode(7);
    ll.insertNode(8);
    ll.insertNode(9);
    ll.insertNode(10);
    ll.insertNode(11);
    ll.insertNode(12);

    ll.iterate();
}