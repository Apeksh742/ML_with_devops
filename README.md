# ML_with_devops

Requirements: Docker, Linux OS (Redhat, CentOS) , Jenkins and some jenkins plugins - like Github, Build Pipeline, Downstream ext.

# Steps 

1. Clone this repository and get into Dockerfile Directory and run following command with your syntax to create the image with all necessary ML libraries
      docker build -t <name>:<tag> <location of docker file>
 
2. Open jenkins and using systemctl start jenkins and it is available on port 8080 by deafult

3. Enter following commands and do setup as discussed in this article 
         https://medium.com/@apekshagarwal.742/integration-of-ml-with-devops-2e47bc6e2fd7
 
4. Then  you just need to start/run Job 1 and all other jobs are already chained so you don't have to do anything.

# Overview of Jobs:

# JOB 1: 
  It will download the code and copy into your workspace
  
# JOB 2:
  It will launch the environment in docker container with the workspace we have downloaded
  
# JOB 3:
  It will train the model in the container created above.
  
# JOB 4:
  It will send a mail to developer if JOB 3 fails. I have used python script for sending mail via SMTP server
  
# JOB 5:
  It will improve the accuracy of the model until 95% in order to get better predictions from the model
  
# JOB 6:
  It will send email to developer if JOB 5 fails.
  
# JOB 7:
  It will send a success mail to developer if all the desired accuracy is achieved in the model
  
# JOB 8:
  It will monitor the environment in which ml model is running and perform the necessary actions according to the current status of    environment.
  
# Article link: https://medium.com/@apekshagarwal.742/integration-of-ml-with-devops-2e47bc6e2fd7
