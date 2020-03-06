# Style Guide

As noted [on the SQM Plan](https://wiki.dseams.info/sqm%20plan/#style-guide), there is a diverse array of tools and languages which
are tied together in a seamless whole for the analysis of trajectories.

## C++ Guide

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
