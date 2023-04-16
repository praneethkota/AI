#if BFS take pop = 0 
#if DFS take pop = -1
k=int(input("Enter num of node"))
g={}
for i in range(k):
    node=int(input("Enter the vertex-"))
    edge=list(map(int,input().split()))
    g[node]=edge
src=int(input("Enter the source node-"))
goal=int(input("Enter the goal node-"))
visited=[]
queue=[]
def bfs(g,visited,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        if s==goal:
            break
        for i in g[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
bfs(g,visited,src)
