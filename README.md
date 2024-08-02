<h1> User-authentication project </h1>

<h3> AIM:<br></h3>
<p>This projects aims is to create a new and more secure way of authentication. Keystrokes pattern is used to identify if it is the owner or not.</p>

<h3>DESCRIPTION:<br></h3>
<p>Keystrokes pattern differs for every person. The typing speed, keystrokes pattern and number of backspaces used together has alomst 0 chances to match with another person. This type of authentication can be a lot more
secure than the present type of authentication method. </p>
<p>For this project we are collecting real time time data to make the model personalized. For now I'm training it with my data and will be using other subjects data to record the non_ownwer data.</p>

**Data:**<br>
The data collection file has the code that records all the required fields for this project. It will add the columns event, key,time, duration, backspace_used to the deginated csv file. So each key press and release
will be recorded into the csv file. This helps in collecting the real time data to test out the model even better. The model will be trained with both owner and non_owner dataset to tell the difference. This will help
the model to differentiate making it more accurate. Aiming to collect more cleaner and accurate data. The data collection is still in progress.

**Model:**<br>
For the data we have collected the best suited will be the neural networks. This will train the model to create a pattern in data to classify the user as owner or non_owner. Stil trying out more options for the best
result, but so far this model looks suitable.

<h3>CONCLUSION:<br></h3>
The idea of the project is to bring a new type of authentication to increase security. This type of keystroke authentication will be nearly impossible to immitate as the typing style of almost everyone is different.

