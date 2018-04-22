ublic class Solution {
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // write your code here
        return buildTree(preorder, inorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }
    
    private TreeNode buildTree(int[] preorder, int[] inorder, int preStart, int preEnd, int inStart, int inEnd){
        if(preStart > preEnd || inStart > inEnd)
            return null;
        int val = preorder[preStart];
        TreeNode root = new TreeNode(val);
        int temp = inStart;
        while(inorder[temp] != val)
            temp++;
        root.left = buildTree(preorder, inorder, preStart + 1, preStart + 1 + temp - 1 - inStart, inStart, temp - 1);
        root.right = buildTree(preorder, inorder, preEnd - (inEnd - temp - 1), preEnd, temp + 1, inEnd);
        return root;
    }
}
