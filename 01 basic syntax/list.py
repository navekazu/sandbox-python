list = ["My", "name", "is", "John."]
print("list:", end=" ")
print(list)

# インデックスは0オリジン
print("list[0]:", end=" ")
print(list[0])

print("list[1]:", end=" ")
print(list[1])

print("list[2]:", end=" ")
print(list[2])

# マイナスのインデックスは後ろからアクセス
print("list[-1]:", end=" ")
print(list[-1])

# :を使ってスライスが出来る
print("list[1:]:", end=" ")
print( list[1:])

print("list[1:2]:", end=" ")
print( list[1:2])

print("list[:2]:", end=" ")
print( list[:2])

print("list[:]:", end=" ")
print( list[:])

# ,を使って部分抜き出しが出来る
print("list[1, 3]:", end=" ")
print( list[1, 3])

