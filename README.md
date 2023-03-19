Inspiration

We were inspired to create this project because we wanted to help teachers save time and effort when it comes to attendance tracking. We also wanted to ensure that attendance records are accurate, which can have a significant impact on a student’s grade and overall academic success. Finally, we wanted to provide an added layer of safety and security by allowing teachers to easily account for all students in the classroom without having to manually see who is present. We believe that our project has the potential to improve the educational experience for both teachers and students.

What it does

Our product is a web-based attendance monitoring system for teachers that allows them to view their student’s attendance in real-time. Attendance AI is a web application that uses machine learning algorithms to automate the attendance tracking process. The solution uses a facial recognition system to identify students and record their attendance in real time. The application provides teachers with a dashboard where they can monitor the attendance of their students. It also generates attendance reports that can be used for administrative purposes. The system is also easy to use, with a simple and intuitive user interface that requires no technical knowledge to operate. Overall, this product is a useful tool for teachers who want to keep track of their student’s attendance in real-time and make informed decisions about how to address any attendance issues.

How we built it

To build this attendance tracking system, we used a combination of several technologies and tools. Firstly, we used Python as our primary programming language, along with several libraries such as Flask, Pandas, face_recognition, and cv2. Flask is a web framework that allowed us to create the web application, and Pandas was used to extract and manipulate the data from the CSV file containing the student attendance records. We utilized ajax to send the requests from the back-end to the front-end. We also used HTML, CSS, and JavaScript to create the web interface of the application. The HTML provided the structure of the web pages, CSS was used to style the pages, and JavaScript was used to make the web pages more interactive and dynamic. To ensure real-time tracking of attendance, we used a technique called server-sent events (SSE). SSE is a technology that allows the server to send updates to the client as soon as new data is available, without the client having to request it. We implemented SSE using the Flask framework. The Flask application is responsible for retrieving data from a CSV file that contains attendance data and serving it to the front end. The students are being recognized using cv2 and face_recognition. The application also has a route that streams the data in real time, allowing the front end to update the data as it changes. The front end is a web page that uses HTML, CSS, and JavaScript to display the attendance data to the user. The page is responsive and displays the data in a table format that is easy to read. The page also updates automatically every few seconds to display the latest attendance data.

Challenges we ran into

One of the main challenges we faced was implementing a login system that would securely authenticate users and prevent unauthorized access to the dashboard. We had to do extensive research and testing to ensure that our login system was secure.

Another pressing challenge we faced was the internet, it was really slow and it really halted our progress.

Another challenge we faced was implementing real-time updates to the attendance records on the dashboard. We wanted to make sure that the dashboard displayed the most up-to-date attendance data at all times, which required us to use AJAX to constantly update the page with new data from the server. This problem required us to spend around 3 hours on it.

We also faced challenges while working with CSS for the first time. While we had some experience with HTML, CSS was a new technology for us, and we had to spend some time learning how to use it effectively to create a visually appealing and responsive interface for the dashboard.

Accomplishments that we're proud of

We are proud of ourselves for powering through all of our challenges even though at times our morale was really low. One of our teammates was sick but he still did a lot of work even though he was really tired and unwell. We are proud of creating a working prototype of Attendance AI that can accurately track attendance in real time. We were able to create a system that securely stored student and attendance data and made it easily accessible to teachers in real-time. We are also proud of creating a responsive and user-friendly front end that can display attendance data in a clear and organized way.

What we learned

We learned a lot about machine learning, artificial intelligence, and the challenges of developing a facial recognition model. We also learned how to integrate different technologies and frameworks to create a web application. We have become more familiar with javascript and ajax through this hackathon. Another thing we learned was how to work with CSS and we had to research a lot about the formatting. Additionally, we gained valuable experience in developing user interfaces and creating a smooth user experience.

What's next for Attendance AI

In the future, we plan to add more features to Attendance AI, such as integrating it with other educational platforms and developing a mobile application for easier access. We also plan to improve the accuracy of the facial recognition model and explore other machine learning algorithms to enhance the functionality of the solution. We also hope to improve the scalability to support whole schools and organizations.
