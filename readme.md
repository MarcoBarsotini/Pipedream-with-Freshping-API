# How to connect Freshping and Pipedream

I made a simple code to notify you in a telegram chat whenever a server is down. See how to integrate <br> (Attention: This is a quick tutorial)
<br>

### How does it work?
Basically, the program receives a Json file from Freshping, with the offline server information. After that, the Pipedream Webhook is triggered and processes the information to send it on the specified telegram channel.
<br><br>

## Creating a webhook in Freshping

Create an account on the platform https://www.freshworks.com/website-monitoring/ and follow the steps   <br><br>

01- Go to settings, and click create a webhook <br>
![Step 1](./images/01.png)

<br><hr><br>

02- Paste the webhook created in Pipedream into the marked field <br>
![Step 2](./images/02.png)

<br><hr><br>

03- Ok, now your webhook is set up. Go to your Workflow in Pipedream, and paste the code available in the repository <br>
![Step 3](./images/03.png)

<br><hr><br>

Here is an example of how your Workflow should look <br>
![Step 4](./images/04.png)

<br><hr><br>

### Created by Marco Barsotini ;)
