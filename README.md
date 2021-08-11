# PiTree Dataset

## About
PiTree dataset is motivated by the insufficiency of existing datasets in adaptive video streaming. 
Many existing emulation datasets, such as [Pensieve](https://github.com/hongzimao/pensieve) or [Oboe](https://github.com/usc-nsl/oboe), are collected years ago with the average bandiwdth of around 1Mbps.
However, with the recent development of communication technology (e.g., 5G), Internet nowadays usually provides a much higher bandwidth of more than 10Mbps.
Therefore, we feel that it is essential to construct a new dataset on both videos and network traces to faithfully evaluate the performance of bitrate adaption algorithms.

You may want to visit the following pages for the details of the dataset:
- [Traces](traces/)
- [Video](video/)

## Citation
~~~
@inproceedings{meng2019pitree,
    author = {Meng, Zili and Chen, Jing and Guo, Yaning and Sun, Chen and Hu, Hongxin and Xu, Mingwei},
    title = {PiTree: Practical Implementation of ABR Algorithms Using Decision Trees},
    year = {2019},
    url = {https://doi.org/10.1145/3343031.3350866},
    booktitle = {Proceedings of the 27th ACM International Conference on Multimedia},
    pages = {2431–2439},
    location = {Nice, France},
    series = {MM ’19}
}

@article{meng2021practically,
    author = {Meng, Zili and Guo, Yaning and Shen, Yixin and Chen, Jing and Zhou, Chao and Wang, Minhu and Zhang, Jia and Xu, Mingwei and Sun, Chen and Hu, Hongxin},
    title = {Practically Deploying Heavyweight Adaptive Bitrate Algorithms With Teacher-Student Learning},
    year = {2021},
    url = {<a href="https://doi.org/10.1109/TNET.2020.3048666">https://doi.org/10.1109/TNET.2020.3048666</a>},
    journal = {IEEE/ACM Transactions on Networking},
    pages = {723-736},
    volume = {29},
    number = {2}
}
~~~
