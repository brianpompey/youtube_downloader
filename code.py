from pip import YouTube

link = input("Enter the link: ")
yt = YouTube(link)



#Title of the video
print("Title: ",yt.title)