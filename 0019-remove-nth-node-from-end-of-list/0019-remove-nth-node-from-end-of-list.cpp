

using namespace std;
class Solution
{
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    int length = 1;
    ListNode* current = head;

    while (current->next) {
        length++;
        current = current->next;
    }

    // head silinecekse
    if (length == n) {
        return head->next;
    }

    current = head;
    while (length - n - 1 > 0) {
        current = current->next;
        length--;
    }

    if (current->next) {
        current->next = current->next->next;
    }

    return head;
}
};