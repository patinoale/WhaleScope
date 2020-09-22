# WhaleScope

### Share Your Adventure

WhaleScope is an app where avid whale watchers can share their latest sightings and use other user's sightings to plan for future trips.

# Getting Started

* Fork the repository
* Clone the file
* Install the dependencies
* Enter ```python3 manage.py runserver``` into the terminal to turn on the server
* Open your favorite browser at  ```http://localhost:8000/```
* Enjoy!

# App Inspiration

People who love whales need a place to obtain info about the best places to go whale watching and share their amazing adventures when they get back.

# Design Inspiration

We wanted to share the true mysticism and beauty of these majestic creatures. Where better to show them, then in their natural habitat. We aim to invoke the feeling of swimming with the whales while celebrating their magnificence.
 
# Languages Used
* Python
* JQuery
* Javascript
* Regex
* Html

# Technologies Used
* Django
* PostgreSQL
* Boto3
* Amazon S3
* Google Maps Javascript Api
* Google Geocoding Api
* Google Geolocation Api
* The Whale Museum Api
* Heroku for Deployment

# Resolved Issues
1) The main whale sighting api we wanted to use was an api written primarily with javascript. The go
Regex was needed to connect the two languages. Thank you to our instructor, Daniel Scott, for helping accomplish this goal!!

2) 

# ERD
![ERD](./images/ERD.png)

# Trello Board
![Trello Board](./images/Trello_Board.png)


# Wire Frames

### Landing Screen
![Landing Page](./images/WireFrameLandingPage.jpeg)

### Planned Index Page
![All Sightings](./images/WireFrameIndexPage.jpeg)

### Planned Sighting's Detail Page
![Sightings Detail Page](./images/WireFrameDetailsPage.jpeg)

# Screenshots of Live App
### Landing Page
![Live Landing Page](./images/Landing_Page.png)

# Unresolved issues
On our Trello Board, we initially planned to be able to show users recent whale news as well as allow users to post photos in the comments. 

1) The whale news was going to populated by a webcrawler. We used the Scrapy framework and were able to get the 'spiders' to crawl though several websites and bring back information

### Webcrawler Terminal
![Webcrawler Terminal](./images/WebcrawlerTerminal.png)
### Crawled Response 
![Crawled Response](./images/Crawled_Response.png)

We got stuck trying to pass the information through pipelines and items.py. It would need to pass through these files to be able to create a file django would be able to display. By the time we got this part completed, there was not enough time to finish the process.

We attempted to pivot to a newsfeed, but there were too many other features that still needed to be built to continue with this.

2) As for the photos in the comments, we just ran out of time. Hopefully we will be able to complete this in future versions.

# Future Enhancements

In the future, we would like to build the webcrawler and aggregate news about whales and other underwater mammels in a sidebar.

# Link to Live App
Click here to see [WhaleScope]()

# Authors who worked on Version 1
* Alejandra Patino - [GitHub](https://github.com/patinoale)
* Brian Kelly - [GitHub](https://github.com/brianjkelly)
* Chengusoyane Kargbo - [GitHub](https://github.com/ChenguK)

## Acknowledgments
Thank you to anyone who helped us get the app to this point.