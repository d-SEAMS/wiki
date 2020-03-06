# Software Quality Management Plan

This section of the wiki is meant for users who wish to gain familiarity with
the code-base and who will eventually be contributing to the project. The
details described here are not set in stone, however, adherence to the ideals
presented in this section will make a PR much more attractive.

## Repository details

- The entire code and development is conducted publicly on GitHub
  - The C++ engine [is here](https://github.com/d-SEAMS/seams-core) (or in the upper right)
  - The wiki itself can be edited (by the pencil icon) [or here](https://github.com/d-SEAMS/wiki)
- Feel free to reach out to the core-developers to help with features being
  worked on

## Style Guide

???+ info "Diversity"
    - The d-SEAMS ecosystem consists of a C++ back-end
    - This is supplemented by a front-end in Lua
    - Initial configuration is through a YAML input
    - It is built with Nix (and CMake)
    - The visualization is effected often through `python` interfaces to OVITO

Hence a separate section for dealing with the various styles and how
they tie into each other [is here](00_styleGuide).
