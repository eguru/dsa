


for t in range(int(raw_input())):
     s = raw_input().strip()
     deletion = 0
     for i in range(0, len(s)-1):
         if s[i] == s[i+1]:
             deletion += 1
     print deletion
     
             
        
