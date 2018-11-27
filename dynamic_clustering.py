def dist(xy):
    x,y = xy
    return (x**2 + y**2)**.5

def total(xys):
    return (sum([x for x, _ in xys]), sum([y for _ ,y in xys]))
    
def delta(xy1,xy2):
    return (xy2[0] - xy1[0], xy2[1] - xy1[1])

def biggest(xy):
    return abs(xy[0]) < abs(xy[1])
    
def cluster(data, radius=7, step_size=.1, max_iteration=1000):
    for _ in range(max_iteration):
        neighbours = {point: total([delta(point,neighbour ) for neighbour in data if dist(delta(point,neighbour)) <= radius ] ) for point in data }
        new_data =[]
        for point,centroid in neighbours.items():
            point = list(point)
            if dist(centroid) <= step_size:
                point[0] += centroid[0] 
                point[1] += centroid[1]
            else:
                b = biggest(centroid)
                point = list(point)
                point[b] += step_size
                point[1-b] += (step_size/centroid[b]) * step_size
            new_data.append(tuple(point))
        data = new_data
    return data


xs = [0,1,1,-3,-3,-6,4]#[0,1,2,5,-3,-6,4]
ys = [0,1,2,-5,-4,-5,4]#[0,-3,4,-5,4,5,0]
data = [xy for xy in zip(xs,ys)]
data = cluster(data)

for x,_ in data:
    print(x)
print()
for _,y in data:
    print(y)