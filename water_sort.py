from collections import deque
from image_process import colour_array


def top(arr):
    for i in range(len(arr)):
        if arr[i]!="":
            return i
    return 4
# new color can be added at top'th position or in array[top-1]
# the topmost color is at array[top]
# if top=4, then array is empty

def colours_moveable(arr):
    k=top(arr)
    if k==3:
        return 3,4
    if k==4:
        return 4,4
    for j in range(k+1,len(arr)):
        if arr[j]==arr[k]:
            continue
        else:
            return k,j
    return k,4
# I can move j-k colors from kth position to jth(excluding) position
# Colors from arr[k] to arr[j] (excluding) are same

def move_possible(arr1,arr2):
    
    k=top(arr2)
    x=top(arr1)
    if k==0:
        return False
    elif k==4:
        return True
    elif x==4:
        return False
    elif arr1[x]==arr2[k]:
        return True
    else:
        return False


def MoveGen(state):
    neighbors=[]
    for i in range(len(state)):
        for j in range(len(state)):
            if i!=j:
                if move_possible(state[i],state[j]):
                    a,b=colours_moveable(state[i])
                    if a==0 and b==4:
                        continue
                    else:
                        c=top(state[j])
                        arr1=state[i].copy()
                        arr2=state[j].copy()
                        new_state=state.copy()
                        for k in range(c):
                            if k<b-a:
                                arr2[c-k-1]=arr1[a+k]
                                arr1[a+k]=""
                        new_state[i]=arr1
                        new_state[j]=arr2
                        neighbors.append(new_state)
    return neighbors

def goal_test(state):
    for arr in state:
        k=arr[0]
        for i in range(1,len(arr)):
            if arr[i]!=k:
                return False
    return True

def f_h(state):
    if goal_test(state):
        return 100
    else:
        return 0
    
def pairs(state):
    val=0
    for arr in state:
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                val+=2
            else:
                val-=1
    return val

def kids(state):
    neighbors=MoveGen(state)
    val=2*len(neighbors)
    for neighbor in neighbors:
        val+=pairs(neighbor)+f_h(neighbor)
    return val
    
def heuristic(state):
    return -(f_h(state)+pairs(state)+kids(state))

def best_first_search(initial_state):
    start_tuple = tuple(tuple(x) for x in initial_state)
    priority_queue = deque([{start_tuple: [None,0]}])
    visited = {}
    path=[]
    while priority_queue:
        current_state = priority_queue[0]
        del priority_queue[0]
        for state, arr in current_state.items():
            state_list = [list(x) for x in state]
            if goal_test(state_list):
                parent=arr[0]
                while state:
                    state_list = [list(x) for x in state]
                    path.append(state_list)
                    if parent:
                        state = parent 
                        parent = visited[state][0]
                    else:
                        break
                path.reverse()
                return path
            if state not in visited.keys():
                    visited[state] = arr
                    for neighbor in MoveGen(state_list):
                        neighbor_tuple = tuple(tuple(x) for x in neighbor)
                        if neighbor_tuple!=arr[0]:
                            if neighbor_tuple not in visited.keys():
                                h_val=heuristic(neighbor)
                                priority_queue.append({neighbor_tuple: [state,h_val]})
        priority_queue=sorted(priority_queue,key=lambda x: list(x.values())[0][1])
    return None  # No valid solution found

def moves(path):
    for i in range(len(path)-1):
        arr0=path[i]
        arr1=path[i+1]
        move=[]
        for j in range(len(arr0)):
            if arr0[j]!=arr1[j]:
                move.append(j)
            if len(move)==2:
                break
        a=top(arr0[move[0]])
        b=top(arr1[move[0]])
        if a<b:
            print(f"move tube {move[0]+1} to tube {move[1]+1}")
        elif b<a:
            print(f"move tube {move[1]+1} to tube {move[0]+1}")


# image_path="Test_Cases/test_625.PNG"
# image_path="Test_Cases/test_627.jpeg"
image_path="Test_Cases/test_630.jpeg"
# image_path="Test_Cases/test_631.jpeg"
# image_path="Test_Cases/test_633.jpeg"
# image_path="Test_Cases/test_634.jpeg"
# image_path="Test_Cases/test_637.jpeg"
# image_path="Test_Cases/test_648.jpeg"
# image_path="Test_Cases/test_649.jpeg"
            
empty_tubes=2

# image_path=str(input("Enter the path of the image: "))
# empty_tubes=int(input("Enter the number of empty tubes: "))

initial_state=colour_array(image_path,empty_tubes)
path=best_first_search(initial_state)
moves(path)