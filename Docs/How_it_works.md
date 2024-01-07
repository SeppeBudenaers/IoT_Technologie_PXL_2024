## Basic schematic
Basic schematic of the docker workflow:

```mermaid
graph LR;
	classDef green stroke:#0f3
	classDef Blue stroke:#05f
	subgraph User
		
    	Dockerfile-->push[Commit to\nGithub];
    end
    
    push-->GA;
    
    subgraph Github
    	direction TB
    	GA[Github actions\nBuilds Docker]:::Blue;
    	DH[Pushes to\nDockerhub]:::Blue;
    	GA-->DH;
    end
    
    DH-->PI;
    
    subgraph Pi
	    direction TB
    	PI[Raspberry pi\nPulls \nfrom dockerhub]:::green;
    	APP[Pi runs \ncontainer]:::green;
		PI-->APP;
	end
```



