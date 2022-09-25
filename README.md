# SWMiniProject-EC463-TwitterRestAPI
Developed by Abhinoor Singh and Chris Gough

## Functionality
The Tweetometer returns information about a Twitter user given their username. Specifically, the app produces three outputs:
1. A metric indicating the likelihood that the user is a bot
2. A metric indicating the overall sentiment (positive/negative) of the users' tweets
3. A list of that user's most frequently discussed topics

In the event that the application user enters an invalid username, an error message is displayed indicating that this is the case. Occasionally, the sentiment analysis is unable to return a list of topics covered frequently by the user. In this case, a message displays to explain to the user that the Google API was not able to provide us with information regarding the content of the user's tweets.

## Design
### Back-end
The app was built in two stages: front-end and back-end. We focused initially on the back-end, as that represented the core product we hoped to deliver. There were several key decisions:
* How will we retrieve and access data?
* What service will host our internal API?
* What information will be returned to the front-end?

We went with the classic approach of building an internal REST API, which made requests to the Twitter, Google, and Botometer APIs, and saved the responses in a JSON format. To gain access to this data, the front-end makes a POST request to the internal API, which takes the Twitter username, combines it with credentials already saved to the internal API, and returns the JSON object containing the relevant information to be displayed on the website. This strategy allows for a clean, simplified back-end, with a singular, clear connection between the front-end and the back-end. Since the internal API handles authentication, no information is needed in the POST request save the Twitter username the application user wishes to analyze.

The REST Api is written in python and uses Flask to host the backend. The API pulls the last 50 tweets from the user's timeline and then parses out all the twitter links, retweets, and replies so only the user's uploaded tweets are analyzed. These tweets are then sent individually to Google's NLP Api, and analyzed. The scores are aggregated, and an average sentiment score is returned. For the categories, the tweets are combined into a paragraph and sent to the Google NLP Api for categorization which then returns all the respective categories that the API is able to parse through. Lastly, the botometer API is called with the user's twiter handle and a bot score is also returned.

For hosting the API, we used Heroku, as it was by far the easiest option available to us and we didn't require a tremendous amount of resources. The request response time is always under 30 seconds, so we knew we wouldn't run into limitations with respect to the amount of data we were able to return. 

To determine what information we needed to return to the front-end, we had to think from the user's perspective. There were three key deliverables, so although the APIs were capable of providing us far more analysis than what we needed, we chose to focus solely on the requirements provided to us by the assignment statement. An application user needs to know if the Twitter user is a bot; whether their tweets are positive or negative; and what topics they cover; so we returned a single score for the first two metrics along with a list of topics. Parsing such an object is simple, and we only have the information we need, rather than diluting it amongst a variety of other, less important features or analyses.
### Front-end
The front-end design was much simpler, as there were fewer design decisions that had to be made. All we really needed was a way to display the analysis in a way that was easy to understand and a web server to host the front-end. Hosting was made simple with Firebase, and we wanted to try a different hosting service, so the decision was fairly easy. Designing the front-end was done initially using Figma, and after deciding on the format in which data would be displayed, all that was left was to implement the design using React.

## SDLC
We followed the Agile framework, tracking our progress on Trello and meeting once a week to discuss relevant design decisions. Although we did not have an official daily scrum, we checked in with each other every couple of days to ensure that progress was being made and there were no roadblocks to completion, as well as to double-check our own design decisions. See the below images, which demonstrate our use of the Trello board:

![image](https://user-images.githubusercontent.com/57511176/192169428-1249e46a-cd62-4ec6-8b03-b417cce0933c.png)

![image](https://user-images.githubusercontent.com/57511176/192169378-712b9a30-5565-4135-ad83-957fa972201b.png)


## Usage

Rest API Endpoint: https://ec463tweetometer.herokuapp.com/tweetometer
React Web App Link: https://sw-mini-project-ec463-362503.web.app/

Note: 
1) The web app is optimized for laptop/desktop use, not for mobile.
2) If the categories do not appear, then the Google NLP did not return anything.
3) If a twitter user has few/no tweets, the API will throw an error msg.
4) Example use cases could be @mkbhd @elonmusk @barackobama @espn etc
