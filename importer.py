# def binary_search(a, x):
#     start = 0 
#     end = len(a) - 1
#     while start <= end : 
#         mid = (start + end ) // 2
#         if x == a[mid] : return mid 
#         elif x > a[mid] : start = mid + 1
#         else : end = mid - 1
#     return -1




def binary_search_sub(a, x, start, end): # start, end 를 집어넣는 이유는 재귀함수를 호출하기 위함으로 보인다.
    if start > end : # start 값이 end 값보다 커지면 끝. 같은 경우 까지는 끝나지 않는다. 같은 경우가 끝나는 것은 만약 숫자가 두개 밖에 없고 뒤에 있는 숫자가 찾는 값인 경우 재귀를 한번 돌리면 start랑 end 값이 같게 되고 한번 더 들어가서 mid가 1이 되어 a[mid] 와 x 가 같다 따라서 result 는 1이다. 이런 결과가 나와야 하는데 == 이 되면 그냥 없다고 하고 끝나게 된다. 
        return -1 
    mid = (start + end) // 2 
    if x == a[mid]: return mid
    elif x > a[mid]: return binary_search_sub(a, x, mid+1, end)
    else : return binary_search_sub(a, x, start, mid-1)
    
    # return -1

def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a)-1)


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 81))