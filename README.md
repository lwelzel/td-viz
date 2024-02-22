# td-viz
Visualization of Tensor Decompositions

Produce publication quality tikz figures of tensor decompositions for use in Latex.

## 3D visualizations of tensor decompositions
Define the parameters of the decomposition and automatically produce the appropriate visualization. Currently only supports Tensor Train and Tensor Ring decompositions.

### Order-4 Tensor Train
![image](https://github.com/lwelzel/td-viz/assets/29613344/a2a3dfee-c2e9-45c8-a6aa-fba3057eb716)


### Order-4 Tensor Ring
![image](https://github.com/lwelzel/td-viz/assets/29613344/252d8204-55ce-405e-a04c-c1a7a2231a3b)


## 2D visualizations of tensor decompositions in tensor network diagrams
Tensor network diagrams. Currently does not support automatic figure generation. Requires the tikz-network package.
### Tensor
![image](https://github.com/lwelzel/td-viz/assets/29613344/e88b4e1b-6e5a-4faa-8903-cdf6212cb5bb)

### CP Decomposition
![image](https://github.com/lwelzel/td-viz/assets/29613344/e563f08a-28ad-4daf-95f4-0a97a88a0bf2)

### Tucker Decomposition
![image](https://github.com/lwelzel/td-viz/assets/29613344/452e1f5d-3993-4355-81d6-c3402794bbbb)

### Tensor Train Decomposition
![image](https://github.com/lwelzel/td-viz/assets/29613344/688ef096-0e46-4ab7-8bdc-687298f302c4)

### Tensor Ring Decomposition
In either TT or TR formatting:
![image](https://github.com/lwelzel/td-viz/assets/29613344/d89cab80-4256-46a3-b083-49a6ebacee01)


## Usage
Please attribute me (Lukas Welzel) if you use this package.

### Geometric tikz figures
Use the provided python script to produce either TT or TR decomposition figures. 

### TND style figures
Use the provided Latex baselines.

### Requirements
#### Geometric tikz figures
- Python 3.6+
- numpy

#### TND style figures 
- tikz-network

## Existing Tools:
- [mptikz - graphical tensor notation for LuaTeX](https://github.com/dsuess/mptikz)
- [PyZX](https://github.com/Quantomatic/pyzx)
- [QUIMB drawing tools](https://quimb.readthedocs.io/en/latest/tensor-drawing.html)

## Motivation

When working on TD I found that there were no good tools to produce high quality plots of TD in either TND or, 
even less so, in their geometric form. 
This package aims to provide a simple way to produce high quality figures of tensor decompositions. 
Currently, it is a bit of a hack job but if you need to produce figures or equations that look somewhat like the cases 
that are shown above it will do the job. In the future, I aim to clean this up and make it a bit more user-friendly. 
I do not have a very strong background in TD or TND so please feel free to contribute to this project or notify me of 
any errors.
