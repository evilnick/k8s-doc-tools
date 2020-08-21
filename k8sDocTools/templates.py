component_page_tpl ="""---
{{ frontmatter_text }}---

<!-- THIS PAGE IS AUTOGENERATED -->
<!-- If you find an error in this page, it is likely to be in the original
source of the information - please file a bug rather than editing the text -->

This page details the charms, snaps, images and other components
which comprise the {{release}} release of Charmed Kubernetes.

Other information about this release can be found on the following pages:

<a class='p-button--brand' href='/kubernetes/docs'> Documentation </a>
<a class='p-button--brand' href='/kubernetes/docs/{{release}}/release-notes'>Release notes </a>
<a class='p-button--brand' href='/kubernetes/docs/{{release}}/upgrade'>Upgrading </a>
<a class='p-button--brand' href='https://bugs.launchpad.net/charmed-kubernetes'>Bugs </a>
<a class='p-button--brand' href='https://github.com/charmed-kubernetes/bundle'>Source </a>
<a class='p-button--brand' href='https://launchpad.net/charmed-kubernetes/+milestone/{{release}}'>Milestone </a>

## What's new

For a list of new features, changes, deprecations, and bug fixes in this
release, please see the [Release notes](release-notes).

## Core charms

These charms are the core components or official optional components of the
release. These charms are maintained by the Charmed Kubernetes team.

<table class ="u-table-layout--auto">
  <thead>
    <tr>
      <th>Charm</th>
      <th>Summary</th>
      <th>docs</th>
      <th>source</th>
      <th>bugs</th>
      <th>version</th>
      <th>notes</th>
    </tr>
  </thead>
  <tbody>
{% for c in charms -%}
<tr>
  <td> {{c.name}} </td>
  <td> {{c.summary.rstrip()}} </td>
  <td> <a href="/kubernetes/docs/{{release}}/charm-{{c.name}}">docs</a> </td> <td> <a href="{{c.source_url}}"> source </a> </td>
  <td> <a href="https://bugs.launchpad.net/charmed-kubernetes"> bugs</a> </td>
  <td> {{c.revision}} </td>
  <td> -- </td>
</tr>
{% endfor %}
 </tbody>
 </table>

## Compatible Charms

These charms are frequently used with Charmed Kubernetes.

<table class ="u-table-layout--auto">
  <thead>
    <tr>
      <th>Charm</th>
      <th>Summary</th>
      <th>Store page</th>
      <th>notes</th>
    </tr>
  </thead>
  <tbody>
{% for cc in compatible_charms -%}
<tr>
  <td> {{cc.name}} </td>
  <td> {{cc.summary.rstrip()}} </td>
  <td> <a href="https://jaas.ai/{{cc.name}}">docs</a> </td>
  <td> {{cc.notes}} </td>
</tr>
{% endfor %}
 </tbody>
 </table>


## Images

These are the container images used by this release:

<!-- GENERATED CONTAINER IMAGES -->

<!-- CONTAINER IMAGES END -->

## Snaps

The following snaps are used by this release of Charmed Kubernetes:


| snap  | confinement | summary | link |
|-------|-------------|---------|------|
{% for s in snaps.keys() -%}
|{{snaps[s]['Name']}}| ? | {{snaps[s]['Description']}} | ? |
{% endfor %}





<!-- LINKS -->
[documentation]: /kubernetes/docs/
[release notes]: /kubernetes/docs/release-notes#{{release}}
[upgrade notes]: /kubernetes/docs/
[bugs]: /kubernetes/docs/
[source]: https://github.com/charmed-kubernetes
[{{release}} milestone]: https://launchpad.net/charmed-kubernetes/+milestone/{{release}}


"""

charm_config_tpl = """<!-- CONFIG STARTS -->
<!--AUTOGENERATED CONFIG TEXT - DO NOT EDIT -->


| name | type   | Default      | Description                               |
|------|--------|--------------|-------------------------------------------|
{% for c in sorted(options.items()) %}
| <a id="table-${c[0]}"> </a> ${c[0]} | ${c[1]['type']} | ${c[1]['default']} | ${c[1]['description']} |
{% end %}

---

{% for d in sorted(overmatter.items()) %}
### ${d[0]}

{% for i in d[1] %}

${i[0]}
**${i[1]}:**

${i[2]}

{% end %}

{% end %}

<!-- CONFIG ENDS -->
"""



charm_config_tpl_2 = """<!-- CONFIG STARTS -->
<!--AUTOGENERATED CONFIG TEXT - DO NOT EDIT -->


| name | type   | Default      | Description                               |
|------|--------|--------------|-------------------------------------------|
{% for c in options.items()|sort %}
| <a id="table-{{c[0]}}"> </a> {{c[0]}} | {{c[1]['type']}} | {{c[1]['default']}} | {{c[1]['description']}} |
{% endfor %}

---

{% for d in overmatter.items()|sort %}
### {{d[0]}}

{% for i in d[1] %}

{{i[0]}}
**{{i[1]}}:**

{{i[2]}}

{% endfor %}

{% endfor %}

<!-- CONFIG ENDS -->
"""


frontmatter_tpl = {
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
