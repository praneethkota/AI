def find(m,d):
    keys=[k for k,v in d.items() if v==m]
    return keys[0]
k=int(input("Enter num of node"))
g={}
h={}
for i in range(k):
    node=int(input("Enter the vertex-"))
    edge=list(map(int,input().split()))
    g[node]=edge
for i in range(k):
    vertex=int(input("Enter the vertex-"))
    dis=int(input())
    h[vertex]=dis
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
        m=99999
        for i in g[s]:
            if i not in visited:
                queue.append(i)
                if h[i]<m:
                    m=h[i]
        queue.append(find(m,h))
bfs(g,visited,src)
