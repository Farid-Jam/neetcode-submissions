class ListNode {
    public:
    int val;
    ListNode* next;

    ListNode (int val): val(val), next(nullptr){};

    ListNode (int val, ListNode* next): val(val), next(next){};
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;
public:
    LinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    int get(int index) {
        ListNode* curr = head->next;
        int i = 0;
        while (curr != nullptr){
            if (i == index){
                return curr->val;
            }
            i++;
            curr = curr->next;
        }
        return -1;
    }

    void insertHead(int val) {
        ListNode* newNode = new ListNode(val);
        newNode->next = head->next;
        head->next = newNode;
        if (newNode->next == nullptr){
            tail = newNode;
        }
    }
    
    void insertTail(int val) {
        ListNode* newNode = new ListNode(val);
        tail->next = newNode;
        tail = newNode;
    }

    bool remove(int index) {
        int i = 0;
        ListNode* curr = head;
        while (i < index && curr != nullptr){
            i++;
            curr = curr->next;
        }
        if (curr != nullptr && curr->next != nullptr){
            ListNode* toDelete = curr->next;
            if (toDelete == tail) {
            tail = curr;
            }
            curr->next = curr->next->next;
            delete toDelete;
            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector<int> values;
        ListNode* curr = head->next;
        while (curr != nullptr){
            values.push_back(curr->val);
            curr = curr->next;
        }
        return values;
    }
};
