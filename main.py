import numpy as np
import open3d as o3d

print("Load a ply point cloud, print it, and render it")
pcd1 = o3d.io.read_point_cloud("PointCould.xyz")  # 这里的cat.ply替换成需要查看的点云文件
o3d.visualization.draw_geometries([pcd1])

pcd2 = o3d.io.read_point_cloud("fandisk1.xyz")
o3d.visualization.draw_geometries([pcd2])

pcd3 = o3d.io.read_point_cloud("fandisk2.xyz")
o3d.visualization.draw_geometries([pcd3])