# Temporal 3DSG Task Planning Benchmark

This repository provides a temporal task planning benchmark built on top of the 3DSG dataset. The benchmark is designed to evaluate whether embodied agents can reason not only over the current state of a 3D scene, but also over historical changes in object locations and object states.

The benchmark contains seven indoor environments, six task domains, and multiple temporal task variants. It is intended for research on robotic task planning, scene graph reasoning, temporal memory, and embodied decision making.

## Overview

We adopt seven scenes from the 3DSG dataset as experimental environments:

* Allensville
* Parole
* Shelbiana
* Kemblesville
* Pablo
* Rosser
* Office

Following the experimental setting of DELTA, we define six evaluation domains:

* Laundry
* Human
* Clean
* Dining
* Office
* PC

To better match the requirements of these domains, the original 3DSG scenes are further augmented with task-related objects. The processed scenes are represented as scene graphs containing multiple node and relation types. These graphs provide the structural basis for task planning in each environment.


## Benchmark Scale

The benchmark contains:

| Component               | Number |
| ----------------------- | -----: |
| Environments            |      7 |
| Domains per environment |      6 |
| Task cases per domain   |      4 |
| Basic task cases        |     42 |
| Temporal task cases     |    126 |
| Total task cases        |    168 |

Each environment contains six domains, and each domain includes one basic task and three temporal variants. This results in a total of 168 task cases.

## Citation

If you use this benchmark, please cite the original 3DSG dataset and the related experimental setting:

```bibtex
@inproceedings{armeni3DSceneGraph2019,
  title = {{{3D Scene Graph}}: {{A Structure}} for {{Unified Semantics}}, {{3D Space}}, and {{Camera}}},
  booktitle = {2019 {{IEEE}}/{{CVF International Conference}} on {{Computer Vision}} ({{ICCV}})},
  author = {Armeni, Iro and He, Zhi-Yang and Zamir, Amir and Gwak, Junyoung and Malik, Jitendra and Fischer, Martin and Savarese, Silvio},
  year = 2019
}

```

```bibtex
@inproceedings{liuDELTADecomposedEfficient2025,
  title = {{{DELTA}}: {{Decomposed Efficient Long-Term Robot Task Planning}} Using {{Large Language Models}}},
  booktitle = {2025 {{IEEE International Conference}} on {{Robotics}} \& {{Automation}} ({{ICRA}})},
  author = {Liu, Yuchen and Palmieri, Luigi and Koch, Sebastian and Georgievski, Ilche and Aiello, Marco},
  year = 2025
}
```

## License

Please check the license terms of the original 3DSG dataset before using or redistributing the processed data. The license of the code and benchmark annotations should be specified in this repository.
