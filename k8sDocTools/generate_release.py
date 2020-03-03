#!/usr/bin/python3

import getpass
import sys
import argparse
import sh
import shutil
import os
from k8sDocTools import __version__
from github import Github
from github import GithubException
from k8sDocTools.globals import repo_id
from k8sDocTools.globals import pages_dir
from k8sDocTools.utils import sync
from k8sDocTools.utils import sshify
from k8sDocTools.bundle import Bundle

def main():
    parser = argparse.ArgumentParser(
        description="Charmed Kubernetes release generator " + __version__
    )

    parser.add_argument("--revision", help="The bundle revision to base the new version on")
    parser.add_argument("-u","--user",
                        help="Username for accessing GitHub")
    parser.add_argument("-p", "--password",
                        help="Token or password for user")
    args = parser.parse_args()

    # get user/password if not supplied
    if not args.user:
      args.user = input("Github username: ")
    if not args.password:
      args.password = getpass.getpass("Github password or personal access token: ")

    g=Github(args.user, args.password)

    # retrieve users name and email for git
    u=g.get_user()
    if u.email == '':
      print("Error: You must have set a public email address in GitHub")
      sys.exit(1)
    # fetch the bundle
    ck = Bundle(args.revision)
    version = ck.release
    # generate a working fork
    docs_repo=g.get_repo(repo_id)
    # find fork url
    fork_url=''
    forks = list(docs_repo.get_forks())
    for f in forks:
      if args.user == f.owner.login:
        fork_url = f.svn_url[18:]
        fork_handle = f
    if fork_url == '':
      print("You have no fork for this repository. Please create one and try again.")
      sys.exit(1)
    print(sshify(fork_url))
    branch_name='release-'+args.version
    local_dir = sync(sshify(fork_url),f.name, docs_repo.svn_url, branch_name, quiet=False)

    # create charm pages
    for charm in ck.charms:
        charm.fetch_page()

    # generate component page
    # add pages to git

    # make PR


if __name__ == "__main__":
    main()
