from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)



#Title of the video
print("Title: ",yt.title)

#number of views
print("Number of views: ",yt.views)

#length of video
print("Length of video: ",yt.length,"seconds")

#video description
print("Description: ",yt.description)

#rating
print("Ratings: ",yt.rating)

#print streams
print(yt.streams.filter(progressive=True))
ys = yt.streams.get_highest_resolution()