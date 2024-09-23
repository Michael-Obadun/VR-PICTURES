Full stack Project

Project purpose & idea
To create a website that allows VR user to upload there images to to one central website. Here the user will be able to :
post/upload thier images, 
view other users images
comment on other users images
like other users images
Rate other users images
Arrange meet ups in VR social spaces

Brainstorm - MVP features & MVP Scope (MoSCoW Prioritisation)
Priority
Allows user to register and sign in to the website. 
Also users to upload there VR post/images.
Allows users to title there post/images.. 
Allows users to place captions with there post/images.
Allows users to commennt on other users post/images.
Allows users to delete there post/images.
Allows users to arrange meet up times (specifi crud)
Not a priorty
Allows user to save drafts of thier post/images.
Allows user to like other users post/images.
Allows users to rate other users post/images.

User Stories - GitHub Projects Board
Manage posts: 
As Admin i can create, read, update and delete any users post  so i can control/monitor the type of post/images
Acceptance Criteria 1 : Admin can create any blog post
Acceptance Criteria 2 : Admin can read any  blog post
Acceptance Criteria 3  : Admin can update any  blog post
Acceptance Criteria 4 : Admin can delete any blog post
Open/Click on a Image: 
As a Site User I can click on a post/Image and see a much bigger view of the image as well as  other associated data relating to the specific image that has been clicked. 
Acceptance Criteria 1 : When a Image is clicked on a detailed view of the post is seen.
Account registration: 
As a Site User I can register an account so that I can comment on a post/image.
Acceptance Criteria 1 : User can Give an email and password to register an account.
Acceptance Criteria 2 : User can then  loggin to their account
Acceptance Criteria 3  : User can then comment on a post/image
Comment on a Image: 
As a Site User I can view all the comments left for a particular post/image
Acceptance Criteria 1 : User can view all comments made on a particular post/image
Acceptance Criteria 2 : User can reply to a comment
Acceptance Criteria 3  : When post/image is clicked all comments associated with the post/image will also be displayed
Like a Image: 
As a Site User I can leave a like and also rate the post/image so that i can easilygather and access them
Acceptance Criteria 1 : User can like a image
Acceptance Criteria 2 : User can rate a image
Acceptance Criteria 3  : User can click a button that shows all thier liked and rated post/Images
Modify or delete comment they have made: 
As a Site User I can modify or delete only comments or post/images they have made. 
Acceptance Criteria 1 : User can modify their comment
Acceptance Criteria 2 : User can delete their comment
Modify or delete meet ups they have made: 
As a Site User I can create, modify or delete and update meet ups they have made. 
Acceptance Criteria 1 : User can create any blog post
Acceptance Criteria 2 : User  can read any  blog post
Acceptance Criteria 3  : User  can update any  blog post
Acceptance Criteria 4 : User  can delete any blog post
Visitor Experiance (Non Site User)
As a Site Visitor I can see a list of all user post/images so i van decide on wether i should register with the site or not.
Acceptance Criteria 1 : Visitor can ONLY see all post made by Admin and Site users

-----------------------------------------------------------------------------------------------------
Data Model
 
class Post(models.Model):
title = models.CharField(max_length=200, unique=True)
slug = models.SlugField(max_length=100, unique=True)
author = models.ForeignKey()
image = models.ImageField(default='fallback.png', blank=False)
caption = models.TextField()
likes = models.ManyToManyField(User, related_name='___', blank=True)
ratings = models.ManyToManyField(User, related_name='___', blank=True)
created_on = models.DateTimeField(auto_now_add=True)
updated_on = models.DateTimeField(auto_now=True)
class Comment(models.Model):
username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
 message = models.TextField() = models.TextField()
created_on = models.DateTimeField(auto_now_add=True)
class Meets(models.Model):
Author = = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host")
Platform = models.CharField(max_length=200, unique=True)
Discription = models.TextField()
Venue = models.CharField(max_length=200, unique=True)
date = models.DateTimeField()

User Flow Diagram

Wireframes
Main/Home Page - Visitors to the site can see all posts/images made here as well as buttons to fire of register and sign in page. (colour schem to be disregarded)
Register/Signin Page - (2 views) register and sign in view
Detail Page - will show a detailed view of the post/image as well as other ascoited data and all comments about the post/image. 
User Page - will dive the user the option to upload post/images and view multiple list from this page

Design
I will create a generic template That i will design taking inspiration from many websites i have viewed over the years.
The colour pallet for the website will be chosen from https://colorhunt.co/
These are the colours i will be using as there is good 
contrast between the colours, most of the colours 
our light which will allow images and texts to pop 
out the screen more
 
I will use the fonts [ ] and [ ] as they are easily legable on screens and is usually seen as a font that is SLIGHTY playfull and fun. I will also have a novelty font [ ] which will be used sparing if not only once or twice. I will use 2 primary font colours black and white and two optional conditional colours green for success notifications and red for error notifications.

Assets

credits
























