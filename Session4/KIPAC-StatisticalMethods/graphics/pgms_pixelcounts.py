from matplotlib import rc
import daft

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM([4, 2], origin=[0.65, 0.35], observed_style="inner")
pgm.add_node(daft.Node("theta", r"$\theta$", 1, 2, fixed=False))
pgm.add_node(daft.Node("F", r"$F_k$", 2, 1, fixed=True, offset=[3,0]))
pgm.add_node(daft.Node("T", r"$T$", 2.25, 1.85, fixed=True))
pgm.add_node(daft.Node("mu", r"$\mu_k$", 3, 1, fixed=True, offset=[5,-1]))
pgm.add_node(daft.Node("N", r"$N_k$", 4, 1, observed=True))
pgm.add_edge("theta", "F")
pgm.add_edge("F", "mu")
pgm.add_edge("T", "mu")
pgm.add_edge("mu", "N")
pgm.add_plate(daft.Plate([1.5, 0.5, 3, 1.1], label=r"pixels $k$", position='bottom left'))
pgm.render()
pgm.figure.savefig("pgms_pixelcounts.png", dpi=200)

pgm = daft.PGM([4, 2], origin=[0.65, 0.35], observed_style="inner")
pgm.add_node(daft.Node("theta", r"$\theta$", 1, 2, fixed=True))
pgm.add_node(daft.Node("F", r"$F_k$", 2, 1, fixed=True, offset=[3,0]))
pgm.add_node(daft.Node("T", r"$T$", 2.25, 1.85, fixed=True))
pgm.add_node(daft.Node("mu", r"$\mu_k$", 3, 1, fixed=True, offset=[5,-1]))
pgm.add_node(daft.Node("N", r"$N_k$", 4, 1, observed=True))
pgm.add_edge("theta", "F")
pgm.add_edge("F", "mu")
pgm.add_edge("T", "mu")
pgm.add_edge("mu", "N")
pgm.add_plate(daft.Plate([1.5, 0.5, 3, 1.1], label=r"pixels $k$", position='bottom left'))
pgm.render()
pgm.figure.savefig("pgms_pixelcounts2.png", dpi=200)
