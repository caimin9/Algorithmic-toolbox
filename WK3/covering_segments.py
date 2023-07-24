import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # Sort segments based on their end points
    segments.sort(key=lambda x: x.end)
    points = []
    
    while segments:
        # Select the end point of the first segment
        point = segments[0].end
        points.append(point)
        # Remove all segments that contain this point
        segments = [s for s in segments if s.start > point]

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

