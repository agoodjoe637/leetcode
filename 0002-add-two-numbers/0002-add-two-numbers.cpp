/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {

        ListNode *sum = new ListNode();
        ListNode *tail = sum;
        int elde = 0;

        while (l1 != nullptr || l2 != nullptr || elde != 0)
        {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;
            int toplam = val1 + val2 + elde;
            if (toplam < 10)
            {
                elde = 0;
            }
            else
            {
                elde = toplam / 10;
            }
            tail->next = new ListNode(toplam % 10);
            tail = tail->next;
            if (l1 != nullptr )
            {
                l1 = l1->next;
            }
            if (l2 != nullptr)
            {
                l2 = l2->next;
            }
        }
        return sum->next;
    }
};