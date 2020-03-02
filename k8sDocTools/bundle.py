#!/usr/bin/python3

import ruamel.yaml
import requests
from jinja2 import Template
from k8sDocTools.charm import Charm
from k8sDocTools.templates import component_page_tpl


core = {
'aws-iam': '0',
'aws-integrator': '0',
'azure-integrator': '0',
'calico': '0',
'canal': '0',
'containerd': '0',
'docker': '0',
'docker-registry': '0',
'easyrsa': '0',
'etcd': '0',
'flannel': '0',
'gcp-integrator': '0',
'kata': '0',
'keepalived': '0',
'kubeapi-load-balancer': '0',
'kubernetes-master': '0',
'kubernetes-worker': '0',
'openstack-integrator': '0',
'tigera-secure-ee': '0',
'vsphere-integrator': '0'
}


frontmatter = {
'wrapper_template': 'kubernetes/docs/base_docs.html',
'markdown_includes': {'nav': 'kubernetes/docs/shared/_side-navigation.md'},
'context': {'title': 'Components', 'description': 'Detailed description of Charmed Kubernetes release'},
'keywords': 'component, charms, versions, release',
'tags': ['reference'],
'sidebar': 'k8smain-sidebar',
'permalink': '-',
'layout': ['base', 'ubuntu-com'],
'toc': False
}


class Bundle():
    def __init__(self,revision):
        self.revision = revision
        self.store_url = 'https://api.jujucharms.com/charmstore/v5/bundle/charmed-kubernetes-'+self.revision+'/archive/bundle.yaml'
        self.frontmatter = frontmatter
        self.yaml = requests.get(self.store_url).content
        self.obj = ruamel.yaml.YAML(typ='safe').load(self.yaml)
        self.channel = self.obj['services']['kubernetes-master']['options']['channel']
        self.release = self.channel.split('/')[0]
        self.services = list(self.obj['services'].keys())
        self.core_versions = core
        self.charms = list()
        # get pinned versions from bundle
        for s in self.services:
            self.core_versions[s] = self.obj['services'][s]['charm'].split('-')[-1:][0]
        for c in self.core_versions.keys():
            self.charms.append(Charm(c, self.core_versions[c]))
        self.snaps = dict()
        # join dicts from all charms to create full dict of snaps
        for c in self.charms:
            self.snaps = {**self.snaps, **c.snaps}

    def __repr__(self):
        return(str(self.yaml))

    def generate_page(self, path):
        # update frontmatter
        self.frontmatter['permalink'] = '/'.join((path,'components.html'))
        self.frontmatter['bundle_revision'] = self.revision
        self.frontmatter['bundle_release'] = self.release
        self.frontmatter['context']['title'] = 'Components of Charmed Kubernetes ' + self.release
        self.frontmatter_text = ruamel.yaml.round_trip_dump(self.frontmatter, block_seq_indent=4)
        t = Template(component_page_tpl)
        self.page = t.render(vars(self))
        # generate page from template
