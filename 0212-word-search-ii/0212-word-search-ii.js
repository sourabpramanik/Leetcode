/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */

class Node{
    constructor(){
        this.links = {}
        this.end = false
    }
}

class Trie{
    constructor(){
        this.root = new Node()
    }
    
    insert(word){
        let root = this.root
        for(let i=0; i<word.length; i++){
            if(!root.links[word[i]]){
                root.links[word[i]] = new Node()
            }
            root = root.links[word[i]]
        }
        root.end = true
    }
}
var findWords = function(board, words) {
    let trie = new Trie();
    let ans = [];
    for(let word of words){
        trie.insert(word)
    }
    
    for(let i=0; i<board.length; i++){
        for(let j=0; j<board[0].length; j++){
            dfs(board, trie.root, i, j, "", ans)
        }
    }
    return ans
};

function dfs(board, node, i, j, path, res){
    if(node.end){
        res.push(path)
        node.end = false
    }
    
    if(i<0 || i>=board.length || j<0 || j>=board[0].length){
        return
    }
    
    let tmp = board[i][j]
    node = node.links[tmp]
    
    if(!node){
        return
    }
    
    board[i][j] = "#"
    dfs(board, node, i+1, j, path+tmp, res)
    dfs(board, node, i-1, j, path+tmp, res)
    dfs(board, node, i, j+1, path+tmp, res)
    dfs(board, node, i, j-1, path+tmp, res)
    board[i][j] = tmp
}