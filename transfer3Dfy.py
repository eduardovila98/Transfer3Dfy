import numpy as np

def three2two(r1,r2):
    
    #It forces the r1 to be in the positive x-axis
    
    #Rotate about z-axis until r1 vector projection coincides with positive x-axis
    r1v1 = np.trranspose([r1])
    r2v1 = np.transpose([r2])
    theta1 = np.angle(complex(r1v1[0],r1v1[1]), deg=False)
    if theta1 < 0:
        theta1 = theta1 + 2*np.pi
    c1, s1 = np.cos(-theta1), np.sin(-theta1)
    R1 = np.array(((c1, -s1, 0.0), (s1, c1, 0.0), (0.0, 0.0, 1.0)))
    r1v2 = np.dot(R1,r1v1)
    r2v2 = np.dot(R1,r2v1)
    #clean it
    r1v2[1] = 0.0

    #Rotate about new y-axis until r1 lies on the positive x-axis
    theta2 = float(np.arctan(r1v2[2]/r1v2[0]))
    c2, s2 = np.cos(theta2), np.sin(theta2)
    R2 = np.array(((c2, 0.0, s2), (0.0, 1.0, 0.0), (-s2, 0.0, c2)))
    r1v3 = np.dot(R2,r1v2)
    r2v3 = np.dot(R2,r2v2)
    #clean it
    r1v3[1], r1v3[2] = 0.0, 0.0

    #Rotate about new x-axis until r2 lies in x-y plane
    theta3 = float(np.arctan(r2v3[2]/r2v3[1]))
    c3, s3 = np.cos(-theta3), np.sin(-theta3)
    R3 = np.array(((1.0, 0.0, 0.0), (0.0, c3, -s3), (0.0, s3, c3)))
    r1vf = np.dot(R3,r1v3)
    r2vf = np.dot(R3,r2v3)
    
    #Reduced them to 2D tuples
    r1vf = (float(r1vf[0]), 0.0)
    r2vf = (float(r2vf[0]), float(r2vf[1]))
    
    #join the 3 angles in a tuple
    angles = (theta1, theta2, theta3)
    
    return r1vf, r2vf, angles


def two2three(angles, r1, r2, v1, v2, x, y, vx, vy):
    
    #add 0.0 to the z coordinate
    r1vf = np.transpose([r1+(0.0,)])
    r2vf = np.transpose([r2+(0.0,)])
    v1vf = np.transpose([v1+(0.0,)])
    v2vf = np.transpose([v2+(0.0,)])

    theta1, theta2, theta3 = angles #extract angles
    #calculate cos and sin
    c3, s3 = np.cos(theta3), np.sin(theta3)
    c2, s2 = np.cos(-theta2), np.sin(-theta2)
    c1, s1 = np.cos(theta1), np.sin(theta1)
    
    #Create rotation matrices
    R3 = np.array(((1.0, 0.0, 0.0), (0.0, c3, -s3), (0.0, s3, c3)))
    R2 = np.array(((c2, 0.0, s2), (0.0, 1.0, 0.0), (-s2, 0.0, c2)))
    R1 = np.array(((c1, -s1, 0.0), (s1, c1, 0.0), (0.0, 0.0, 1.0)))
    #Dot them into one
    R = np.dot(R1,np.dot(R2,R3))
    
    #Rotate r and v
    r1v1 = np.dot(R,r1vf)
    r2v1 = np.dot(R,r2vf)
    v1v1 = np.dot(R,v1vf)
    v2v1 = np.dot(R,v2vf)
    
    #apply rotation to all points and velocities of trajectory
    N = len(x)
    xr = np.array([0.0] * N)
    yr = np.array([0.0] * N)
    zr = np.array([0.0] * N)
    vxr = np.array([0.0] * N)
    vyr = np.array([0.0] * N)
    vzr = np.array([0.0] * N)
    
    for i in range(N):
        r = np.transpose(np.array([[x[i], y[i], 0.0]]))
        r = np.dot(R,r)
        #save it
        xr[i] = r[0]
        yr[i] = r[1]
        zr[i] = r[2]
        
        #now for the velocities
        v = np.transpose(np.arrat([[vx[i], vy[i], 0.0]]))
        v = np.dot(R,v)
        #save it
        vxr[i] = v[0]
        vyr[i] = v[1]
        vzr[i] = v[2]

    return r1v1, r2v1, v1v1, v2v1, xr, yr, zr, vxr, vyr, vzr