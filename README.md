# Deep archive command for `git`

## Features

- Archive a git repository with all sub-modules.
- Speicify the a tag of ref of the repository to archive.

## Installation

You can install _Git Archive Deep_ via [pip] from [PyPI]:

```console
$ pip install git-archive-deep
```

## Usage

Let's say you have a repository in a directory `MyTool/` and you want to archive version 2.1, which is tagged `v2.1`.
```console
git archive-deep v2.1 ./MyTool
```
This will create a zip file named `MyTool-v2.1.zip` that contains the repository along with its sub-modules.

This tool is similar to [git-archive-all](https://github.com/Kentzo/git-archive-all), but it allows you to specify a
git ref instead of archiving the currently checked out commit. It is really just simple wrapper around Git that calls
`git archive <ref> .` in the repository directory, but then reads `.gitmodules` (if it exists), determines the SHA1 for each
sub-module using `git rev-parse` (calling `git rev-parse v2.1:path/to/submodule` will print the SHA1 for the commit that is checked out in submodule
located at `path/to/submodule` for version `v2.1`), and then just calls itself for each sub-module recursively, merging each archive into the main repo.

## License

Distributed under the terms of the [MIT license][license],
_Git Archive Deep_ is free and open source software.

