# jupyter-root
Jupyter notebook for data science with PyROOT, s2i ready for deployment in jupyterhub on OpenShift.  
  centOS7, python 3.6, tensorflow 2.0 and ROOT 6.22.  

Based on https://github.com/jupyter-on-openshift/jupyter-notebooks/tree/2.5.1 which is based on https://hub.docker.com/r/centos/python-36-centos7 .  
ROOT build following https://github.com/root-project/root-docker .  

Deployment in openshift via https://github.com/jupyter-on-openshift/jupyterhub-quickstart  
(Update: use instead https://github.com/jupyter/docker-stacks/tree/master/examples/openshift ?)

Docker: https://hub.docker.com/r/jackfrost373/jupyter-root  
Image can be run with  
`docker run -p 8080:8080 -e JUPYTER_ENABLE_LAB=true jackfrost373/jupyter-root[:tag]`  
The notebook is then served at http://127.0.0.1:8080



================================

To deploy on the OpenShift web interface:

- add the notebook image:  (top-right, 'add to project' > 'import YAML/JSON')  
copy contents of `image-streams/s2i-root-notebook.json`

- add the hub image:  
https://raw.githubusercontent.com/jupyter-on-openshift/jupyterhub-quickstart/master/image-streams/jupyterhub.json

- add the deployment template:  
`templates/jupyterhub-deployer.json`  

- add an instance from the template (bottom left, 'templates' > 'JupyterHub')

- Add the custom config files:  
  `Resources > config maps > myApp-cfg`  
  Replace with content from `jupyter-configs`
  
- Redeploy

