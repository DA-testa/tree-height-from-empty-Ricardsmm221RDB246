###Ricards Meiers-Meiris 1.grupa,221RDB246
import sys
import threading
import numpy


def compute_height(n, parents):
    tree = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            continue
        if parent not in tree:
            tree[parent] = [node]
        else:
            tree[parent].append(node)
    
    
    def height(node):   
        if node not in tree:
            return 1
        heights = [height(child) for child in tree[node]]
        return max(heights) + 1
   
    root = parents.index(-1)
    return height(root)


def main():
    print("Do you want to enter input from keyboard or file? (k/f)")
    source = input().strip().lower()
    while source not in ['k', 'f']:
        print("Invalid input. Please enter 'k' for keyboard input or 'f' for file input.")
        source = input().strip().lower()
        if source == 'k':
            print("Enter the number of nodes:")
        n = int(input())
    
        print("Enter the parents of nodes separated by spaces:")
        parents = list(map(int, input().split()))
    else:
       
        print("Enter the filename:")
        filename = input().strip()
        
        if 'a' in filename:
            print("Invalid filename. Please enter a filename that does not contain the letter 'a'.")
            return
        try: 
            with open(f'folder/{filename}', 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except:
            print("Error reading file. Please check the filename and try again.")
            return
    
    print("Height of the tree:", compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start() 
