# Style Guide

As noted [on the SQM Plan](https://wiki.dseams.info/sqm%20plan/#style-guide), there is a diverse array of tools and languages which
are tied together in a seamless whole for the analysis of trajectories.

## Code Formatting

- Formatting should be consistent
- Consistency is best obtained by standardized automated tooling
- This may sound a lot like the `python` methodology, but it differs from
  `python` in that it is a lot more sane to not enforce white-space in the
  language itself
- The sweet-spot is the usage of post-coding formatters, which are sensitive to
  user-directives
- These formatters are thus IDE independent and also flexible in terms of
  allowing judicious diversions from the style-guide

### Clang Format

The best way to auto-format code is the `clang-format` tool. Custom rules are often
provided in the project root. The tool is [available online](https://clang.llvm.org/docs/ClangFormat.html).

- This works for most IDEs:
  - [Emacs](https://github.com/lassik/emacs-format-all-the-code)
  - [Sublime Text 3](https://packagecontrol.io/packages/Clang%20Format)
  - [Vim](https://github.com/rhysd/vim-clang-format)

## C++ Guide

- `clang-format` is the preferred tool for formatting the code (defaults work
  fine)
- The `llvm` ecosystem and static analysis are favored heavily, including the
  use of `clang`
- We strive to ensure modern (min. C++11) code as far as possible
- It is nicer to have verbosity (through comments) than verbose code

!!! warning "Use namespaces"
    Namespaces are crucial to our workflow, **no top-level imports** are allowed

- Doxygen is used for generating [API documentation](https://docs.dseams.info)

!!! note "Annotate scientific details"
    We would prefer that all formulae are documented (with LaTeX) for every method where applicable, along with references

- Unit tests are exceedingly important, due to the modular structure of the code
  - We use Catch2 for testing
- Every C++ function must have a Lua interface which _must be_ documented

We leverage the following libraries:

- [Catch2](https://github.com/catchorg/Catch2) for tests
- [cxxopts](https://github.com/jarro2783/cxxopts) for parsing command line options
- [rang](https://github.com/agauniyal/rang) for terminal styles (ANSI)
- [sol3](https://github.com/ThePhD/sol2) for interfacing with lua
- [yaml-cpp](https://github.com/jbeder/yaml-cpp) for working with `yaml`
- [Linear Algebra PACKage (LAPACK)](http://www.netlib.org/lapack/)
- [Basic Linear Algebra Subprograms (BLAS)](http://www.netlib.org/blas/)
- [Spectra](https://github.com/yixuan/spectra/) for faster matrix calculations
- [Boost Geometry](https://www.boost.org/doc/libs/1_68_0/libs/geometry/doc/html/index.html) for working with different coordinates
- [Boost Math](https://www.boost.org/doc/libs/?view=category_math) for spherical harmonics

!!! note "Use included libraries"
    We support a wide range of popular libraries, so do not add additional ones
    unless they are crucial to the algorithm and furthermore **are part of the nix build**

### Resources

C++ is a rather fast moving target, so in most cases, the relevant library
documentation is the best source.

- The [LLVM standards](https://llvm.org/docs/CodingStandards.html)

??? info
    We don't actually enforce these standards everywhere. Just remember to keep
    things `clang-tidy` and similar to whatever you see in the code. A quick rule of
    thumb is that if you are not contributing more code than what exists already,
    **don't be a hero** about the style guide
    - If you do have a strong opinion about a style guide, open an issue and
      talk to us

## Lua Guide

- All `lua` scripts must be accompanied by comments
- Every script must have details of which trajectory is required

!!! warning "Document lua"
    Since our Doxygen setup does not extract `lua` function descriptions, do
    remember to link to the C++ API and describe functions in the associated
    markdown file. Also, you will want to update the wiki to include the lua functions

### Resources

- The official [lua resources](https://www.lua.org/)
- The [sol3 documentation](http://sol2.rtfd.io/)

## YAML Guide

- Use short comments

!!! note "Examples"
    It is highly unlikely that a YAML file will be added without a corresponding
    trajectory (on figshare preferably) and a Lua script, thus it is best to
    **add an example** to the [user wiki](../examples/index)

### References

- [yaml-cpp](https://github.com/jbeder/yaml-cpp) documentation
- [Official specifications](https://yaml.org/)

## Nix Guide

!!! danger
    This is often one of the most difficult parts of the work-flow to grasp due
    to the functional programming principles involved.

- **Never** use anything locally built
- **Purity** is required during your builds (the CI enforces this)

??? info
    In-spite of this, most contributors will not have to mess around with the
    nix-build setup more than what will be natural upon inspecting the [existing code](https://github.com/d-SEAMS/seams-core).

### Resources

- [Nix pills](https://nixos.org/nixos/nix-pills/index.html)
- Official [nix-lang manual](https://nixos.org/nix/manual/)
- [Existing code](https://github.com/d-SEAMS/seams-core/blob/master/shell.nix)

??? note
    Historically, the `nix-lang` derivations were originally written in an
    `org-mode` file and tangled out to separate segments. This was depreciated
    since it made it harder for non-emacs users to contribute.
