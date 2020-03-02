#!/usr/bin/python3

from theblues.charmstore import CharmStore
cs = CharmStore('https://api.jujucharms.com/v5')


class Charm():
    """
    Fetches the charm info from the CharmStore and unpacks some values
    to make it possible to use in templates.
    If instantiated with a 'revision' of 0, will fetch info from the latest
    stable version.
    """
    def __init__(self,name,revision):

        self.name = name
        self.store_name = 'cs:~containers/'+name
        self.revision = revision
        if self.revision == '0':
            # get latest version from the store and update revision
            self.obj =  CharmStore('https://api.jujucharms.com/v5').entity(self.store_name)
            self.revision = self.obj['Id'].split('-')[-1:][0]
        else:
            self.obj =  CharmStore('https://api.jujucharms.com/v5').entity(self.store_name+'-'+revision)



        self.bugs_url = 'https://bugs.launchpad.net/charmed-kubernetes'
        self.bugs_url = 'https://github.com/charmed-kubernetes'
        if isinstance (self.obj['Meta']['common-info'], dict):
            if 'bugs-url' in self.obj['Meta']['common-info']:
                self.bugs_url = self.obj['Meta']['common-info']['bugs-url']
            if 'homepage' in self.obj['Meta']['common-info']:
                self.source_url = self.obj['Meta']['common-info']['homepage']
        self.actions = list()
        if 'ActionSpecs' in self.obj['Meta']['charm-actions']:
            if isinstance(self.obj['Meta']['charm-actions']['ActionSpecs'], list):
                self.actions = list(self.obj['Meta']['charm-actions']['ActionSpecs'].keys())
        self.summary = self.obj['Meta']['charm-metadata']['Summary']
        self.description = self.obj['Meta']['charm-metadata']['Description']
        self.storage = list()
        if 'Storage' in self.obj['Meta']['charm-metadata']:
            self.storage = list(self.obj['Meta']['charm-metadata']['Storage'].keys())
        self.snaps = dict()
        self.files = dict()
        if 'Resources' in self.obj['Meta']['charm-metadata']:
            for resource in self.obj['Meta']['charm-metadata']['Resources'].keys():
                if(self.obj['Meta']['charm-metadata']['Resources'][resource]['Path'][-5:] == '.snap'):
                    self.snaps[resource] = self.obj['Meta']['charm-metadata']['Resources'][resource]
                else:
                    self.files[resource] = self.obj['Meta']['charm-metadata']['Resources'][resource]
