# Procedurally Generated Vase

This is a procedurally generated vase in the program Grasshopper written in python with RhinoScript. The vase is 3d printable.

## Summary

This program procedurally generates a vase by using Grasshoppers existing Library for 3d shape generation. The algorithm works by generating a random number of points then creating a NURBS curve, an offset surface function will be used to add a thickness to the vase for 3d printing.

## Timeline

Road map for this project.

- Week 0: Write Proposal
- Week 1: Pivioted from using Houdini to Grasshopper. Clearer workflow and community support for my type of application.
- Week 2: Able to generate a static thin vase using python in grasshopper.
- Week 3: Added random points from set ranges.
- Week 4: Added points to base for flat bottom and thickened for 3d printing.

## Challenges

- Sticking with Houdini for so long was frustrating becuase I was having to learn two applications at the same time for something it generally isn't used for.
Understanding how NURBS curves are generated is much more complex then using Rhino itself. I still don't fully understand the knot system but it only has slight effect (unnoticable but potential for more control).
Generating a NURBS curve with full multiplicity for the start and end was challenging.
Error messages and debugging is horrible in grasshopper, there is no line count and messages are unclear.

## Completed Work

Upload photos and videos of your completed final project!

Also upload the code that makes up your project to your repository.

## References and links

RhinoScript Python Docs
https://developer.rhino3d.com/api/RhinoScriptSyntax/

## Prerequisites 
Must have Rhino3D installed
If not preinstalled download the Grasshopper plugin for Rhino3D
If not preinstalled download the PythonScripting plugin for Grasshopper for Rhino3D

# How to 

## Step 1

Download all files from this repository. 

## Step 2

Open the necessary applications to navigate to Grasshopper.

## Step 3

Select Open from file < open and navigate to proceduralVase.gh

## Step 4

Open python scripting component in grasshopper

## Step 5 (Optional)

Adjust variable ranges in options area

## Step 6

Run python scripting component and bake to layer.

## Step 7 (Optional)

Export to .stl and open in your 3d printing program. Follow the 3d printing for Rhino3D. Enjoy your procedurally generated print!
