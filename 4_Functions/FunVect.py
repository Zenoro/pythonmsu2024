def superposition(fs, gs):
    added = []
    for gss in gs:
        def gg(x, g=gss):
            return fs(g(x))
        added.append(gg)
    return added
