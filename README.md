# jupyter-root
Jupyter notebook for data science with PyROOT, s2i ready for deployment in jupyterhub on OpenShift.  
  centOS7, python 3.6, tensorflow 2.0 and ROOT 6.22.  

Based on https://github.com/jupyter-on-openshift/jupyter-notebooks/tree/2.5.1  
  based on https://hub.docker.com/r/centos/python-36-centos7 .  
ROOT build following https://github.com/root-project/root-docker .  

Deployment in openshift via https://github.com/jupyter-on-openshift/jupyterhub-quickstart  

Docker: https://hub.docker.com/r/jackfrost373/jupyter-root  
Image can be run with  
`docker run -p 8080:8080 jackfrost373/jupyter-root[:tag]`  
The notebook is then served at http://127.0.0.1:8080


