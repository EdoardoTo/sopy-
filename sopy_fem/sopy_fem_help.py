import json
import os
import sys

exampleTypesSet = {"dynamics_TRUSS02",
                    "electrical_BR02",
                    "mechanics_BR02",
                    "mechanics_QU04",
                    "mechanics_TR03",
                    "structural_TRUSS02",
                    "thermal_BR02"
                }

def sopy_fem_help(exampleType="", basePath="sopy_fem/sopy_fem/Examples/"):
    if (exampleType in exampleTypesSet):
        fileName = basePath + exampleType + "/data.json"
        with open(fileName, "r") as exampleFile:
            jsonText = json.load(exampleFile)

        print(json.dumps(jsonText, indent=4))
    else:
        print("Please choose one of the following examples types:\n")
        for exampleType in exampleTypesSet:
            print("  - ", exampleType)


if __name__ == '__main__':
    args = sys.argv[1:]
    exampleType = ""
    basePath= "Examples/"
    if (len(args)  != 0):
        exampleType = args[0]
    sopy_fem_help(exampleType, basePath)
