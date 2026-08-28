# Security Policy

## Reporting a vulnerability

Do not open a public issue for a vulnerability in the collector or workflow.
Use GitHub's private vulnerability reporting feature for this repository.

Include the affected file, impact, reproduction steps, and any suggested
mitigation. Reports about the content of linked research papers are out of
scope; contact the paper authors or arXiv as appropriate.

## Workflow trust boundary

The scheduled workflow treats arXiv metadata as untrusted display content. It
does not execute paper content, follow arbitrary paper links, or install Python
packages. Workflow write permission is limited to repository contents.
