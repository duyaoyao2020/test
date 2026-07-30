# Third-party writing tools

This directory keeps external projects that are useful for improving AI-assisted writing workflows.

## Projects

- `Humanizer-zh`: Chinese text humanization skill for reducing typical AI wording and making generated drafts sound more natural.
  - Source: https://github.com/op7418/Humanizer-zh
- `no-ai-slop`: Writing quality checklist and workflow for removing vague, generic, or over-polished AI prose.
  - Source: https://github.com/petergyang/no-ai-slop

## Notes

These projects are included as Git submodules, so their upstream history stays separate from this repository. After cloning this repository, initialize them with:

```sh
git submodule update --init --recursive
```
