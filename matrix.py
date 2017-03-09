import math

def make_translate( x, y, z ):
    trans = new_matrix()
    ident(trans)
    trans[3][0] = x
    trans[3][1] = y
    trans[3][2] = z
    return trans

def make_scale( x, y, z ):
    scale = new_matrix()
    scale[0][0] = x
    scale[1][1] = y
    scale[2][2] = z
    scale[3][3] = 1
    return scale
    
def make_rotX( theta ):    
    #x,y*math.cos(theta)-z*math.sin(theta),z*math.cos(theta)+y*math.sin(theta)
    rotX = new_matrix()
    theta*=math.pi/180
    rotX[0][0] = 1
    rotX[1][1] = math.cos(theta)
    rotX[1][2] = -1*math.sin(theta)
    rotX[2][1] = math.sin(theta)
    rotX[2][2] = math.cos(theta)    
    rotX[3][3] = 1
    return rotX
            
def make_rotY( theta ):
    #x*math.cos(theta)+z*math.sin(theta), y, z*math.cos(theta)-x*math.sin(theta
    rotY = new_matrix()
    theta*=math.pi/180
    rotY[0][0] = math.cos(theta)
    rotY[0][2] = math.sin(theta)
    rotY[1][1] = 1
    rotY[2][0] = -1*math.sin(theta)
    rotY[2][2] = math.cos(theta)
    rotY[3][3] = 1
    return rotY

def make_rotZ( theta ):
    #x*cos(theta) - y*sin(theta), x*sin(theta)+ y*cos(theta), z
    rotZ = new_matrix()
    theta*=math.pi/180
    rotZ[0][0] = math.cos(theta)
    rotZ[0][1] = -1*math.sin(theta)
    rotZ[1][0] = math.sin(theta)
    rotZ[1][1] = math.cos(theta)    
    rotZ[2][2] = 1
    rotZ[3][3] = 1
    return rotZ

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def int_matrix(m):
    for r in range( len( m[0] ) ):
        for c in range (len(m) ):
          m[c][r] = int(m[c][r])
