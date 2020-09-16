# jupyter-root
Jupyter notebook for data science with ROOT, s2i ready for deployment in jupyterhub on OpenShift.


Based on https://github.com/jupyter-on-openshift/jupyter-notebooks/tree/2.5.1  
Deployment in openshift via https://github.com/jupyter-on-openshift/jupyterhub-quickstart  

Docker: https://hub.docker.com/r/jackfrost373/jupyter-root  
Image can be run with  
`docker run -p 8080:8080 jackfrost373/jupyter-root[:tag]`  
The notebook is then served at http://127.0.0.1:8080

