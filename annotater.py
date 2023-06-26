# JSONLINES one line break down Information 

# {"id":"I4PD9040711.jpg_2000x700.jpg","image":"https://s3.amazonaws.com/image-processing.openpecha/Works/0b/W4PD759/images-web/W4PD759-I4PD904/I4PD9040711.jpg_2000x700.jpg?AWSAccessKeyId=AKIAWEXEWJ7GDFYE3KNU&Signature=In%2FuQFseETubRYHdai9vh16QtyU%3D&Expires=1719114980","_input_hash":293206308,"_task_hash":993718261,"_view_id":"image_manual","width":2000,"height":416,
#  "spans":[
#      {"id":"9d765c3a-7191-4d82-895e-45ee83e08f9d","label":"Line","color":"yellow","x":295.2,"y":98.5,"height":23.9,"width":1438.2,"center":[1014.3,110.45],"type":"rect","points":[[295.2,98.5],[295.2,122.4],[1733.4,122.4],[1733.4,98.5]]},
#      {"id":"6d242164-3137-4048-ae15-523a451891d5","label":"Line","color":"cyan","x":282.9,"y":160.3,"height":19.2,"width":1442.3,"center":[1004.05,169.9],"type":"rect","points":[[282.9,160.3],[282.9,179.5],[1725.2,179.5],[1725.2,160.3]]},
#      {"id":"3219bf41-4038-4cbc-94e6-a97e25b551a7","label":"Line","color":"magenta","x":285,"y":221.4,"height":19.7,"width":169.5,"center":[369.75,231.25],"type":"rect","points":[[285,221.4],[285,241.1],[454.5,241.1],[454.5,221.4]]},
#      {"id":"3d3e774f-1315-4400-ac9a-da6fa9f92fe7","label":"Line","color":"springgreen","x":456.6,"y":221.3,"height":13.9,"width":1270.7,"center":[1091.95,228.25],"type":"rect","points":[[456.6,221.3],[456.6,235.2],[1727.3,235.2],[1727.3,221.3]]},
#      {"id":"b14b9eff-5524-4ca0-9d0c-d359396f965d","label":"Line","color":"tomato","x":289.1,"y":279.1,"height":17,"width":939.7,"center":[758.95,287.6],"type":"rect","points":[[289.1,279.1],[289.1,296.1],[1228.8,296.1],[1228.8,279.1]]}
#      ],
#  "answer":"accept","_annotator_id":"line_segments-nyibum","_session_id":"line_segments-nyibum"}



import jsonlines

# Specify the path to the JSONL file
file_path = "line_segmentation.jsonl"

# Create a dictionary to store the count of lines segmented by each annotator
annotator_counts = {}
annotator_absent = []

# Open the JSONL file
with jsonlines.open(file_path) as reader:
    # Iterate over each line in the file (Note: line refers to one image jsonl line)
    for line in reader:
        # if annotator is present in line (Note: line refers to one image jsonl line)
        if "_annotator_id" in line:
            # Extract the annotator ID from the line (Note: line refers to one image jsonl line)
            annotator_id = line["_annotator_id"]
            # if new annotator found intialized new dictonary
            if annotator_id not in annotator_counts:
                annotator_counts[annotator_id]={
                                                'accept':{"counts":0,
                                                            "image_id":[]},

                                                'reject':{"counts":0,
                                                          "image_id":[]},

                                                'ignore':{"counts":0,
                                                          "image_id":[]},

                                                'no_span':{"counts":0,
                                                           "image_id":[]}                              
                }

            # if annotations is accepted
            if line["answer"]=="accept":
                # if line segmented by anotators in images (Note in one image: spans size = no of line segment)
                if "spans" in line:
                    # Count the number of spans in the current line (line refers to one image jsonl line)
                    line_count = len(line["spans"])
                    # Update the accepted count for the current annotator
                    annotator_counts[annotator_id]['accept']['counts'] += line_count
                    annotator_counts[annotator_id]['accept']['image_id'].append(line['id'])
                else:
                    # Update the no_span images count for the current annotator
                    annotator_counts[annotator_id]['no_span']['counts'] += 1
                    annotator_counts[annotator_id]['no_span']['image_id'].append(line['id'])
            else:
                # Update the rejected or ignored count for the current annotator
                annotator_counts[annotator_id][line['answer']]['counts'] += 1
                annotator_counts[annotator_id][line['answer']]['image_id'].append(line['id'])        
        else:
            annotator_absent.append(line['id'])
        

# Print the counts for each annotator
for annotator_id, count in annotator_counts.items():
    print(f"Annotator: {annotator_id}   segmented: {count['accept']['counts']} lines   Rejected:{count['reject']['counts']}    Ignored:{count['ignore']['counts']}   No_span: {count['no_span']['counts']}")


# View all lines with missing _annotator_id
print("\nImages whose Annotaters is not mentioned: ")
for img_id in annotator_absent:
    print(img_id)

# View specific category image_id for specific annotatators 
print("\nRejected images_id for annotator: 'line_segments-palden' ")
print(annotator_counts["line_segments-palden"]["reject"]["image_id"])





