
## Additional config for jupyterhub. 
## Set it via the JUPYTERHUB_CONFIG template parameter.
## Finally, attach persistent storage to the deployment.

# List of notebooks to start in hub

c.KubeSpawner.profile_list = [
    {
        'display_name': 'Minimal Notebook (CentOS 7 / Python 3.6)',
        'kubespawner_override': {
            'image_spec': 's2i-minimal-notebook:3.6'
        }
    },
    {
        'display_name': 'ROOT data science Notebook (CentOS 7 / Python 3.6 / ROOT 6.22 / tensorflow 2.0)',
        'default': True,
        'kubespawner_override': {
            'image_spec': 's2i-root-notebook:v1.0'
        }
    }
]


# Set notebook options

c.KubeSpawner.environment = { 'JUPYTER_ENABLE_LAB': 'true' }


# Set user authentication

from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator

c.GitHubOAuthenticator.oauth_callback_url = 'https://<your-jupyterhub-hostname>/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = 'your-client-key-from-github'
c.GitHubOAuthenticator.client_secret = 'your-client-secret-from-github'

c.Authenticator.admin_users = {'your-github-username'}
c.Authenticator.whitelist = {'user1', 'user2', 'user3', 'user4'}


# Set persistent storage

c.KubeSpawner.user_storage_pvc_ensure = True

c.KubeSpawner.pvc_name_template = '%s-nb-{username}' % c.KubeSpawner.hub_connect_ip
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

c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': ['cull-idle-servers', '--timeout=1800'],
    }
]
