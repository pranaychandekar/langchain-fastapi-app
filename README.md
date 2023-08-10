# Web Service to host an ML Model for Prediction. 
A simple python web service to host a machine learning model for prediction as a REST API.      
  
<p align="center">          
  <img src="/docs/images/mpws-00.jpg" alt="RESTful Web Service">          
</p>    
  
The container trains a simple [text classifier](https://fasttext.cc/docs/en/supervised-tutorial.html) and hosts it for prediction as a web service using [FastAPI](https://fastapi.tiangolo.com/). The data for model training is included in the project.       
  
  
>*For more details on customizing this project or using this as a template please follow [this article](https://medium.com/analytics-vidhya/ml-prediction-as-a-restful-web-service-9fa33d01566f).*  
  ---      
 ### Pre-requisites      
 1. System should have [docker engine](https://docs.docker.com/install/) installed.      
>**Note**: I developed and tested this on Ubuntu-16.04.      
 ---      
 ### Hosting the web service      
 1. Build the docker image       
```bash 
docker build --network=host -t ml-prediction-web-service:v1 .  
```   
2. Check the image       
```bash 
docker images 
``` 
<p align="center">          
  <img src="/docs/images/mpws-01.png" alt="Docker Images">          
</p>          
    
3. Run the container      
```bash  
docker run -d --net=host --name=ml-prediction-web-service ml-prediction-web-service:v1
```    
    
4. Check whether the container is up       
```bash 
docker ps 
``` 
<p align="center">          
  <img src="/docs/images/mpws-02.png" alt="Running Containers">          
</p>          
      
      
>When we run the container two scripts are initiated: 
>1. `train.py` which trains the model to be hosted. 
>2. `app.py` which hosts the model as a web service.      
 ---      
 ### API Usage   
 The web services includes the openapi integration. Thus, we can directly use the swagger portal from web browser to use the API. To open the swagger portal go to your browser and enter `http://localhost:8080/swagger/`. This will open the swagger portal only if the service is hosted properly.      
<p align="center">          
  <img src="/docs/images/mpws-03.png" alt="Swagger Portal">          
</p>          
      
To check whether service is up:      
      
 1. Click on the `GET` bar.       
      
 2. Click on `Try it out` <p align="center">          
  <img src="/docs/images/mpws-04.png" alt="Try It Out">          
</p>         
      
 3. Click on `Execute` <p align="center">          
  <img src="/docs/images/mpws-05.png" alt="Execute">          
</p>         
      
 4. If you see the following screen then your service is up.      
<p align="center">          
  <img src="/docs/images/mpws-06.png" alt="Service Up">          
</p>          
      
To predict the label of the text:      
      
 1. Click on the `POST` bar.       
      
 2. Click on `Try it out` 
 <p align="center">          
  <img src="/docs/images/mpws-07.png" alt="Try It Out">          
</p>         
      
 3. Click on `Execute`      
 4. We should see a response similar to the following:      
<p align="center">          
  <img src="/docs/images/mpws-09.png" alt="Prediction Response">          
</p>          
      
---      
 ### Logs checking   
 To check the the web service logs we need to get inside the running container. To do so execute the following command:      
```bash  
docker exec -it ml-prediction-web-service bash
``` 
Now we are inside the container.      
      
The logs are available in the logs folder in the files `ml-prediction-web-service.log` and `ml-prediction-web-service.err`.      
      
<p align="center">          
  <img src="/docs/images/mpws-10.png" alt="Inside container">          
</p>          
      
---      
 ### Stopping the web service   
 Run the following command to stop the container:      
```bash  
docker stop ml-prediction-web-service
```  
---      
 ### API Documentation with [ReDoc](https://github.com/Redocly/redoc)   
 <p align="center">          
  <img src="/docs/images/mpws-11.png" alt="ReDoc Top">          
</p>

<p align="center">          
  <img src="/docs/images/mpws-12.png" alt="ReDoc API Details">          
</p>
 
--- 
**Author**: [Pranay Chandekar](https://www.linkedin.com/in/pranaychandekar/)