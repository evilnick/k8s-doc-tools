
import yaml
import requests

core = {
'aws-iam': 0,
'aws-integrator': 0,
'azure-integrator': 0,
'calico': 0,
'canal': 0,
'containerd': 0,
'docker': 0,
'docker-registry': 0,
'easyrsa': 0,
'etcd': 0,
'flannel': 0,
'gcp-integrator': 0,
'kata': 0,
'keepalived': 0,
'kubeapi-load-balancer': 0,
'kubernetes-master': 0,
'kubernetes-worker': 0,
'openstack-integrator': 0,
'tigera-secure-ee': 0,
'vsphere-integrator': 0,
}





class Bundle():
    def __init__(self,revision):
        self.revision = revision
        self.store_url = 'https://api.jujucharms.com/charmstore/v5/bundle/charmed-kubernetes-'+self.revision+'/archive/bundle.yaml'
        self.yaml = requests.get(self.store_url).content
        self.obj = yaml.load(self.yaml, Loader=yaml.FullLoader)
        self.channel = self.obj['services']['kubernetes-master']['options']['channel']
        self.release = self.channel.split('/')[0]
        self.services = list(self.obj['services'].keys())
        self.core_versions = core


    def __repr__(self):
        return(str(self.yaml))

    def get_snaps(self):
        pass
