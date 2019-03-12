import json
import sys

#filter data
def filter(input_file, output_file):
    f = open(input_file)
    json_in = json.load(f)
    f.close()
    
    fc = {"type": "FeatureCollection", "features": []}
    for line in json_in:
        data = line["data"]
        if "latitude" in data: #there are multiple dictionaries called data that don't all have latitude key
            feature = {
                    "type": "Feature",
                    "properties": {"latitude": data["latitude"],
                                   "longitude": data["longitude"],
                                   "altitude": data["altitude"]},
                    "geometry": { "type": "Point",
                                  "coordinates": [data["longitude"],data["latitude"]]
                        }
            }
            fc["features"].append(feature)
        
    write = open(output_file, "w")
    json.dump(fc, write)
    write.close()
        
if __name__ == "__main__":
    filename_in = sys.argv[1]
    filename_out = sys.argv[2]
    filter(filename_in, filename_out)
        
                    
