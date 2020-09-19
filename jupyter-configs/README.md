
## Additional config for jupyterhub on OpenShift cluster

Copy the contents of jupyterhub_config.{py,sh} to their respective files in the OpenShift configuration:  
`Resources > config maps > myApp-cfg`. The files should already be there (but empty), if deployed with the jupyter-on-openshift/jupyterhub-quickstart templates.  
Do not forget to setup the github OAuth application and fill in the details here.


TODO   
Then, define shared persistent storage:  
`Storage > Create Storage`. Make sure to mark the RWX radio button.  
Attach it to the application:  
`Applications > Deployments > Configuration > Add Storage`.  Set mount path to /opt/app-root/src/. 


(Application should then automatically redeploy. If not, `Applications > Deployments > myApp > Deploy`). 

