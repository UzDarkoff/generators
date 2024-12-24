#1.iter
# a=list(range(1,100))
# a_iter=iter(a)
# while True:
#     try:
#         print(next(a_iter))
#     except StopIteration:
#         print("stop")
#         break
#
# s=set(range(10,50))
# s_iter=iter(s)
# print("============")
# while True:
#     try:
#         print(next(s_iter))
#     except StopIteration:
#         print("stop")
#         break

# 2.oop
# class Numbers:
#     def __init__(self,start,stop):
#         self.start=start
#         self.stop=stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start+=1
#         if self.start<self.stop:
#             return self.start
#         raise StopIteration
# for i in Numbers(1,10):
#     print(i)

# class Count:
#     def __init__(self,low,high):
#         self.current=high
#         self.low=low
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.current-=1
#         if self.current>self.low:
#             return self.current
#         raise StopIteration
# for i in Count(20,60):
#     print(i)

# 3.anonim
# generator=(i for i in range(10))
# print(generator)
# my_comp=(num for num in range(20) if num%2==0)
# print(my_comp)

# 4.function
# def mygenerator(a,b):
#     for i in range(a,b):
#         if i%4==0:
#             yield i**2
# for j in mygenerator(10,100):
#     print(j)

# def cube(x):
#     for item in range(x):
#         yield item**3
# for i in cube(6):
#     print(i)
