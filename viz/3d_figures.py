import numpy as np


def generate_tensor_train_tikzpicture(tensor_shape, tensor_ranks):
    tensor_shape = np.array(tensor_shape, dtype=int)
    tensor_ranks = np.array(tensor_ranks, dtype=int)

    # scaling:
    max_val = np.maximum(tensor_shape.max(), tensor_ranks.max())

    power = 4

    scaled_tensor_shape = tensor_shape ** (1/power)
    scaled_tensor_ranks = tensor_ranks ** (1/power)
    scaled_tensor_ranks[0] = 0
    scaled_tensor_ranks[-1] = 0

    # rel scaling
    # tensor_shape = tensor_shape / max_val
    # tensor_ranks = tensor_ranks / max_val

    # geometry scaling
    tikz_scaling = 0.65

    latex_code = f"""
    \\begin{{equation}}
        \\mathcal{{X}} \\approx 
        \\begin{{tikzpicture}}[baseline={{-0.5*{scaled_tensor_ranks[1]:2f}*{tikz_scaling}cm}}, scale={tikz_scaling}, every node/.style={{font=\\tiny}}, every edge quotes/.append style={{auto, text=black}}]
            \\pgfmathsetmacro{{\\cubex}}{{{scaled_tensor_shape[0]:2f}}}
            \\pgfmathsetmacro{{\\cubey}}{{{scaled_tensor_ranks[1]:2f}}}
            \\pgfmathsetmacro{{\\cubez}}{{{scaled_tensor_ranks[0]:2f}}}
            \\draw [draw=black, every edge/.append style={{draw=black, densely dashed, opacity=.5}}, fill=lightgray]
                (0,0,0) coordinate (o) -- ++(-\\cubex,0,0) coordinate (a) -- ++(0,-\\cubey,0) coordinate (b) edge coordinate [pos=1] (g) ++(0,0,-\\cubez)  -- ++(\\cubex,0,0) coordinate (c) -- cycle
                (o) -- ++(0,0,-\\cubez) coordinate (d) -- ++(0,-\\cubey,0) coordinate (e) edge (g) -- (c) -- cycle
                (o) -- (a) -- ++(0,0,-\\cubez) coordinate (f) edge (g) -- (d) -- cycle;
              % Invisible lines for dimensions, but text remains visible
            \\path 
                (b) +(0,-7.5pt) coordinate (b1) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$I_1={tensor_shape[0]}$}} (b1 -| c)
                (b) +(-7.5pt,0) coordinate (b2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_1={tensor_ranks[1]}$}} (b2 |- a)
                (c) +(5.3pt,-5.3pt) coordinate (c2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$~$}} ([xshift=3.5pt,yshift=-3.5pt]e);
        \\end{{tikzpicture}}
        \\bullet 
        \\begin{{tikzpicture}}[baseline={{-0.5*{scaled_tensor_ranks[2]:2f}*{tikz_scaling}cm}}, scale={tikz_scaling}, every node/.style={{font=\\tiny}}, every edge quotes/.append style={{auto, text=black}}]
            \\pgfmathsetmacro{{\\cubex}}{{{scaled_tensor_shape[1]:2f}}}
            \\pgfmathsetmacro{{\\cubey}}{{{scaled_tensor_ranks[2]:2f}}}
            \\pgfmathsetmacro{{\\cubez}}{{{scaled_tensor_ranks[1]:2f}}}
            \\draw [draw=black, every edge/.append style={{draw=black, densely dashed, opacity=.5}}, fill=lightgray]
                (0,0,0) coordinate (o) -- ++(-\\cubex,0,0) coordinate (a) -- ++(0,-\\cubey,0) coordinate (b) edge coordinate [pos=1] (g) ++(0,0,-\\cubez)  -- ++(\\cubex,0,0) coordinate (c) -- cycle
                (o) -- ++(0,0,-\\cubez) coordinate (d) -- ++(0,-\\cubey,0) coordinate (e) edge (g) -- (c) -- cycle
                (o) -- (a) -- ++(0,0,-\\cubez) coordinate (f) edge (g) -- (d) -- cycle;
              % Invisible lines for dimensions, but text remains visible
            \\path 
                (b) +(0,-7.5pt) coordinate (b1) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$I_2={tensor_shape[1]}$}} (b1 -| c)
                (b) +(-7.5pt,0) coordinate (b2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_2={tensor_ranks[2]}$}} (b2 |- a)
                (c) +(5.3pt,-5.3pt) coordinate (c2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_1={tensor_ranks[1]}$}} ([xshift=3.5pt,yshift=-3.5pt]e);
        \\end{{tikzpicture}}
        \\bullet 
        \\begin{{tikzpicture}}[baseline={{-0.5*{scaled_tensor_ranks[3]:2f}*{tikz_scaling}cm}}, scale={tikz_scaling}, every node/.style={{font=\\tiny}}, every edge quotes/.append style={{auto, text=black}}]
            \\pgfmathsetmacro{{\\cubex}}{{{scaled_tensor_shape[2]:2f}}}
            \\pgfmathsetmacro{{\\cubey}}{{{scaled_tensor_ranks[3]:2f}}}
            \\pgfmathsetmacro{{\\cubez}}{{{scaled_tensor_ranks[2]:2f}}}
            \\draw [draw=black, every edge/.append style={{draw=black, densely dashed, opacity=.5}}, fill=lightgray]
                (0,0,0) coordinate (o) -- ++(-\\cubex,0,0) coordinate (a) -- ++(0,-\\cubey,0) coordinate (b) edge coordinate [pos=1] (g) ++(0,0,-\\cubez)  -- ++(\\cubex,0,0) coordinate (c) -- cycle
                (o) -- ++(0,0,-\\cubez) coordinate (d) -- ++(0,-\\cubey,0) coordinate (e) edge (g) -- (c) -- cycle
                (o) -- (a) -- ++(0,0,-\\cubez) coordinate (f) edge (g) -- (d) -- cycle;
              % Invisible lines for dimensions, but text remains visible
            \\path 
                (b) +(0,-7.5pt) coordinate (b1) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$I_3={tensor_shape[2]}$}} (b1 -| c)
                (b) +(-7.5pt,0) coordinate (b2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_3={tensor_ranks[3]}$}} (b2 |- a)
                (c) +(5.3pt,-5.3pt) coordinate (c2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_2={tensor_ranks[2]}$}} ([xshift=3.5pt,yshift=-3.5pt]e);
        \\end{{tikzpicture}}
        \\bullet 
        \\begin{{tikzpicture}}[baseline={{-0.5*{scaled_tensor_ranks[4]:2f}*{tikz_scaling}cm}}, scale={tikz_scaling}, every node/.style={{font=\\tiny}}, every edge quotes/.append style={{auto, text=black}}]
            \\pgfmathsetmacro{{\\cubex}}{{{scaled_tensor_shape[3]:2f}}}
            \\pgfmathsetmacro{{\\cubey}}{{{scaled_tensor_ranks[4]:2f}}}
            \\pgfmathsetmacro{{\\cubez}}{{{scaled_tensor_ranks[3]:2f}}}
            \\draw [draw=black, every edge/.append style={{draw=black, densely dashed, opacity=.5}}, fill=lightgray]
                (0,0,0) coordinate (o) -- ++(-\\cubex,0,0) coordinate (a) -- ++(0,-\\cubey,0) coordinate (b) edge coordinate [pos=1] (g) ++(0,0,-\\cubez)  -- ++(\\cubex,0,0) coordinate (c) -- cycle
                (o) -- ++(0,0,-\\cubez) coordinate (d) -- ++(0,-\\cubey,0) coordinate (e) edge (g) -- (c) -- cycle
                (o) -- (a) -- ++(0,0,-\\cubez) coordinate (f) edge (g) -- (d) -- cycle;
              % Invisible lines for dimensions, but text remains visible
            \\path 
                (b) +(0,-7.5pt) coordinate (b1) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$I_4={tensor_shape[3]}$}} (b1 -| c)
                (b) +(-7.5pt,0) coordinate (b2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$~$}} (b2 |- a)
                (c) +(5.3pt,-5.3pt) coordinate (c2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_3={tensor_ranks[3]}$}} ([xshift=3.5pt,yshift=-3.5pt]e);
        \\end{{tikzpicture}}
        \\label{{fig:ttd_}}
    \\end{{equation}}
    """

    return latex_code


