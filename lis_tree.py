class TreeNode:
    """Class untuk merepresentasikan node dalam tree"""
    def __init__(self, value=None):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        """Menambahkan child node"""
        self.children.append(child_node)
    
    def __repr__(self):
        return f"Node({self.value})"


class LISTree:
    """Class untuk membangun dan menganalisis LIS Tree"""
    
    def __init__(self, sequence):
        self.sequence = sequence
        self.root = TreeNode(None)  # Root tanpa nilai
        self.all_paths = []
        
    def build_tree(self):
        """Membangun tree structure"""
        print("=" * 80)
        print("PROSES PEMBANGUNAN TREE")
        print("=" * 80)
        
        # Level 1: Semua elemen sequence sebagai direct children dari root
        for i, num in enumerate(self.sequence):
            node = TreeNode(num)
            self.root.add_child(node)
            self._build_subtree(node, i)
            print(f"✓ Membangun subtree untuk node {num}")
        
        print(f"\n✓ Tree berhasil dibangun dengan {len(self.sequence)} node di level 1\n")
    
    def _build_subtree(self, parent_node, parent_index):
        """Membangun subtree secara rekursif"""
        parent_value = parent_node.value
        
        # Cari semua elemen setelah parent yang lebih besar
        for i in range(parent_index + 1, len(self.sequence)):
            if self.sequence[i] > parent_value:
                child_node = TreeNode(self.sequence[i])
                parent_node.add_child(child_node)
                # Rekursif build subtree untuk child
                self._build_subtree(child_node, i)
    
    def find_all_paths(self):
        """Mencari semua path dari root ke leaf"""
        print("=" * 80)
        print("PROSES PENCARIAN SEMUA PATH")
        print("=" * 80)
        
        self.all_paths = []
        
        for child in self.root.children:
            self._dfs_paths(child, [])
        
        print(f"✓ Ditemukan {len(self.all_paths)} path dari root ke leaf\n")
        return self.all_paths
    
    def _dfs_paths(self, node, current_path):
        """DFS untuk mencari semua path"""
        # Tambahkan node saat ini ke path
        new_path = current_path + [node.value]
        
        # Jika leaf node, simpan path
        if not node.children:
            self.all_paths.append(new_path)
        else:
            # Rekursif untuk semua children
            for child in node.children:
                self._dfs_paths(child, new_path)
    
    def find_lis(self):
        """Mencari Longest Increasing Subsequence"""
        print("=" * 80)
        print("PROSES PENCARIAN LIS")
        print("=" * 80)
        
        if not self.all_paths:
            self.find_all_paths()
        
        # Cari path terpanjang
        lis = max(self.all_paths, key=len)
        lis_length = len(lis)
        
        print(f"✓ Panjang maksimum subsequence: {lis_length}")
        print(f"✓ LIS ditemukan: {lis}\n")
        
        return lis, lis_length
    
    def display_tree_structure(self, node=None, prefix="", is_last=True):
        """Menampilkan struktur tree dalam format visual"""
        if node is None:
            node = self.root
            print("\n" + "=" * 80)
            print("VISUALISASI STRUKTUR TREE")
            print("=" * 80)
            print("ROOT")
        
        # Display children
        children = node.children
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            
            # Print connector
            connector = "└── " if is_last_child else "├── "
            print(f"{prefix}{connector}{child.value}")
            
            # Recursive call for subtree
            extension = "    " if is_last_child else "│   "
            self.display_tree_structure(child, prefix + extension, is_last_child)
    
    def display_statistics(self):
        """Menampilkan statistik tree"""
        print("\n" + "=" * 80)
        print("STATISTIK TREE")
        print("=" * 80)
        
        total_nodes = self._count_nodes(self.root)
        total_paths = len(self.all_paths)
        max_depth = max(len(path) for path in self.all_paths) if self.all_paths else 0
        
        print(f"Total nodes dalam tree    : {total_nodes}")
        print(f"Total paths (root to leaf): {total_paths}")
        print(f"Kedalaman maksimum tree   : {max_depth}")
        print(f"Jumlah elemen input       : {len(self.sequence)}")
    
    def _count_nodes(self, node):
        """Menghitung total nodes dalam tree"""
        if not node.children:
            return 1
        return 1 + sum(self._count_nodes(child) for child in node.children)


def main():
    """Fungsi utama program"""
    
    print("\n" + "=" * 80)
    print(" " * 15 + "PROGRAM LONGEST INCREASING SUBSEQUENCE")
    print(" " * 20 + "MENGGUNAKAN STRUKTUR TREE")
    print("=" * 80)
    
    # INPUT
    sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
    
    print("\nINPUT:")
    print("-" * 80)
    print(f"Urutan bilangan: {sequence}")
    print(f"Jumlah elemen  : {len(sequence)}")
    
    # PROSES
    print("\n" + "=" * 80)
    print("MEMULAI PEMROSESAN...")
    print("=" * 80 + "\n")
    
    # Inisialisasi dan build tree
    lis_tree = LISTree(sequence)
    lis_tree.build_tree()
    
    # Tampilkan struktur tree
    lis_tree.display_tree_structure()
    
    # Cari semua path
    all_paths = lis_tree.find_all_paths()
    
    # Tampilkan beberapa path sebagai contoh
    print("=" * 80)
    print("CONTOH PATH YANG DITEMUKAN (10 pertama)")
    print("=" * 80)
    for i, path in enumerate(all_paths[:10], 1):
        print(f"{i:2d}. {path} (panjang: {len(path)})")
    
    if len(all_paths) > 10:
        print(f"... dan {len(all_paths) - 10} path lainnya")
    
    # Cari LIS
    lis, lis_length = lis_tree.find_lis()
    
    # Tampilkan statistik
    lis_tree.display_statistics()
    
    # OUTPUT AKHIR
    print("\n" + "=" * 80)
    print("HASIL AKHIR PROGRAM")
    print("=" * 80)
    print(f"\nUrutan input           : {sequence}")
    print(f"Longest Increasing     : {lis}")
    print(f"Subsequence (LIS)        ")
    print(f"Panjang LIS            : {lis_length}")
    print(f"\nVerifikasi increasing  : ", end="")
    
    # Verifikasi bahwa hasil adalah increasing
    is_increasing = all(lis[i] < lis[i+1] for i in range(len(lis)-1))
    print("✓ VALID" if is_increasing else "✗ TIDAK VALID")
    
    print("\n" + "=" * 80)
    print("PROGRAM SELESAI")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()