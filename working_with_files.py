poem_path = r"C:\Users\LENOVO\Desktop\test test\python_mid\python-poem.txt"

rf = open(poem_path) # open method open files in --> bydefault read mode
"""print(f"Before reading, cursor --> {rf.tell()}")
print(rf.read())
print(f"After reading, cursor position --> {rf.tell()}")
print("------------------------------------------------")
rf.seek(0)
print(rf.read())"""

"""print(f"next line --> {rf.readline()}",end="")
print(f"next line --> {rf.readline()}",end="")
print(f"next line --> {rf.readline()}",end="")
print(f"next line --> {rf.readline()}",end="")"""

"""all_lines = rf.readlines()
for line in all_lines:
    print(f"The line is --> {line}",end="")
print(all_lines)"""
rf.close()



with open(poem_path) as rf: #default read mode --> "r"
    print(rf.read())


# Three types of writing data in file {w,a,r+} mode

# 1) Write mode
# Deletes all prev data and writes new data
with open("kritika.txt","w") as wf:
    wf.write("Hi stupid")


# 1) Append mode
# Doesn't delete all prev data and writes new data
with open("samay.txt","a") as af:
    af.write("Samay is cute")

# 1) R plus mode
# Read and write new data
with open("file.txt","r+") as rpf:
    rpf.write("Write r+ mode")


with open("file.txt","r+") as rpf:
    rpf.seek(len(rpf.read()))
    rpf.write("last ma lekh gadha")
    rpf.write("write r+ mode")

# 4) read and write
with open(poem_path,"r") as rf:
    with open("samay.txt","w") as wf:
        wf.write(rf.read())

# 5) read love story
with open("love_story.txt","r",encoding="utf-8") as rf:
    print(rf.encoding)
    print(rf.read())


with open("samay.txt","r") as rf:
    with open("samay.txt","w") as wf:
        for line in rf.readline():
            samay_part1, samay_part2 = line.split(",")
            wf.write(f"{samay_part1}'s salary is {samay_part2}")
