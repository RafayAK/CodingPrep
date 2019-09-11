"""
This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network.
What if we know the files in the two computers are mostly the same?
"""

# apparently this problem is best solved by a data structure used
# in Bitcoin and other decentralized systems: Merekel Tree

# Merkel Tree is a binary tree each leaf node represents the hash of the data
# it represents and each parent node has the collated(combined) hashes of the leaf nodes

# overview of the Merkel Tree Algo:
# 1- If change is made to a file(leaf node), we recalculate the hash of the file and
#    all the nodes up the branch to the root node of the directory
# 2- To see if the two directories need syncing only need to check the root node hash of the directory
# 3- The nodes that hae the same hashes can be ignored from the syncing process as the entire directory stucture
#    below them must also be the same

"""
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


class MerkleDirectory(MerkleNode):
    def __init__(self):
        MerkleNode.__init__(self)
        self.is_dir = True
        self.children = []  # list of files

    def recalculate_hash(self):
        if self.children:
            coalated_hash = ""
            for child in self.children:
                coalated_hash += child.hash

            self.node_hash = md5(coalated_hash.encode()).hexdigest()


class MerkleFile(MerkleNode):
    def __init__(self, filename):
        MerkleNode.__init__(self)
        self.is_dir = False
        self.file_name = filename
        self.content = ""  # in case the node is leaf it will have some content

    def set_content(self, new_content):
        self.content = new_content
        self.caculate_hash()
        if self.parent:
            self.parent.recalculate_hash()

    def caculate_hash(self):
        self.hash = md5(self.content.encode()).hexdigest()

    def add_to_directory(self, dir_node:MerkleDirectory):
        self.parent = dir_node
        dir_node.children.append(self)

        while dir_node:
            dir_node.recalculate_hash()
            dir_node = dir_node.parent  # move to parent directory of the current directory



def get_files_that_are_different(root_1, root_2, files_changed_system_1, files_changed_system_2):

    if not root_1 and not root_2:
        return files_changed_system_1, files_changed_system_2

    if not root_1 or not root_2:
        files_changed_system_1.append(root_2)
        files_changed_system_2.append(root_1)

        return files_changed_system_1, files_changed_system_2

    if root_1.node_hash != root_2.node_hash:
        files_changed_system_1.append(root_2)
        files_changed_system_2.append(root_1)

        root_1_children = root_1.children
        root_2_children = root_2.children

        len_diff = abs(len(root_1_children) - len(root_2_children))

        if len(root_1_children) > len(root_2_children):
            root_2_children = root_2_children + [None for i in range(len_diff)]
        elif len(root_2_children) > len(root_1_children):
            root_1_children = root_2_children + [None for i in range(len_diff)]

        for child_1, child_2 in zip(root_1_children, root_2_children):
            get_files_that_are_different(child_1, child_2, files_changed_system_1, files_changed_system_2)

    return files_changed_system_1, files_changed_system_2

a_1 = MerkleFile("FileA")
b_1 = MerkleDirectory()
a_1.set_content("abc")
a_1.add_to_directory(b_1)
a_1.set_content("abcd")

a_2 = MerkleFile("FileA")
b_2 = MerkleDirectory()
a_2.set_content("abc")
a_2.add_to_directory(b_2)

# Now to know the files that have changed, we can just compare the two trees
# and effectively know which files have changed and need syncing.

file_changes_for_system_1, file_changes_for_system_2 = get_files_that_are_different(
    b_1, b_2, [], []
)

