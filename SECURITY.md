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
packages. Feed bodies are size-limited, DTD and entity declarations are
rejected, arXiv identifiers and redirect targets are validated, and generated
links are rebuilt from validated identifiers. Workflow write permission is
limited to repository contents. After a concurrent main update, the workflow
regenerates once from the new head rather than rebasing output produced by
older code; another race fails safely.

The GitHub Pages frontend uses a first-party Content Security Policy and puts
all paper metadata into text-only DOM sinks. Generated arXiv links are derived
from validated identifiers; the frontend does not execute remote scripts or
load third-party runtime dependencies.
