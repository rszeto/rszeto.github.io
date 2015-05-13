---
layout: default
---

![Ryan Szeto](http://placehold.it/300x300)

# About me
I am an incoming Computer Science and Engineering Ph.D. student at University of Michigan Ann Arbor, where I plan to work with Jia Deng in the area of Computer Vision. I graduated (most likely) summa cum laude from University of Massachusetts Amherst in 2015, where I received a B.S. degree in Computer Science. During my junior year, I was inducted into the UMass Amherst chapter of Phi Beta Kappa.

The majority of my research at UMass was as a member of the RIPPLES lab, which specializes in new software systems for capturing and presenting lectures. I worked on various aspects of the Presentations Automatically Organized from Lectures (PAOL) system, including video conversion, whiteboard processing, multithreading, and the graphical user interface. During the 2012 spring and fall semesters, I worked with the Center for e-Design under the instruction of Jack Wileden and Sundar Krishnamurty, where I primarily worked on program that converted models between Computer-Aided Design (CAD) systems.

I was also a member of UMass' Commonwealth Honors College (CHC), where I (most likely) graduated as a Commonwealth Honors College Scholar with greatest distinction. As part of CHC's Departmental Honors track, I completed an Honors Thesis on detecting marker strokes from whiteboard images efficiently.

From the UMass School of Computer Science (now known as the College of Information and Computer Sciences), I received the Outstanding Achievement in Artificial Intelligence Award, which is given to a top student who has excelled in both academic and research-oriented endeavors in AI. I also received the Cisco Award for Outstanding Achievement and course commendations in many classes.

# Awards
* Outstanding Achievement in Artificial Intelligence Award 
* Honors Dean's Award
* Honors Research Grant
* Research Assistant Fellowship
* Cisco Award for Outstanding Achievement
* Course Commendations in CMPSCI 220, 240, 250, and 585 (UMass)

# Extracurricular interests
In my spare time, I like singing, swimming, and playing Ultimate Frisbee!

# News

{% for post in site.categories.news %}
  * [{{ post.date | date: "%B %e, %Y" }}: {{ post.news-line }}]({{ post.url }})
{% endfor %}