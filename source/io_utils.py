import csv
import numpy as np
import pandas as pd
import networkx as nx

def load_grid_csv(linksfile_path, verticesfile_path):
    # Load csv files
    df_links = pd.read_csv(linksfile_path, sep=',')
    df_vertices = pd.read_csv(verticesfile_path, sep=',')
    # Create graph object
    graph = nx.Graph()
    # Add vertices and links to graph object
    vertices = df_vertices["v_id"] #.to_numpy_array()
    graph.add_nodes_from(vertices)
    positions = {} # position dictionary
    for idx, row in df_vertices.iterrows():
        lon = row['lon']
        lat = row['lat']
        v_id = row['v_id']
        # positions[row['v_id']] = (lon, lat)
        # positions[([lon, lat])
        # positions.append( row["v_id"] )
        # append tuple to dictionary
        positions[v_id] = (float(lon), float(lat)) # lon.replace(".", "")
    # Add node positions on map
    for idx, row in df_links.iterrows():
        # Get indices of connected vertices
        vi = row['v_id_1']
        vj = row['v_id_2']
        # print("Adding edge between {} and {}".format(vi, vj))
        graph.add_edge(vi, vj)
   
    return graph, positions