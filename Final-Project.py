#!/usr/bin/env python
# coding: utf-8

# In[20]:


class BinaryIndexedTree:    
    def __init__(self, n, m):        
        self.ft = [[0 for i in range(n + 1)] 
        for j in range(m + 1)]        
        self.n = n        
        self.m = m 
        
    def LSB(self, x):        
        return x & (-x) 
    
    def update(self, x, y, val):        
        while x <= self.m:            
            y1 = y            
            while y1 <= self.n:                
                self.ft[x][y1] += val                
                y1 += self.LSB(y1)            
            x += self.LSB(x)  
            
    def prefix_sum(self, y, x):        
        s = 0        
        x1 = x        
        while x1 > 0:            
            y1 = y            
            while y1 > 0:                
                s += self.ft[x1][y1]                
                y1 -= self.LSB(y1)            
            x1 -= self.LSB(x1)        
        return s    
    def Prefix_Sum(self, x1, y1, x2, y2):        
        return (self.summation(x2, y2) - self.summation(x1 - 1, y2) - self.summation(x2, y1 - 1) + self.summation(x1 - 1, y1 - 1))    
    def Construct(self, matrix):        
        self.n = len(matrix)        
        self.m = len(matrix[0])        
        for i in range(self.m):            
            for j in range(self.n):                
                self.update(i + 1, j + 1, matrix[i][j])  
                
    def Print(self):        
        matrix = [[1, 2, 3, 4],                 
                  [5, 3, 8, 1],                  
                  [4, 6, 7, 5],                  
                  [2, 4, 8, 9]]        
        self.Construct(matrix)        
        for i in range(len(matrix)-1):            
            for j in range(len(matrix[0])-1):                
                print(matrix[i][j])            
            print("\n")


# In[21]:


b1 = BinaryIndexedTree(4,3)


# In[22]:


b1.prefix_sum(2,1)


# In[23]:


b1.Construct([[1,3],[2,4]])


# In[24]:


b1.Print()


# In[ ]:




