
# copied from https://github.com/jupyter-on-openshift/jupyter-notebooks/blob/2.5.1/minimal-notebook/jupyter_notebook_config.py

import os

port = int(os.environ.get('JUPYTER_NOTEBOOK_PORT', '8080'))

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = port
c.NotebookApp.open_browser = False
c.NotebookApp.quit_button = False

if os.environ.get('JUPYTERHUB_SERVICE_PREFIX'):
    c.NotebookApp.base_url = os.environ.get('JUPYTERHUB_SERVICE_PREFIX')

#password = os.environ.get('JUPYTER_NOTEBOOK_PASSWORD')
#if password:
#    import notebook.auth
#    c.NotebookApp.password = notebook.auth.passwd(password)
#    del password
#    del os.environ['JUPYTER_NOTEBOOK_PASSWORD']

image_config_file = '/opt/app-root/src/.jupyter/jupyter_notebook_config.py'

if os.path.exists(image_config_file):
    with open(image_config_file) as fp:
        exec(compile(fp.read(), image_config_file, 'exec'), globals())


# List of notebooks to start in hub

#c.KubeSpawner.profile_list = [
#    {
#        'display_name': 'Minimal Notebook (CentOS 7 / Python 3.6)',
#        'kubespawner_override': {
#            'image_spec': 's2i-minimal-notebook:3.6'
#        }
#    },
#    {
#        'display_name': 'ROOT data science Notebook (CentOS 7 / Python 3.6 / ROOT 6.22 / tensorflow 2.0)',
#        'default': True,
#        'kubespawner_override': {
#            'image_spec': 's2i-root-notebook:v1.0'
#        }
#    }
#]


# Set notebook options
c.KubeSpawner.environment = { 'JUPYTER_ENABLE_LAB': 'true' }


# Set user authentication
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator

c.GitHubOAuthenticator.oauth_callback_url = 'https://<jupyterhubURL>/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = '<githubclientkey>'
c.GitHubOAuthenticator.client_secret = '<githubclientsecret>'

c.Authenticator.admin_users = {'<githubusername>'}
c.Authenticator.whitelist = {'user1','user2'}


# Set persistent storage

c.KubeSpawner.user_storage_pvc_ensure = True

c.KubeSpawner.pvc_name_template = 'nb-{username}' 
c.KubeSpawner.user_storage_capacity = '1Gi'

c.KubeSpawner.volumes = [
    {
        'name': 'data',
        'persistentVolumeClaim': {
            'claimName': c.KubeSpawner.pvc_name_template
        }
    }
]

c.KubeSpawner.volume_mounts = [
    {
        'name': 'data',
        'mountPath': '/opt/app-root/src'
    }
]


# Cull idle notebooks

#c.JupyterHub.services = [
#    {
#        'name': 'cull-idle',
#        'admin': True,
#        'command': ['cull-idle-servers', '--timeout=1800'],
#    }
#]
