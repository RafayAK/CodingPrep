"""
This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network.
What if we know the files in the two computers are mostly the same?
"""

# apparently this problem is best solved by a data structure used
# in Bitcoin and other decentralized systems: Merekle Tree

# Merkel Tree is a binary tree each leaf node represents the hash of the data
# it represents and each parent node has the collated(combined) hashes of the leaf nodes

# overview of the Merkle Tree Algo:
# 1- If change is made to a file(leaf node), we recalculate the hash of the file and
#    all the nodes up the branch to the root node of the directory
# 2- To see if the two directories need syncing only need to check the root node hash of the directory
# 3- The nodes that hae the same hashes can be ignored from the syncing process as the entire directory structure
#    below them must also be the same

"""
    ABCDEFGH <-- Merkle Root
       /    \
    ABCD     EFGH
    / \      / \
   AB  CD   EF  GH
  / \  / \  / \ / \
  A B  C D  E F G H


         Dir_A                                                 
      (hash_dirA)                                                 
        /     \                                            
 Branch1        Branch2                                        
 (hash_br1)     (hash_br2)                               
   /   \           /    \                                      
file1  file22    file3   file4                                       
(hash1) (hash2)  (hash3) (hash4)


        Dir_B
      (hash_dirB)
        /     \
 Branch1        Branch2
 (hash_br1)     (hash_br2)
   /   \           /    \
file1  file22    file3   file4
(hash1) (hash2)  (hash3) (hash4)


"""


from hashlib import md5

class MerkleNode:
    def __init__(self):
        self.parent = None
        self.node_hash = None
        self.left = None
        self.right = None

    def recalculate_hash(self):
        collated_hash = ""
        if self.left:
            collated_hash += self.left.node_hash
        if self.right:
            collated_hash += self.right.node_hash

        self.node_hash = md5(collated_hash.encode()).hexdigest()
        if self.parent:
            self.parent.recalculate_hash()



class MerkleFile(MerkleNode):
    def __init__(self, filename):
        MerkleNode.__init__(self)
        self.is_dir = False
        self.content = ""
        self.file_name = filename

    def update_content(self, new_content):
        self.content = new_content
        self.calculate_hash()

        if self.parent:  # if parent exists -> in a directory
            self.parent.recalculate_hash() # change/update of data causes the hashes to be updated in the tree

    def calculate_hash(self):
        self.node_hash = md5(self.content.encode()).hexdigest()



class MerkleDirectory:
    def __init__(self):
        self.root = None
        self.is_dir = True
        self.children = []

    def add_file(self, merklefile):
        self.children.append(merklefile)
        self.remake_hash_tree()  # addition of new data causes the tree to be remade
        return self.children[-1]  # return the file after its been added to the directory

    def remake_hash_tree(self):
        self.root = None

        def helper(children):  # helper function to remake tree in case a new file is added
            # try make nodes with two leaves if possible

            if len(children) == 1:
                return children[0]

            mkl_node_list = []
            iter_start = 0
            for iter_end in range(2, len(children)+2, 2):
                mkl_node = MerkleNode()
                nodes = children[iter_start:iter_end]
                if len(nodes) == 2: # got two nodes
                    mkl_node.left = nodes[0]
                    nodes[0].parent = mkl_node
                    mkl_node.right = nodes[1]
                    nodes[1].parent = mkl_node
                    mkl_node.node_hash = md5((nodes[0].node_hash+nodes[1].node_hash).encode()).hexdigest()
                else:
                    # only got one node
                    mkl_node.left = nodes[0]
                    nodes[0].parent = mkl_node
                    mkl_node.node_hash = md5((nodes[0].node_hash).encode()).hexdigest()

                mkl_node_list.append(mkl_node)
                iter_start=iter_end

            return helper(mkl_node_list)

        self.root = helper(self.children)


def get_differing_files(dir_1:MerkleDirectory, dir_2:MerkleDirectory):
    root_1, root_2 = dir_1.root, dir_2.root

    if root_1.node_hash == root_2.node_hash:
        print("Directories on both systems upto date")

    else:
        while(root_1 or root_2):
            temp_root_1 = root_1
            temp_root_2 = root_2

            if root_1 and not root_2:
                print("\"{}\" exists on System_1 but does not exist on System_2".format(root_1.file_name))
                break

            if not root_1 and root_2:
                print("\"{}\" exists on System_2 but does not exist on System_1".format(root_2.file_name))
                break

            # check if the roots point to a file-> left and right empty
            if (root_1.left is None and root_1.right is None) and (root_2.left is None and root_2.right is None):
                print("System_1 \"{}\" has data: {} \nSystem_2 \"{}\" has data: {}".format(root_1.file_name, root_1.content,
                                                                                  root_2.file_name, root_2.content))
                break

            if root_1.left.node_hash != root_2.left.node_hash:
                root_1 = root_1.left
                root_2 = root_2.left

            else:
                root_1 = root_1.right
                root_2 = root_2.right



# System_1
dir_A = MerkleDirectory()
file_a_1 = MerkleFile('file_a')
file_a_1.update_content('a')

file_b_1 = MerkleFile('file_b')
file_b_1.update_content('b')

file_c_1 = MerkleFile('file_c')
file_c_1.update_content('c')

file_a_1 = dir_A.add_file(file_a_1)
file_b_1 = dir_A.add_file(file_b_1)
file_c_1 = dir_A.add_file(file_c_1)


# System_2
dir_B = MerkleDirectory()
file_a_2 = MerkleFile('file_a')
file_a_2.update_content('a')

file_b_2 = MerkleFile('file_b')
file_b_2.update_content('b')

file_c_2 = MerkleFile('file_c')
file_c_2.update_content('c')

file_a_2 = dir_B.add_file(file_a_2)
file_b_2 = dir_B.add_file(file_b_2)
file_c_2 = dir_B.add_file(file_c_2)

# Before changes in files
print("\n--------- Before changes in files ---------\n")
get_differing_files(dir_A, dir_B)
print("\n------------------------------------------\n\n")


file_c_2.update_content("cc") # changes made to file_c

# after changes in files
print("\n--------- After changes in files ---------\n")
get_differing_files(dir_A, dir_B)
print("\n------------------------------------------\n")


file_c_2.update_content("c")  # revert changes
print("\n---- After reverting changes in files ----\n")
get_differing_files(dir_A, dir_B)
print("\n------------------------------------------\n")


# add file in system_2

file_d_2 = MerkleFile('file_d')
file_d_2.update_content('d')

file_d_2 = dir_B.add_file(file_d_2)
print("\n--------- After adding a file ---------\n")
get_differing_files(dir_A, dir_B)
print("\n------------------------------------------\n")