colormap = plt.get_cmap('hot')
norm = plt.Normalize(vmin=scores.min(), vmax=scores.max())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(X, Y, Z, 
                        c=scores, cmap=colormap, norm=norm)
