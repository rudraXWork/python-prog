def check_for_word(word):
    with open("sample.txt","r") as f:
        data = f.read()
        if (data.find(word)!=-1):
            print("found")
        else:
            print("not found")    
check_for_word("rudra")

def check_for_line(word):
    line_no=1
    data = True 
    with open("sample.txt","r") as f :
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
            line_no+= 1
check_for_line("word")     

#def check_for_line(word):
    #with open("sample.txt", "r") as f:
        #for line_no, line in enumerate(f):
            #if word in line:
               # print(line_no + 1) #