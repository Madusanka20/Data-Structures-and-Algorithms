from pyamaze import maze, agent, COLOR ,textLabel # Ensure correct import

def dijkstra(m,*h,start=None, goal=None):
    if start is None:
        start=(m.rows,m.cols)
    if goal is None:
        goal=(1,1)   

    hurdles = [(agent.position, getattr(agent, "cost", 0)) for agents in h for agent in agents]
    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}

    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]  #Current cell
        if currCell==(1,1):
            break
        
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[goal]



if __name__=='__main__':
    # Create the maze
    myMaze = maze(20, 20)
    myMaze.CreateMaze(loopPercent=6)

    # Define agents

    # Red agents
    red_agents=[
        agent(myMaze, 4, 4, color='red'),
        agent(myMaze, 16, 16, color='red'),  
        agent(myMaze, 13, 6, color='red')
    ]
    
    # Blue agents
    blue_agents = [
        agent(myMaze, 3, 3, color='blue'),
        agent(myMaze, 3, 4, color='blue'),
        agent(myMaze, 3, 5, color='blue'),
        agent(myMaze, 4, 5, color='blue'),
        agent(myMaze, 5, 5, color='blue'),
        agent(myMaze, 5, 4, color='blue'),
        agent(myMaze, 5, 3, color='blue'),
        agent(myMaze, 4, 3, color='blue'),
        
        agent(myMaze, 15, 15, color='blue'),
        agent(myMaze, 15, 16, color='blue'),
        agent(myMaze, 15, 17, color='blue'),
        agent(myMaze, 16, 15, color='blue'),
        agent(myMaze, 16, 17, color='blue'),
        agent(myMaze, 17, 15, color='blue'),
        agent(myMaze, 17, 16, color='blue'),
        agent(myMaze, 17, 17, color='blue'),

        agent(myMaze, 12, 5, color='blue'),
        agent(myMaze, 12, 6, color='blue'),
        agent(myMaze, 12, 7, color='blue'),
        agent(myMaze, 13, 5, color='blue'),
        agent(myMaze, 13, 7, color='blue'),
        agent(myMaze, 14, 5, color='blue'),
        agent(myMaze, 14, 6, color='blue'),
        agent(myMaze, 14, 7, color='blue')
    ]

    # Yellow agents
    yellow_agents = [
        agent(myMaze, 2, 2, color='yellow'),
        agent(myMaze, 2, 3, color='yellow'),
        agent(myMaze, 2, 4, color='yellow'),
        agent(myMaze, 2, 5, color='yellow'),
        agent(myMaze, 2, 6, color='yellow'),
        agent(myMaze, 3, 2, color='yellow'),
        agent(myMaze, 3, 6, color='yellow'),
        agent(myMaze, 4, 2, color='yellow'),
        agent(myMaze, 4, 6, color='yellow'),
        agent(myMaze, 5, 2, color='yellow'),
        agent(myMaze, 5, 6, color='yellow'),
        agent(myMaze, 6, 2, color='yellow'),
        agent(myMaze, 6, 3, color='yellow'),
        agent(myMaze, 6, 4, color='yellow'),
        agent(myMaze, 6, 5, color='yellow'),
        agent(myMaze, 6, 6, color='yellow'),

        agent(myMaze, 14, 14, color='yellow'),
        agent(myMaze, 14, 15, color='yellow'),
        agent(myMaze, 14, 16, color='yellow'),
        agent(myMaze, 14, 17, color='yellow'),
        agent(myMaze, 14, 18, color='yellow'),
        agent(myMaze, 15, 14, color='yellow'),
        agent(myMaze, 17, 14, color='yellow'),
        agent(myMaze, 17, 18, color='yellow'),
        agent(myMaze, 16, 14, color='yellow'),
        agent(myMaze, 16, 18, color='yellow'),
        agent(myMaze, 15, 18, color='yellow'),
        agent(myMaze, 18, 18, color='yellow'),
        agent(myMaze, 18, 17, color='yellow'),
        agent(myMaze, 18, 16, color='yellow'),
        agent(myMaze, 18, 15, color='yellow'),
        agent(myMaze, 18, 14, color='yellow'),

        agent(myMaze, 11, 4, color='yellow'),
        agent(myMaze, 11, 5, color='yellow'),
        agent(myMaze, 11, 6, color='yellow'),
        agent(myMaze, 11, 7, color='yellow'),
        agent(myMaze, 11, 8, color='yellow'),
        agent(myMaze, 12, 4, color='yellow'),
        agent(myMaze, 14, 4, color='yellow'),
        agent(myMaze, 14, 8, color='yellow'),
        agent(myMaze, 13, 4, color='yellow'),
        agent(myMaze, 13, 8, color='yellow'),
        agent(myMaze, 12, 8, color='yellow'),
        agent(myMaze, 15, 8, color='yellow'),
        agent(myMaze, 15, 7, color='yellow'),
        agent(myMaze, 15, 6, color='yellow'),
        agent(myMaze, 15, 5, color='yellow'),
        agent(myMaze, 15, 4, color='yellow')
    ]

    # Assign cost values efficiently
    red_cost = 40
    blue_cost = 20

    # Assign cost to red agents
    for red in red_agents:
        red.cost = red_cost

    # Assign cost to blue agents
    for blue in blue_agents:
        blue.cost = blue_cost


    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c=dijkstra(myMaze,red_agents,blue_agents,yellow_agents,start=(20,10),goal=(6,14))
    textLabel(myMaze,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(myMaze,20,10,color=COLOR.cyan,filled=True,footprints=True)
    myMaze.tracePath({a:path})

    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c=dijkstra(myMaze,red_agents,blue_agents,yellow_agents,start=(6,14),goal=(16,7))
    textLabel(myMaze,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(myMaze,6,14,color=COLOR.yellow,filled=True,footprints=True)
    myMaze.tracePath({a:path})

    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c=dijkstra(myMaze,red_agents,blue_agents,yellow_agents,start=(16,7),goal=(17,19))
    textLabel(myMaze,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(myMaze,16,7,color=COLOR.green,filled=True,footprints=True)
    myMaze.tracePath({a:path})

    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c=dijkstra(myMaze,red_agents,blue_agents,yellow_agents,start=(17,19),goal=(20,10))
    textLabel(myMaze,'Total Cost',c)

    # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    a=agent(myMaze,17,19,color=COLOR.red,filled=True,footprints=True)
    myMaze.tracePath({a:path})

    



    # Green agents (Survivors)
    s1 = agent(myMaze, 6, 14, color='green')
    s2 = agent(myMaze, 16, 7, color='green')
    s3 = agent(myMaze, 17, 19, color='green')

    # Run the maze
    myMaze.run()
