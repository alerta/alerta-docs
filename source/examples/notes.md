note: content in first line only
.
```{note} a
```
.
arguments: []
body:
- a
content_offset: 0
options: {}
warnings: []
.

note: content in body only
.
```{note}
a
```
.
arguments: []
body:
- a
content_offset: 0
options: {}
warnings: []
.

note: content after option
.
```{note}
:class: name
a
```
.
arguments: []
body:
- a
content_offset: 1
options:
  class:
  - name
warnings: []
.

note: content after option with new line
.
```{note}
:class: name

a
```
.
arguments: []
body:
- a
content_offset: 2
options:
  class:
  - name
warnings: []
.

note: content after yaml option
.
```{note}
---
class: name
---
a
```
.
arguments: []
body:
- a
content_offset: 3
options:
  class:
  - name
warnings: []
.

note: content in first line and body
.
```{note} first line
:class: tip

body line
```
.
arguments: []
body:
- first line
- ''
- body line
content_offset: 1
options:
  class:
  - tip
warnings: []
.

admonition: no options, no new line
.
```{admonition} first line
body line
```
.
arguments:
- first line
body:
- body line
content_offset: 0
options: {}
warnings: []
.

admonition: no options, new line
.
```{admonition} first line

body line
```
.
arguments:
- first line
body:
- body line
content_offset: 1
options: {}
warnings: []
.

admonition: with options
.
```{admonition} first line
:class: tip

body line
```
.
arguments:
- first line
body:
- body line
content_offset: 2
options:
  class:
  - tip
warnings: []
.

warning: bad yaml
.
```{note}
---
a: {
---
```
.
arguments: []
body: []
content_offset: 3
options: {}
warnings:
- Invalid options format (bad YAML)
.

warning: yaml not a dict
.
```{note}
---
a
---
```
.
arguments: []
body: []
content_offset: 3
options: {}
warnings:
- Invalid options format (not a dict)
.

warning: unknown option name
.
```{note}
:unknown: name
```
.
arguments: []
body: []
content_offset: 1
options: {}
warnings:
- 'Unknown option keys: [''unknown''] (allowed: [''class'', ''name''])'
.

warning: invalid option value
.
```{note}
:class: 1
```
.
arguments: []
body: []
content_offset: 1
options: {}
warnings:
- 'Invalid option value for ''class'': 1: cannot make "1" into a class name'
.

error: missing argument
.
```{admonition}
```
.
error: 1 argument(s) required, 0 supplied
.