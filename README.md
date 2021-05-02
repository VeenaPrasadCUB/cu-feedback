# CU-FEEDBACK 

## Team 6 : Colorado Buffaloes

## Team Members : Jay Luther , Nischal Paramashivaiah , Pradyoth Srinivasan , Shruthi Sridharan , Veena Prasad

Web application written in Python using `flask` and deployed on Heroku.

# Project Motivation

It is a well-documented fact that to improve at a skill, you need constant feedback. When learning to cook, you have others taste it and be honest. When learning an instrument, you record yourself to see how you sound. The same is true for teaching, although getting consistent feedback is a tall order. 

Under the CU Boulder CS Department's current system for managing Teaching Assistants (TAs), we have students fill out questionaires twice a semester, which helps the department make hiring decisions for subsequent semesters. However, this limited amount of feedback does not greatly help our current TAs improve in their roles as educators. Instead, from a TAs perspective, it gives a glimpse at the issues we face in teaching our students but fails to provide enough feedback to help us learn from our mistakes and experiment with our methodology.

To aid in solving this problem, we are developing a system to help TAs get regular feedback from their students. Using our app, a TA can sign into their educator dashboard and send a brief anonymous survey to their students. The survey should take no longer than one minute to complete, and be in a simple Google form. By doing this, and stressing the ease and minimal amount of time it takes to complete, our experiments have shown that a TA can get a majority response rate at regular intervals throughout the semester. These surveys will contain questions that the TA themselves want the answers to, which allows them to gauge understanding of core materials in their class and get constructive feedback. 

Upon the completion of a survey, the data will be automatically imported into the educator dashboard, which will provide a brief analysis of the results. Using simple questions on students' comprehension of core topics, we can get a quantitative look at how much our students understand. Using Natural Language Processing, we can classify the ratio of positive to negative comments, as well as identify suggestions within these comment blocks that may be of use to the TA. The raw, anonymized data will also be available for the TAs to view.

By seeing these results at regular intervals throughout the semester, our department's TAs can continually grow their skills as educators. With unofficial feedback at regular intervals, we can better gauge how our students respond to TAs lectures, and ensure that students are comfortable with the material taught. If they are not, this will be reflected in the survey results, which will give the TA actionable feedback on what the students simply are not understanding and encourage the TA to experiment with different methods. This process, completed regularly throughout the semester, will likely improve the comprehension of our students, thus improving the quality of our department's undergraduate education.


---

|Website|URL|
|:---|:---:|
|User stories | https://www.pivotaltracker.com/n/projects/2491532 |
|Production software | http://cu-feedback.herokuapp.com/ |

|Topic|Topic|
|:---|:---|
|Project Planning|Pivotal Tracker|
|Language|Python, Javascript, HTML|
|Build Tool|Gradle|
|Testing Tools|Pytest|
|Front-end Framework|Javascript / HTML|
|Back-end Framework|Flask|
|Data Persistence|MySQL|
|Messaging|Apache Kafka|
|Production|Heroku|
|Continuous Integration|Github Actions|
|Monitoring|Heroku|
|Continuous Delivery|Heroku|

### Deployment Process

The web application is written in Python using `flask` and deployed on Heroku.

### Design Decisions 

- Front-end : Javascript and HTML/CSS : Our application a simple front-end web app and does not require any complex frameworks. 
- Back-end : Python / Flask : Python is a comfortable language for all team members.
- Database : MySQL : We are importing the data from a .csv file into Python, requiring no complex objects. As we are using Python on the back-end, MySQL is simple enough to suit our needs.
- Database : ElasticSearch : Visualization dashboard was easy to build with ElasticSearch-Kibana.
- Deployment : Heroku : Having used it during Homework 4, it seemed a logical continuation to leverage our new knowledge with Heroku for our application.

### Communication

We use a combination of Pivotal Tracker, Whatsapp, and Zoom. 

- Pivotal Tracker: We use Pivotal Tracker to stay up to date on the current progress of all team members.
- Whatsapp: This allows us to ask questions on the fly, whenever we run into issues or would like a quick word with our teammates.
- Zoom: We hold weekly meetings to plan the current sprint and ensure that everything is running smoothly.

### Work Distribution

During our weekly Zoom meeting, we spend time on Pivotal Tracker assigning stories to individuals. This allows our schedules to be a bit flexible, while also encouraging us to take different roles in different sprints. Our Pivotal Tracker can be found [here](https://www.pivotaltracker.com/n/projects/2491532).

### Iteration Planning

Iteration Planning can be found in the following link :
[https://github.com/jay-ml/cu-feedback/wiki/Iteration-Planning](https://github.com/jay-ml/cu-feedback/wiki/Iteration-Planning)

### Final Project Presentation
Project Presentation slides can be found [here](https://github.com/jay-ml/cu-feedback/blob/master/FOS%20Presentation%20-%20Team%20Colorado%20Buffaloes%20-%20Final.pptx)

### Demo of our project
You can find our project demo [here](https://github.com/jay-ml/cu-feedback/blob/master/Demo%20of%20our%20project.mp4)
