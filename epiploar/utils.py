import numpy as np
import matplotlib.pyplot as plt



def compute_fundamental_matrix_normalized(points1, points2):
 
    assert points1.shape[0] == points2.shape[0], "no. of points don't match"
    
    c1 = np.mean(points1, axis=0)
    c2 = np.mean(points2, axis=0)
    
    # compute the scaling factor
    s1 = np.sqrt(2 / np.mean(np.sum((points1 - c1) ** 2, axis=1)))
    s2 = np.sqrt(2 / np.mean(np.sum((points2 - c2) ** 2, axis=1)))
    
    # compute the normalization matrix for both the points
    T1 = np.array([
        [s1, 0, -s1 * c1[0]],
        [0, s1, -s1 * c1[1]],
        [0, 0 ,1]
    ])
    T2 = np.array([
        [s2, 0, -s2 * c2[0]],
        [0, s2, -s2 * c2[1]],
        [0, 0, 1]
    ])
    
    
    points1_n = T1 @ points1.T # normalize the points
    points2_n = T2 @ points2.T
    
    F_n = compute_fundamental_matrix(points1_n.T, points2_n.T)
    
    # de-normalize the fundamental
    return T2.T @ F_n @ T1

def compute_fundamental_matrix(points1, points2):

    assert points1.shape[0] == points2.shape[0], "no. of points don't match"
    
    u1 = points1[:, 0]
    v1 = points1[:, 1]
    u2 = points2[:, 0]
    v2 = points2[:, 1]
    one = np.ones_like(u1)
    
    # A = [u2.u1, u2.v1, u2, v2.u1, v2.v1, v2, u1, v1, 1] for all the points
    A = np.c_[u1 * u2, v1 * u2, u2, u1 * v2, v1 * v2, v2, u1, v1, one]
    
    
    U, S, V = np.linalg.svd(A, full_matrices=True) # peform svd on A and find the minimum value of |Af|
    f = V[-1, :]
    F = f.reshape(3, 3)
    
    
    
    U, S, V = np.linalg.svd(F, full_matrices=True)
    S[-1] = 0 # constrain F and make rank 2 by zeroing out last singular value
    F = U @ np.diag(S) @ V # recombine again
    return F

def plot_line(coeffs, xlim):

    a, b, c = coeffs
    x = np.linspace(xlim[0], xlim[1], 100)
    y = (a * x + c) / -b
    return x, y

def plot_epipolar_lines(img1, img2, points1, points2):

    
    h, w, c = img1.shape
    n = points1.shape[0]
    
    F = compute_fundamental_matrix_normalized(points1, points2)
    
    nrows = 2
    ncols = 1
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6, 8))
    
    ax1 = axes[0]
    ax1.set_title("Image 1")
    ax1.imshow(img1)
    
    ax2 = axes[1]
    ax2.set_title("Image 2")
    ax2.imshow(img2)
    
    for i in range(n):
        p1 = points1.T[:, i]
        p2 = points2.T[:, i]
        
        
        coeffs = p2.T @ F # Epipolar line in the image of camera 1 given the points in the image of camera 2
        x, y = plot_line(coeffs, (-1500, w))
        ax1.plot(x, y, color="orange")
        ax1.scatter(*p1.reshape(-1)[:2], color="blue")

        
        coeffs = F @ p1
        x, y = plot_line(coeffs, (0, 2500))
        ax2.plot(x, y, color="orange")
        ax2.scatter(*p2.reshape(-1)[:2], color="blue")
        
    ax1.set_xlim(0, w)
    ax1.set_ylim(h, 0)
    ax2.set_xlim(0, w)
    ax2.set_ylim(h, 0)

    plt.tight_layout()
    plt.show()




