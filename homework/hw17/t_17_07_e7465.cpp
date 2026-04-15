#include <iostream>

using namespace std;

class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Tree {
private:
    TreeNode* insertNode(TreeNode* node, int val) {
        if (node == NULL) {
            return new TreeNode(val);
        }
        if (val < node->val) {
            node->left = insertNode(node->left, val);
        } else {
            node->right = insertNode(node->right, val);
        }
        return node;
    }

    bool compareNodes(TreeNode* n1, TreeNode* n2) {
        if (n1 == NULL && n2 == NULL) return true;
        if (n1 == NULL || n2 == NULL) return false;
        if (n1->val != n2->val) return false;
        return compareNodes(n1->left, n2->left) && compareNodes(n1->right, n2->right);
    }

public:
    TreeNode *head;
    Tree() : head(NULL) {};

    void Insert(int val) {
        head = insertNode(head, val);
    }

    int IsSameTree(Tree *p) {
        if (compareNodes(this->head, p->head)) return 1;
        return 0;
    }
};

int main() {
    int n, m, val;
    Tree tree1, tree2;

    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; i++) {
        cin >> val;
        tree1.Insert(val);
    }

    if (!(cin >> m)) return 0;
    for (int i = 0; i < m; i++) {
        cin >> val;
        tree2.Insert(val);
    }

    cout << tree1.IsSameTree(&tree2) << endl;

    return 0;
}
