#!/bin/bash

# Create main directories
mkdir -p src/{agents,components,utils,services,state} \
         data/{processed,raw} \
         tests/{test_agents,test_components,test_workflows} \
         docs config scripts notebooks workflows

# Create __init__.py files
touch src/__init__.py \
      src/agents/__init__.py \
      src/components/__init__.py \
      src/utils/__init__.py \
      src/services/__init__.py \
      src/state/__init__.py \
      tests/__init__.py \
      tests/test_agents/__init__.py \
      tests/test_components/__init__.py \
      tests/test_workflows/__init__.py

# Move existing agent_pkm.py to src/
mv agent_pkm.py src/

# Create main.py
touch src/main.py

# Create config files
touch config/config.py
touch config/.env.example

echo "Project structure created successfully!"