def generate_tensor_ring_tikzpicture(tensor_shape, tensor_ranks):
    tensor_shape = np.array(tensor_shape, dtype=int)
    tensor_ranks = np.array(tensor_ranks, dtype=int)

    # scaling:
    max_val = np.maximum(tensor_shape.max(), tensor_ranks.max())

    power = 4

    scaled_tensor_shape = tensor_shape ** (1/power)
    scaled_tensor_ranks = tensor_ranks ** (1/power)

    # rel scaling
    # tensor_shape = tensor_shape / max_val
    # tensor_ranks = tensor_ranks / max_val

    # geometry scaling
    tikz_scaling = 0.65

    latex_code = "\\begin{equation}\n    \\mathcal{X} \\approx \\operatorname{\\mathbf{Tr}}\\left["

    for i in range(min(len(tensor_shape), len(tensor_ranks) - 1)):
        latex_code += f"""\\begin{{tikzpicture}}[baseline={{-0.5*{scaled_tensor_ranks[i + 1]:2f}*{tikz_scaling}cm}}, scale={tikz_scaling}, every node/.style={{font=\\tiny}}, every edge quotes/.append style={{auto, text=black}}]
            \\pgfmathsetmacro{{\\cubex}}{{{scaled_tensor_shape[i]:2f}}}
            \\pgfmathsetmacro{{\\cubey}}{{{scaled_tensor_ranks[i + 1]:2f}}}
            \\pgfmathsetmacro{{\\cubez}}{{{scaled_tensor_ranks[i]:2f}}}
            \\draw [draw=black, every edge/.append style={{draw=black, densely dashed, opacity=.5}}, fill=lightgray]
                (0,0,0) coordinate (o) -- ++(-\\cubex,0,0) coordinate (a) -- ++(0,-\\cubey,0) coordinate (b) edge coordinate [pos=1] (g) ++(0,0,-\\cubez)  -- ++(\\cubex,0,0) coordinate (c) -- cycle
                (o) -- ++(0,0,-\\cubez) coordinate (d) -- ++(0,-\\cubey,0) coordinate (e) edge (g) -- (c) -- cycle
                (o) -- (a) -- ++(0,0,-\\cubez) coordinate (f) edge (g) -- (d) -- cycle;
            % Invisible lines for dimensions, but text remains visible
            \\path 
                (b) +(0,-7.5pt) coordinate (b1) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$I_{i + 1}={tensor_shape[i]}$}} (b1 -| c)
                (b) +(-7.5pt,0) coordinate (b2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_{i + 1}={tensor_ranks[i + 1]}$}} (b2 |- a)
                (c) +(5.3pt,-5.3pt) coordinate (c2) edge [draw=none] node [sloped, allow upside down, auto=false, anchor=center, text=black] {{$R_{i}={tensor_ranks[i]}$}} ([xshift=3.5pt,yshift=-3.5pt]e);
        \\end{{tikzpicture}}{"," if i < min(len(tensor_shape), len(tensor_ranks) - 1) - 1 else ""}
        """

    latex_code += "\\right]\n    \\label{fig:trd_}\n\\end{equation}"

    return latex_code


if __name__ == "__main__":
    tensor_shapes = [39, 67, 189, 189]
    tensor_ranks = [1, 36, 150, 150, 1]
    tikz_code = generate_tensor_train_tikzpicture(tensor_shapes, tensor_ranks)
    print(tikz_code)

    print("\n\n\n\n")

    tensor_shapes = [39, 67, 189, 189]
    tensor_ranks = [6, 6, 100, 100, 6]
    tikz_code = generate_tensor_ring_tikzpicture(tensor_shapes, tensor_ranks)
    print(tikz_code)

