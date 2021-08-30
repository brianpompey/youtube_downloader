from pip import YouTube

link = input("Enter the link: ")
yt = YouTube(link)



#Title of the video
print("Title: ",yt.title)

#number of views
print("Number of views: ",yt.views)