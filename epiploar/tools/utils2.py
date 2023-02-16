import cv2
import numpy as np
from matplotlib import pyplot as plt




make_line = lambda u, v: np.vstack((u, v)).T


# basis vectors
x = np.array([1, 0, 0])
y = np.array([0, 1, 0])
z = np.array([0, 0, 1])

# basis vectors as homogeneous coordinates
xh = np.array([1, 0, 0, 1])
yh = np.array([0, 1, 0, 1])
zh = np.array([0, 0, 1, 1]) 

def Rx(theta):
  return np.array([[ 1, 0           , 0           ],
                   [ 0, np.cos(theta),-np.sin(theta)],
                   [ 0, np.sin(theta), np.cos(theta)]], dtype="float32")
  
def Ry(theta):
  return np.array([[ np.cos(theta), 0, -np.sin(theta)],
                   [ 0           , 1, 0           ],
                   [np.sin(theta), 0, np.cos(theta)]], dtype="float32")
  
def Rz(theta):
  return np.array([[ np.cos(theta), -np.sin(theta), 0 ],
                   [ np.sin(theta), np.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]], dtype="float32")


def create_rotation_transformation_matrix(angles, axis_info):
    
    ''' The rotation is in anti-clockwise direction in a left handed axial system
    angles(list) - radians
    axis_info(str) - axis in which to rotate '''
    
    fn_mapping = {'x': Rx, 'y': Ry, 'z': Rz}
    net = np.identity(3)
    for angle, axis in list(zip(angles, axis_info))[::-1]:
        if fn_mapping.get(axis) is None:
            raise ValueError("Invalid axis")
        R = fn_mapping.get(axis)
        net = np.matmul(net, R(angle))
        
    return net

def create_translation_matrix(offset):
    
    '''
    translates a vetor by an offset(3,)
    Returns T(4, 4)'''

    T = np.identity(4)
    T[:3, 3] = offset
    return T



def create_rotation_change_of_basis_matrix(transformation_matrix):
    '''
    Creates a rotation change of basis matrix
    '''
  
    xt = transformation_matrix.T @ x.reshape(3, 1)
    yt = transformation_matrix.T @ y.reshape(3, 1)
    zt = transformation_matrix.T @ z.reshape(3, 1)
    
    return np.hstack((xt, yt, zt))


    
def compute_intrinsic_parameter_matrix(f, s, a, cx, cy):

    K = np.array([[ f,   s, cx],
                   [ 0, a*f, cy],
                   [ 0,   0,  1]], dtype="float32")

    return K

def compute_image_projection(points, K):
    '''
    Compute projection of points onto the image plane
    
    points(3, n_points)
        points we want to project onto the image plane should be represented in the camera coordinate system
    K(3, 3) camera intrinsic matrix

    '''
        
    h_points_i = K @ points
    
    h_points_i[0, :] = h_points_i[0, :] / h_points_i[2, :]
    h_points_i[1, :] = h_points_i[1, :] / h_points_i[2, :]

    points_i = h_points_i[:2, :]    # (2, n_points) the projected points on the image
    
    return points_i

def generate_random_points(n_points, xlim, ylim, zlim):

    x = np.random.randint(xlim[0], xlim[1], size=n_points)
    y = np.random.randint(ylim[0], ylim[1], size=n_points)
    z = np.random.randint(zlim[0], zlim[1], size=n_points)
    
    return np.vstack((x, y, z))

def compute_coordniates_wrt_camera(world_points, E, is_homogeneous=False):
    '''
    Performs a change of basis operation from the world coordinate system
    to the camera coordinate system
    
    Parameters
    ------------
    world_points - np.ndarray, shape - (3, n_points) or (4, n_points)
             points in the world coordinate system
    E - np.ndarray, shape - (3, 4)
        the camera extrinsic matrix
    is_homogeneous - boolean
        whether the coordinates are represented in their homogeneous form
        if False, an extra dimension will  be added for computation
        
    Returns
    ----------
    points_c - np.ndarray, shape - (3, n_points)
             points in the camera coordinate system
    '''
    if not is_homogeneous:
        # convert to homogeneous coordinates
        points_h = np.vstack((world_points, np.ones(world_points.shape[1])))
        
    points_c = E @ points_h
    return points_c


def compute_world2img_projection(world_points, M, is_homogeneous=False):
    '''
    Given a set of points in the world and the overall camera matrix,
    compute the projection of world points onto the image
    
    Parameters
    -----------
    world_points (3, n_points) -  points in the world coordinate system
                   
    M(3, 4) - The overall camera matrix which is a composition of the extrinsic and intrinsic matrix
        
    is_homogeneous - boolean
        whether the coordinates are represented in their homogeneous form
        if False, an extra dimension will  be added for computation

    '''
    if not is_homogeneous:
        # convert to homogeneous coordinates
        world_points = np.vstack((world_points, np.ones(world_points.shape[1])))
        
    h_points_i = M @ world_points
    
    h_points_i[0, :] = h_points_i[0, :] / h_points_i[2, :]
    h_points_i[1, :] = h_points_i[1, :] / h_points_i[2, :]

    points_i = h_points_i[:2, :]    # projections(2, n_points) - projections of the world points onto the image
    
    return points_i