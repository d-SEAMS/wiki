# Wiki Home

**Deferred Structural Elucidation Analysis for Molecular Simulations**

[![Build Status](https://travis-ci.org/d-SEAMS/seams-core.svg?branch=master)](https://travis-ci.org/d-SEAMS/seams-core)
[![built with nix](https://builtwithnix.org/badge.svg)](https://builtwithnix.org)

- Check our build status [here](https://travis-ci.org/d-SEAMS/seams-core).
- The docs themselves are [here](https://docs.dseams.info) and development is
  ongoing [on GitHub](https://github.com/d-SEAMS/seams-core)
- We also have [a Zenodo community](https://zenodo.org/communities/d-seams/) for user-contributions like reviews, testimonials
  and tutorials
- Trajectories are hosted [on
  figshare](https://figshare.com/projects/d-SEAMS_Datasets/73545).
- Our [wiki is here](https://wiki.dseams.info)

## Citation

!!! success "Published"
     This has been published at the [Journal of Chemical Information and
     Modeling (JCIM)](https://doi.org/10.1021/acs.jcim.0c00031). You may also
     read [the preprint on arXiv](https://arxiv.org/abs/1909.09830).

If you use this software please cite the following paper:

    Goswami, R., Goswami, A., & Singh, J. K. (2020). d-SEAMS: Deferred Structural Elucidation Analysis for Molecular Simulations. Journal of Chemical Information and Modeling. https://doi.org/10.1021/acs.jcim.0c00031

??? info "Bibtex Entry"
         @Article{Goswami2020,
         author={Goswami, Rohit and Goswami, Amrita and Singh, Jayant Kumar},
         title={d-SEAMS: Deferred Structural Elucidation Analysis for Molecular Simulations},
         journal={Journal of Chemical Information and Modeling},
         year={2020},
         month={Mar},
         day={20},
         publisher={American Chemical Society},
         issn={1549-9596},
         doi={10.1021/acs.jcim.0c00031},
         url={https://doi.org/10.1021/acs.jcim.0c00031}
         }



Here, try the abstract:

??? abstract "d-SEAMS: Deferred Structural Elucidation Analysis for Molecular Simulations"
     Structural analyses are an integral part of computational research on nucleation and supercooled water, whose accuracy and efficiency can impact the validity and feasibility of such studies. The underlying molecular mechanisms of these often elusive and computationally expensive processes can be inferred from the evolution of ice-like structures, determined using appropriate structural analysis techniques. We present d-SEAMS, a free and open-source post-processing engine for the analysis of molecular dynamics trajectories, which is specifically able to qualitatively classify ice structures, in both strong confinement and bulk systems. For the first time, recent algorithms for confined ice structure determination have been implemented, along with topological network criteria for bulk ice structure determination. Recognizing the need for customization in structural analysis, d-SEAMS has a unique code architecture, built with `nix`, employing a `YAML`-`Lua` scripting pipeline. The software has been designed to be user-friendly and easy to extend. The engine outputs are compatible with popular graphics software suites, allowing for immediate visual insights into the systems studied. We demonstrate the features of d-SEAMS by using it to analyze nucleation in the bulk regime and for quasi-one and quasi-two-dimensional systems. Structural time evolution and quantitative metrics are determined for heterogenous ice nucleation on a silver-exposed β-AgI surface, homogenous ice nucleation, flat monolayer square ice formation and freezing of an ice nanotube. 

## Details

- There's a [landing page](https://dseams.info) which you might be looking for
- The [developer docs](https://docs.dseams.info) are distinct
- The actual source code [is here](https://github.com/d-SEAMS/seams-core)
- The related publication [pre-print is here](https://arxiv.org/abs/1909.09830)
- This is meant to add details about the process
- It will include the SQM (Software Quality Management) plan
- Examples will be here

## License

        Copyright (C)  d-SEAMS Core Team.
        Permission is granted to copy, distribute and/or modify this document
        under the terms of the GNU Free Documentation License, Version 1.3
        or any later version published by the Free Software Foundation;
        with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
        A copy of the license is included in the section entitled "GNU
        Free Documentation License".

## Acknowledgements

- The SQM is developed as per the guidelines of [Prof. Helmut
  Neukirchen](https://uni.hi.is/helmut/) from the [Software Quality Management](https://ugla.hi.is/kennsluskra/index.php?tab=nam&chapter=namskeid&id=08732220210&merkja=Software+Quality+Management&kennsluar=2020) course
